import os

from dotenv import load_dotenv

load_dotenv()

TORTOISE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.postgres',
            'credentials': {
                'user': 'postgres',
                'password': '123',
                'host': 'localhost',
                'port': '5432',
                'database': 'new',
            }
        }
    }
}


TORTOISE_ORM = {
    "connections": {
        "default": TORTOISE_URL
    },
    "apps": {
        "models": {

            "models": ["app.models"],
            "default_connection": "default"
        },
        }
    }
