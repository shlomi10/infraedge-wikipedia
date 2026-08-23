from playwright.sync_api import APIRequestContext

from utils.logger import get_logger


class ApiClient:
    SUCCESS_STATUSES = (200, 201, 204)

    def __init__(self, request: APIRequestContext):
        self.request = request
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str, params: dict | None = None):
        self.logger.info(f"GET {endpoint} params={params}")
        response = self.request.get(endpoint, params=params)
        self.validate(response)
        return response.json()

    def post(self, endpoint: str, data: dict | None = None):
        self.logger.info(f"POST {endpoint}")
        response = self.request.post(endpoint, data=data)
        self.validate(response)
        return response.json() if response.text() else None

    def patch(self, endpoint: str, data: dict):
        self.logger.info(f"PATCH {endpoint}")
        response = self.request.patch(endpoint, data=data)
        self.validate(response)
        return response.json() if response.text() else None

    def validate(self, response):
        if response.status not in self.SUCCESS_STATUSES:
            self.logger.error(f"API failed: {response.status} {response.text()}")
            raise AssertionError(f"API failed: {response.status} {response.text()}")
