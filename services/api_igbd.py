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

def get_headers():
    load_dotenv()
    client_id = os.getenv("TWITCH_CLIENT_ID")
    token = get_auth_token()
    header = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    return header

def get_videogame(name : str):
    headers = get_headers()
    url = f"{base_url}/games"
    payload = f"fields name, genres; search \"{name}\"; where version_parent = null;"
    response = requests.post(url, headers=headers, data=payload)
    response.raise_for_status()
    return response.json()[0]




