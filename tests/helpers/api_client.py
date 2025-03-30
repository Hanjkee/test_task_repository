import requests
import logging

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = logging.getLogger("api")

    def get_comments(self, post_id):
        url = f"{self.base_url}/posts/{post_id}/comments"
        self.logger.info(f"GET {url}")
        return requests.get(url)

    def create_comment(self, post_id, data):
        url = f"{self.base_url}/posts/{post_id}/comments"
        self.logger.info(f"POST {url} - {data}")
        return requests.post(url, json=data)