import re


def extrair_receita(transcricao: str) -> dict:
    """
    Extrai os ingredientes e o modo de preparo da transcrição.

    Parâmetros:
        transcricao (str): Texto da transcrição do vídeo.

    Retorna:
        dict: Dicionário com 'ingredientes', 'modo_de_preparo' e 'transcricao'.
              Se não for possível extrair a receita, retorna a transcrição completa.
    """
    if not transcricao:
        return {"erro": "A transcrição está vazia."}

    # Expressões regulares para detectar seções de ingredientes e modo de preparo
    padrao_ingredientes = r"(ingredientes[:\s\n]*)(.+?)(\n\n|modo de preparo|\Z)"
    padrao_preparo = r"(modo de preparo[:\s\n]*)(.+)"

    # Tentar encontrar a lista de ingredientes
    ingredientes_match = re.search(
        padrao_ingredientes, transcricao, re.IGNORECASE | re.DOTALL
    )
    ingredientes = ingredientes_match.group(2).strip() if ingredientes_match else None

    # Tentar encontrar o modo de preparo
    preparo_match = re.search(padrao_preparo, transcricao, re.IGNORECASE | re.DOTALL)
    preparo = preparo_match.group(2).strip() if preparo_match else None

    # Se não encontrar ingredientes ou modo de preparo, retornar a transcrição completa
    if not ingredientes or not preparo:
        return {
            "ingredientes": [],
            "modo_de_preparo": "",
            "transcricao": transcricao,  # Transcrição completa para a IA interpretar
        }

    # Processar ingredientes
    if isinstance(ingredientes, str):
        ingredientes = [i.strip() for i in ingredientes.split("\n") if i.strip()]
    else:
        ingredientes = []

    return {
        "ingredientes": ingredientes,
        "modo_de_preparo": preparo,
        "transcricao": "",  # Não precisa da transcrição completa se a receita foi extraída
    }
