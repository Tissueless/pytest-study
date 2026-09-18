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
        response = self.session.request(
            method,
            f"{self.base_url}{endpoint}",
            **kwargs
        )
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError(
                f"{method} {endpoint} failed with status {response.status_code}"
    )
        return response

    def get_user(self, user_id):
        return self.request(
            "GET",
            f"/users/{user_id}",
        )

    def create_user(self, payload):
        return self.request(
            "POST",
            "/users",
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