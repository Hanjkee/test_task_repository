import requests
import logging

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = logging.getLogger("api")
        
    def _log_request(self, method, url, **kwargs):
        self.logger.info(f"Request: {method} {url}")
        if kwargs.get("json"):
            self.logger.debug(f"Request data: {kwargs['json']}")
            
    def _log_response(self, response):
        self.logger.info(f"Response: {response.status_code}")
        self.logger.debug(f"Response data: {response.text}")

    def get_comments(self, post_id):
        url = f"{self.base_url}/posts/{post_id}/comments"
        self._log_request("GET", url)
        response = requests.get(url)
        self._log_response(response)
        return response
        
    def create_comment(self, post_id, data):
        url = f"{self.base_url}/posts/{post_id}/comments"
        self._log_request("POST", url, json=data)
        response = requests.post(
            url,
            json=data,
            headers={"Content-type": "application/json; charset=UTF-8"}
        )
        self._log_response(response)
        return response