import json

from config import BASE_URL
from utils.headers import auth
from utils.logger import get_logger


def test_partail_update(api_request_context,auth_token,bookingid):
 logger=get_logger()
 payload={"additionalneeds" : "Lunch"}
 response = api_request_context.patch(f"{BASE_URL}/booking/{bookingid}"
        ,headers=auth(auth_token),
                    data=json.dumps(payload))
 assert response.status == 200
 logger.info("status code:"+str(response.status))
 assert response.json()["additionalneeds"] == "Lunch"
 logger.info("validated additionalneeds")
