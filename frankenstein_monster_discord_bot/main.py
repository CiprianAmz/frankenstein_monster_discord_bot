
from discord import Intents
from frankenstein_monster_bot import FrankensteinMonsterBot
from phi_model_wrapper import PhiModelWrapper
from config import load_config_from_json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

CONFIG_PATH = "local/local_config.json"


def main():
    config = load_config_from_json(CONFIG_PATH)
    model = PhiModelWrapper(config.model_path, config.prompt_prefix)

    intents = Intents.default()
    intents.message_content = True
    discord_bot = FrankensteinMonsterBot(
        intents=intents
    )
    discord_bot.register_model(model)

    discord_bot.run(config.access_token)


if __name__ == "__main__":
    main()
