import random
def create_booking_payload():
    return {
        "firstname": f"river{random.randint(1,100)}",
        "lastname": f"pheonix{random.randint(1,100)}",
        "totalprice": random.randint(1,1000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }