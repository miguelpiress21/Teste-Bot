from bot_audio import BotAudio
from bot_imagem import BotImagem

class BotMultimodal(BotAudio, BotImagem):
    """
    Bot multimodal que processa imagens e áudios
    """
    def __init__(self, token: str):
        BotAudio.__init__(self, token)
        BotImagem.__init__(self, token)