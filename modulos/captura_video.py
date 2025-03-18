import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled


def validar_url_youtube(url: str) -> bool:
    """Valida se o URL fornecido é um link válido do YouTube."""
    padrao_youtube = re.compile(r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+")
    return bool(padrao_youtube.match(url))


def extrair_transcricao(video_url: str) -> str:
    """Extrai a transcrição do vídeo do YouTube, se disponível."""
    if not validar_url_youtube(video_url):
        return "Erro: URL do YouTube inválido."

    try:
        video_id = video_url.split("v=")[-1].split("&")[0]  # Extrai o ID do vídeo
        transcricao = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["pt", "en"]
        )
        texto = " ".join([item["text"] for item in transcricao])
        return texto
    except TranscriptsDisabled:
        return "Erro: Este vídeo não possui legendas automáticas disponíveis."
    except Exception as e:
        return f"Erro ao obter transcrição: {str(e)}"
