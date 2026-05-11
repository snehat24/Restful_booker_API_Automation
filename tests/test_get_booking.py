from packaging import markers

from config import BASE_URL
from utils.logger import get_logger

def test_get_method(api_request_context,bookingid):
 logger=get_logger()
 response=api_request_context.get(f"{BASE_URL}/booking/{bookingid}")
 logger.info("validating status code for get")
 assert response.status == 200
 assert 'application/json' in response.headers['content-type']
 logger.info(f"status code: {response.status}")
 assert "firstname" in response.json()
 assert "lastname" in response.json()
 assert "bookingdates" in response.json()
 logger.info("validated firstname,lastname,bookingdates")
 logger.info(f"Body: {response.json()}")
 logger.info("Headers:"+str(response.headers))