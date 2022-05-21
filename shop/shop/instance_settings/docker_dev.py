import environ

from shop.instance_settings.base import *  # noqa: F403,W0614

if not "env" not in locals():
    env = environ.Env()

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DATABASE_NAME", default="db_name"),
        "USER": env("DATABASE_USER", default="db_user"),
        "PASSWORD": env("DATABASE_PASSWORD", default="password"),
        "HOST": "db",
        "PORT": 3306,
    }
}
