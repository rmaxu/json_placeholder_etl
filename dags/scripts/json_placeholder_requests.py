import requests
import sys

def create_get_request(url: str, params=None):
    try:
        if params:
            response = requests.get(url, params=params)
        else:
            response = requests.get(url)
        return response.json()
    except requests.exceptions.Timeout:
        print("WARNING: request timed out")
        return None
    except requests.exceptions.RequestException as ex:
        sys.exit(f"Something went wrong with the Request: {repr(ex)}")
    except Exception as ex:
        sys.exit(f"Something went wrong around the Request: {repr(ex)}")


class JsonPlaceholder:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
    
    def get_posts(self):
        url = self.base_url + "/posts"
        return create_get_request(url)
    
    def get_post_by_id(self, id: int):
        url = f"{self.base_url}/posts/{id}"
        return create_get_request(url)

    def get_post_comments(self, id: int):
        url = f"{self.base_url}/comments"
        params = {
            'postId': str(id),
        }
        return create_get_request(url, params=params)

    def get_comments(self):
        url = f"{self.base_url}/comments"
        return create_get_request(url)

    def get_users(self):
        url = f"{self.base_url}/users"
        return create_get_request(url)

    def get_photos(self):
        url = f"{self.base_url}/photos"
        return create_get_request(url)

    def get_todos(self):
        url = f"{self.base_url}/photos"
        return create_get_request(url)