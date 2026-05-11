import json

from utils.headers import header
from config import BASE_URL
from payloads import auth_payload
from utils.logger import get_logger


def test_token(api_request_context):
 logger = get_logger()
 payload=auth_payload()
 response = api_request_context.post(f"{BASE_URL}/auth"
                                     , headers=header(),
                                     data=json.dumps(payload))
 logger.info("validating status code")
 assert response.status == 200
 logger.info(f"status code: {response.status}")
 token=response.json()["token"]
 logger.info("created token")