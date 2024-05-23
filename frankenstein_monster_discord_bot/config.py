import json
from typing import Optional
from dataclasses import dataclass


@dataclass
class FrankensteinBotConfig:
    access_token: str
    model_path: str
    prompt_prefix: str


def load_config_from_json(file_path: str) -> FrankensteinBotConfig:
    with open(file_path) as f:
        config_json = dict(json.load(f))
        return FrankensteinBotConfig(
            access_token=config_json["discord_access_token"],
            model_path=config_json["model_path"],
            prompt_prefix=config_json.get("prompt_prefix_instruction", ""),
        )
