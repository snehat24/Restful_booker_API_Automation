import json

from config import BASE_URL
from utils.headers import auth
from utils.logger import get_logger


def test_update(api_request_context,auth_token,bookingid):
 logger=get_logger()
 payload={"firstname" : "jim","lastname" : "brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
 response = api_request_context.put(f"{BASE_URL}/booking/{bookingid}"
       , headers=auth(auth_token),
                                      data=json.dumps(payload))
 assert response.status == 200
 logger.info("validating status code:"+str(response.status))
 assert "firstname" in response.json().keys()
 logger.info("validated firstname too"+str(response.json()["firstname"]))