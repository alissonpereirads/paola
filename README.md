# 🍽️ Paola - Extrator de Receitas do YouTube

Bem-vindo a Paola, um projeto de estudo que utiliza técnicas de LLM (Large Language Models) e ferramentas para extrair e ajustar receitas de vídeos do YouTube. Este projeto foi desenvolvido como parte do meu portfólio de estudos em Ciência de Dados e Inteligência Artificial, com o objetivo de explorar o potencial das LLMs e frameworks como LangChain e Streamlit.

## 🚀 Sobre o Projeto

Paola é uma aplicação que permite extrair receitas de vídeos do YouTube de forma automatizada. Ele utiliza a transcrição do vídeo para identificar ingredientes, modo de preparo, tempo de cozimento e outras informações relevantes. Além disso, caso algo esteja faltando na receita, a aplicação utiliza uma IA especializada (com prompt de um chef renomado) para completar os detalhes e garantir que a receita seja bem-sucedida.

### Funcionalidades Principais:
- Extrair receitas de vídeos do YouTube.
- Completar informações faltantes na receita (ingredientes, quantidades, modo de preparo, etc.).
- Sugerir dicas profissionais para garantir o sucesso da receita.
- Identificar vídeos que não são de receita e responder com uma mensagem humorística.

## 🛠️ Ferramentas e Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes ferramentas e tecnologias:

### Frameworks e Bibliotecas:
- **Streamlit**: Para criar a interface web da aplicação de forma simples e interativa.
- **LangChain**: Para integrar e gerenciar a interação com o modelo de linguagem (LLM).
- **Groq**: Para acessar modelos de linguagem avançados e processar as requisições de IA.
- **YouTubeTranscriptApi**: Para extrair a transcrição de vídeos do YouTube.
- **Regex (Expressões Regulares)**: Para processar e extrair informações específicas da transcrição.

### Recursos de IA:
- **LLM (Large Language Model)**: Utilizado para interpretar a transcrição e gerar receitas completas e ajustadas.
- **Prompt Engineering**: Criação de prompts especializados para garantir que a IA atue como um chef renomado.

### Outras Ferramentas:
- **Python**: Linguagem principal do projeto.
- **Git e GitHub**: Para versionamento e compartilhamento do código.

## 🧠 Fundamentos e Aprendizados

Este projeto foi uma excelente oportunidade para explorar conceitos importantes em IA e processamento de linguagem natural (NLP), além de praticar habilidades em desenvolvimento de aplicações web. Aqui estão alguns dos principais aprendizados:

### 1. Regex (Expressões Regulares)
Conheci e usei expressões regulares para extrair padrões específicos de texto, como ingredientes e modo de preparo. Foi desafiador, mas muito recompensador ver como o regex pode ser poderoso para processar dados textuais.

Hoje em dia, com tantos recursos disponíveis, é possível aprender quase qualquer coisa buscando na internet. Foi assim que me aproximei do regex e consegui aplicá-lo no projeto.

### 2. Integração com APIs
Utilizei o YouTubeTranscriptApi  para extrair transcrições de vídeos. Isso me permitiu trabalhar com dados reais e entender como integrar APIs externas em um projeto.

### 3. Prompt Engineering
A criação de prompts eficazes para a IA foi crucial para garantir que as receitas fossem extraídas e ajustadas corretamente. Aprendi como pequenos ajustes no prompt podem impactar significativamente a qualidade das respostas.

### 4. Desenvolvimento de Interfaces com Streamlit
O Streamlit foi uma ferramenta incrível para criar uma interface web de forma rápida e intuitiva. Aprendi a organizar o layout, adicionar interatividade e exibir informações de forma clara.

## ⚠️ Atenção: Problema Conhecido

Atualmente, o projeto funciona perfeitamente localmente, mas ao tentar subir para o Streamlit, o YouTube bloqueia as requisições de transcrição. Isso ocorre porque o YouTube frequentemente bloqueia IPs de provedores de nuvem (como o Streamlit) para evitar abuso de sua API.

### Contexto do Problema:
- O YouTube bloqueia requisições excessivas ou provenientes de IPs de provedores de nuvem.
- Isso é um desafio comum ao usar APIs públicas, como a youtube-transcript-api ou o YouTubeLoader.

### Solução Temporária:
- **Executar localmente**: O projeto funciona sem problemas quando executado no seu computador pessoal.

### Planos Futuros:
Estou explorando soluções para resolver esse problema, como o uso de proxies ou autenticação alternativa.

Enquanto isso, o projeto está disponível para execução local, e você pode testá-lo seguindo as instruções abaixo.

## 📂 Como Executar o Projeto Localmente

Se você quiser testar o Paola localmente, siga os passos abaixo:

### Pré-requisitos:
- Python 3.x instalado.
- Conta no Groq para acessar a API de LLM.

### Passos:
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/paola.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure a chave da API do Groq no arquivo .env:
```
GROQ_API_KEY=sua_chave_aqui
```

4. Execute a aplicação:
```bash
streamlit run main.py
```

5. Acesse a aplicação no navegador através do link fornecido pelo Streamlit.

## Sobre Mim 👋

Olá! Meu nome é [Alisson Pereira], sou estudante de Ciência de Dados no 3º semestre e um entusiasta de Inteligência Artificial. Estou em busca da minha primeira oportunidade de estágio para aplicar meus conhecimentos em projetos reais e continuar aprendendo com profissionais experientes.

## 📧 Contato

Se você gostou do projeto ou tem alguma dúvida, você pode me encontrar no:

- **LinkedIn**: [Alisson Pereira](https://www.linkedin.com/in/alisson-pereira-ds/)
- **E-mail**: alissonpereira.contato@gmail.com
- **GitHub**: [alissonpereirads](https://github.com/alissonpereirads)



---

Feito com ❤️ por [Alisson Pereira]
