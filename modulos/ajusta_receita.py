from langchain_groq import ChatGroq
from groq import RateLimitError
from dotenv import load_dotenv
import os
import re

# Carrega as variáveis de ambiente
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")


def ajustar_receita(receita: dict) -> dict:
    """
    Ajusta a receita usando IA para completar ingredientes, sugerir ajustes e fornecer dicas.
    Se o vídeo não for de receita, retorna uma mensagem engraçada.

    Parâmetros:
        receita (dict): Dicionário com 'ingredientes', 'modo_de_preparo' e 'transcricao'.

    Retorna:
        dict: Dicionário com a receita ajustada e dicas do chef.
              Se o vídeo não for de receita, retorna uma mensagem engraçada.
    """
    try:
        # Conecta ao Groq usando a chave de API do arquivo .env
        chat = chat = ChatGroq(api_key=api_key, model="llama-3.3-70b-versatile")

        # Prompt para a IA
        prompt = f"""
        Você é um chef renomado com mais de 20 anos de experiência. Sua tarefa é analisar a transcrição abaixo e:
        1. Verificar se o conteúdo do vídeo é sobre uma receita.
        2. Se for uma receita:
           - Extrair os ingredientes e o modo de preparo.
           - Completar ingredientes ou quantidades faltantes, se necessário.
           - Sugerir ajustes no modo de preparo.
           - Informar o tempo de preparo e a quantidade de porções.
           - Dar dicas profissionais sobre temperatura, tempo de cozimento e técnicas.
        3. Se NÃO for uma receita:
           - Responder com uma mensagem engraçada, indicando que o vídeo não é sobre culinária.

        Transcrição:
        {receita["transcricao"]}

        Responda no seguinte formato:
        - Se for uma receita:
          - Ingredientes ajustados: [lista de ingredientes ajustados]
          - Modo de preparo ajustado: [texto com o modo de preparo ajustado]
          - Tempo de preparo: [tempo estimado]
          - Quantidade de porções: [quantidade de porções]
          - Dicas do chef: [texto com dicas profissionais]
        - Se NÃO for uma receita:
          - Mensagem: [mensagem engraçada]
        """

        # Enviando prompt
        resposta = chat.invoke(prompt)

        # Acessa o conteúdo da resposta
        conteudo_resposta = resposta.content

        # Verifica se a resposta é uma receita ou uma mensagem engraçada
        if "Mensagem:" in conteudo_resposta:
            return {"mensagem": conteudo_resposta.split("Mensagem:")[1].strip()}
        else:
            # Processa a resposta da IA para uma receita
            return {
                "ingredientes_ajustados": conteudo_resposta.split(
                    "Ingredientes ajustados:"
                )[1]
                .split("Modo de preparo ajustado:")[0]
                .strip(),
                "modo_de_preparo_ajustado": conteudo_resposta.split(
                    "Modo de preparo ajustado:"
                )[1]
                .split("Tempo de preparo:")[0]
                .strip(),
                "tempo_de_preparo": conteudo_resposta.split("Tempo de preparo:")[1]
                .split("Quantidade de porções:")[0]
                .strip(),
                "quantidade_porcoes": conteudo_resposta.split("Quantidade de porções:")[
                    1
                ]
                .split("Dicas do chef:")[0]
                .strip(),
                "dicas_do_chef": conteudo_resposta.split("Dicas do chef:")[1].strip(),
            }

    except RateLimitError as e:
        # Captura o erro de limite de uso e extrai o tempo de espera
        mensagem_erro = str(e)
        tempo_espera = re.search(r"Por favor volte em (\d+m\d+\.\d+s)", mensagem_erro)

        if tempo_espera:
            tempo_espera = tempo_espera.group(1)
            mensagem_amigavel = (
                "⚠️ **Ops! Parece que você cozinhou demais!** 🍳🔥\n\n"
                "Você excedeu o limite de requisições para o serviço de IA. "
                f"Por favor, aguarde **{tempo_espera}** enquanto a gente 'resfria os motores' e tente novamente. 😅"
            )
        else:
            mensagem_amigavel = (
                "⚠️ **Ops! Parece que você cozinhou demais!** 🍳🔥\n\n"
                "Você excedeu o limite de requisições para o serviço de IA. "
                "Por favor, aguarde alguns minutos e tente novamente. 😅"
            )

        return {"erro": mensagem_amigavel}

    except Exception as e:
        # Captura outros erros e exibe uma mensagem genérica
        mensagem_erro = (
            "⚠️ **Ocorreu um erro ao processar a receita.**\n\n"
            "Por favor, tente novamente mais tarde ou verifique o link do vídeo.\n\n"
            f"Detalhes do erro: {str(e)}"
        )
        return {"erro": mensagem_erro}
