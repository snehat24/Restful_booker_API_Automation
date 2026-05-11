import json

from config import BASE_URL
from payloads.booking_payload import create_booking_payload
from utils.headers import header
from utils.logger import get_logger


def test_post_method(api_request_context):
    logger= get_logger()
    payload =create_booking_payload()
    response = api_request_context.post(f"{BASE_URL}/booking",
                                        data=json.dumps(payload),headers=header())
    assert response.status == 200
    logger.info(f"booking id: {response.json()['bookingid']}")
    logger.info(f"status code: {response.status}")
    logger.info(f"headers: {response.headers}")