import requests


class APIClient:

    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()

        self.session.headers.update({
            "Accept": "application/json"
        })

        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })
        


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
    def update_user(self, user_id, payload):
        return self.request(
            "PUT",
            f"/users/{user_id}",
            json=payload
        )
    def delete_user(self, user_id):
        return self.request(
            "DELETE",
            f"/users/{user_id}"
        )