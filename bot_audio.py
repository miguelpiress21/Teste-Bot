import os
import speech_recognition as sr
from telegram.ext import MessageHandler, filters
from bot_base import BotTelegram

class BotAudio(BotTelegram):
    def __init__(self, token):
        super().__init__(token
        self.recognizer = sr.Recognizer()

        self.app.add_handler(
            MessageHandler(filters.VOICE, self.processar_audio)
        )

    async def processar_audio(self, update, context):
        voice = update.message.voice
        file = await voice.get_file()
        caminho = "temp_audio.wav"

        await file.download_to_drive(caminho)

        with sr.AudioFile(caminho) as source:
            audio = self.recognizer.record(source)

        try:
            texto = self.recognizer.recognize_google(
                audio, language="pt-BR"
            )
            await update.message.reply_text(
                f"🎧 Texto reconhecido:\n{texto}"
            )
        except:
            await update.message.reply_text(
                "❌ Não foi possível reconhecer o áudio."
            )


        os.remove(caminho)
