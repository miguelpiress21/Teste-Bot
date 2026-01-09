import os
from bot_multimodal import BotMultimodal

TOKEN = os.getenv("Coloque aqui o token")

bot = BotMultimodal(TOKEN)

bot.run()

