import requests
import os
from dotenv import load_dotenv

base_url = 'https://api.igdb.com/v4'

# Connection à l'Oauth2
def get_auth_response():
    load_dotenv()
    client_id = os.getenv("TWITCH_CLIENT_ID")
    client_secret = os.getenv("TWITCH_CLIENT_SECRET")
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    return requests.post(url, data=payload)

def get_auth_token() -> str:
    response = get_auth_response()
    response.raise_for_status()  # Raise an error for bad responses
    token = response.json().get("access_token")
    return token






