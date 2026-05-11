from config import BASE_URL
from utils.logger import get_logger


def test_get_method(api_request_context):
 logger=get_logger()
 response=api_request_context.get(f"{BASE_URL}/booking/78675")
 logger.imfo("validating status code ")
 assert response.status == 404
 logger.info("status code:"+str(response.status))
 assert response.text() == "Not Found"
 logger.info("Text:"+str(response.text()))