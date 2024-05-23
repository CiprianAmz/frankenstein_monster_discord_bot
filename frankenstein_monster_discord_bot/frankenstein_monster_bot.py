import logging
from discord import Client
from phi_model_wrapper import PhiModelWrapper


class FrankensteinMonsterBot(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._model = None

    def register_model(self, model: PhiModelWrapper):
        self._model = model

    async def on_ready(self):
        logging.info("Frankenstein Monster is awake...")

    async def on_message(self, message):
        logging.info("Receiving message...")

        # We do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!chat"):
            reply_message = "Aghhh"

            if self._model:
                reply_message = self._model.reply(
                    message.content[len("!chat"):])

            await message.reply(reply_message, mention_author=True)
