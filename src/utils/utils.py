from datetime import datetime
import json
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)

c_handler = logging.StreamHandler()
#f_handler = logging.FileHandler('../../logs/discord.log')
c_handler.setLevel(logging.INFO)
#f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
#f_format = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
c_handler.setFormatter(c_format)
#f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
#logger.addHandler(f_handler)

def get_time():
    return datetime.now().strftime("%Y-%m-%D %H:%M:%S")

# Read the guild/server name or id and then get the k, v's from the array in the settings.json file
def modify_settings(key, val):
    with open('../settings.json', 'r+') as settings_f:
        settings = json.load(settings_f)
        settings[key] = val
        settings_f.seek(0)
        json.dump(settings, settings_f, indent=4)
        settings_f.truncate()

    settings_f.close()

def load_settings():
    with open('../settings.json', 'r+') as settings_f:
        settings = json.load(settings_f)

    settings_f.close()
    return settings