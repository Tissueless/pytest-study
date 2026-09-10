import os

ENVIRONMENT = os.getenv("TEST_ENV", "qa")

BASE_URLS = {
    "dev": "https://jsonplaceholder.typicode.com",
    "qa": "https://jsonplaceholder.typicode.com",
    "stg": "https://jsonplaceholder.typicode.com",
}


def get_base_url():
    return BASE_URLS[ENVIRONMENT]