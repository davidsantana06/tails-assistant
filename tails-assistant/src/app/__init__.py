from os import path
from speech_recognition import Recognizer
import colorama
import json

from .actuators import UserGames, ArchiveGames
from .constants import DATABASE_DIR
from .token import retrieve_stop_words


def init_app():
    colorama.init(autoreset=True)

    with open(f'{DATABASE_DIR}/tails_features.json', 'r', encoding='utf-8') as features_file:
        features: dict[str, object] = json.load(features_file)
        ai_name: str = features.get('name')
        ai_actions: list[dict[str, object]] = features.get('actions')

    actuators = (ArchiveGames(), UserGames())
    recognizer = Recognizer()
    stop_words = retrieve_stop_words()

    return (ai_name, ai_actions, actuators, recognizer, stop_words)
