import socket
import os


def load_settings():
    name = socket.gethostname()
    BASE_DIR = os.path.dirname(__file__)
    filename = "{}/instance_settings/{}.py".format(BASE_DIR, name)
    try:
        setting_file = open(filename)
    except FileNotFoundError:
        setting_file = open(filename, "w")
        setting_file.write("from shop.instance_settings.development import *")
    setting_file.close()

    return "shop.instance_settings.{}".format(name)
