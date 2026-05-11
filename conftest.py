import json

import pytest
from playwright.sync_api import sync_playwright

from payloads.auth_payload import auth_payload
from payloads.booking_payload import create_booking_payload
from utils.headers import header


@pytest.fixture
def api_request_context():
    print("MY FIXTURE USED")
    with sync_playwright() as p:
        request_context = p.request.new_context()
        yield request_context
        request_context.dispose()

@pytest.fixture
def auth_token(api_request_context):
    response = api_request_context.post(
        "https://restful-booker.herokuapp.com/auth",
        headers=header(),
        data=json.dumps(auth_payload())
    )
    return response.json()["token"]

@pytest.fixture
def bookingid(api_request_context, auth_token):
    payload = create_booking_payload()
    response = api_request_context.post(
        "https://restful-booker.herokuapp.com/booking",
        headers=header(),
        data=json.dumps(payload)
    )
    return response.json()["bookingid"]