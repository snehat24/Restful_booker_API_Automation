def header():
    return {
        "Content-Type": "application/json"
    }

def auth(auth_token):
    return {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }
