import os
import socket
from pathlib import Path


def load_settings():
    name = socket.gethostname()
    BASE_DIR = os.path.dirname(__file__)
    filename = "{}/instance_settings/{}.py".format(BASE_DIR, name)
    path = Path(filename)
    if not path.is_file():
        # TODO - add posibility to disable automatic generation of settings file
        with open(filename, "w") as settings_file:
            # TODO - load proper settings depending if in docker or not
            settings_file.write("from shop.instance_settings.docker_dev import *  # noqa F403, W0614 W0401")

    return "shop.instance_settings.{}".format(name)
