import streamlit as st
from modulos.captura_video import extrair_transcricao
from modulos.extrai_receita import extrair_receita
from modulos.ajusta_receita import ajustar_receita

st.title("Paola - Extrator de Receitas do YouTube 🍽️")

# Input do link do vídeo no topo
video_url = st.text_input("Cole aqui o link do vídeo do YouTube")

if video_url:
    # Exibe o vídeo
    st.video(video_url)

    if st.button("📥 Extrair e Ajustar Receita"):
        with st.spinner("⏳ Processando..."):  # Spinner para indicar processamento
            # Extrai a transcrição do vídeo
            transcricao = extrair_transcricao(video_url)

            if "Erro" in transcricao:
                st.error(transcricao)
            else:
                # Extrai a receita da transcrição
                receita = extrair_receita(transcricao)

                # Ajusta a receita com a IA
                receita_ajustada = ajustar_receita(receita)

                # Verifica se ocorreu um erro durante o ajuste da receita
                if "erro" in receita_ajustada:
                    st.error(receita_ajustada["erro"])
                elif "mensagem" in receita_ajustada:
                    # Se o vídeo não for de receita, exibe a mensagem engraçada
                    st.warning(receita_ajustada["mensagem"])
                else:
                    # Exibe a receita ajustada em seções destacadas com Markdown
                    st.markdown("## 📝 **Receita Extraída**")
                    st.markdown("---")

                    # Seção de Ingredientes
                    if "ingredientes_ajustados" in receita_ajustada:
                        st.markdown("### 🛒 **Ingredientes:**")
                        st.write(receita_ajustada["ingredientes_ajustados"])
                        st.markdown("---")
                    else:
                        st.warning("⚠️ Ingredientes não puderam ser extraídos.")

                    # Seção de Modo de Preparo
                    if "modo_de_preparo_ajustado" in receita_ajustada:
                        st.markdown("### 🍳 **Modo de Preparo:**")
                        st.write(receita_ajustada["modo_de_preparo_ajustado"])
                        st.markdown("---")

                    else:
                        st.warning("⚠️ Modo de preparo não pôde ser extraído.")

                    # Seção de Tempo de Preparo e Porções
                    if "tempo_de_preparo" in receita_ajustada:
                        st.markdown("### ⏱️ **Tempo de Preparo:**")
                        st.write(receita_ajustada["tempo_de_preparo"])
                    else:
                        st.warning("⚠️ Tempo de preparo não pôde ser extraído.")

                    if "quantidade_porcoes" in receita_ajustada:
                        st.markdown("### 🍽️ **Quantidade de Porções:**")
                        st.write(receita_ajustada["quantidade_porcoes"])
                    else:
                        st.warning("⚠️ Quantidade de porções não pôde ser extraída.")

                    # Seção de Dicas do Chef

                    if "dicas_do_chef" in receita_ajustada:
                        st.markdown("## 👨‍🍳 **Dicas do Chef**")
                        st.write(receita_ajustada["dicas_do_chef"])
                    else:
                        st.warning("⚠️ Dicas do chef não puderam ser extraídas.")
