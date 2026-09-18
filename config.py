import os

BASE_URLS = {
    "dev": "https://jsonplaceholder.typicode.com",
    "qa": "https://jsonplaceholder.typicode.com",
    "stg": "https://jsonplaceholder.typicode.com",
}


def get_base_url():
    environment = os.getenv("TEST_ENV", "qa")

    if environment not in BASE_URLS:
        raise ValueError(
            f"Invalid TEST_ENV: {environment}. "
            f"Expected one of: {list(BASE_URLS.keys())}"
        )

    return BASE_URLS[environment]

# config.py

BASE_URL = "https://jsonplaceholder.typicode.com"