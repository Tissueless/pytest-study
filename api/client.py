import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def request(self, method, endpoint, **kwargs):
        return self.session.request(
            method,
            f"{self.base_url}{endpoint}",
            **kwargs
        )
    def get_user(self, user_id):
        return self.session.get(
            f"{self.base_url}/users/{user_id}"
        )

    def create_user(self, payload):
        return self.session.post(
            f"{self.base_url}/users",
            json=payload
        )