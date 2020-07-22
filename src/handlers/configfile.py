import yaml
from os import environ


try:
    HOME_CONFIG = f"{environ['HOME']}/.config/mangawind.yml"
    with open(HOME_CONFIG, 'r') as file:
        conf = yaml.safe_load(file)
except FileNotFoundError:
    try:
        with open('/etc/mangawind.yml', 'r') as file:
            conf = yaml.safe_load(file)
    except FileNotFoundError:
        try:
            with open('config.yml', 'r') as file:
                conf = yaml.safe_load(file)
        except FileNotFoundError:
            print("No configuration file was found")