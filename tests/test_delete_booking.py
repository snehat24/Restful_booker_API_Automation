import json

from config import BASE_URL
from conftest import bookingid
from utils.headers import auth
from utils.logger import get_logger


def test_delete(api_request_context,auth_token,bookingid):
 logger=get_logger()
 response = api_request_context.delete(f"{BASE_URL}/booking/{bookingid}"
        ,headers=auth(auth_token))
 logger.info("validating status code for delete")
 assert response.status == 201
 logger.info(f"status code: {response.status}")
 res=api_request_context.get(f"{BASE_URL}/booking/{bookingid}")
 logger.info("validating if booking s deleted or not")
 assert res.status == 404
 logger.info(f"status code: {res.status}")