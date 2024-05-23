#!/usr/bin/bash
python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
python3 frankenstein_monster_discord_bot/main.py
deactivate
