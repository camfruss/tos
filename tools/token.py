import dotenv
from getpass import getpass
from globals import ACCESS_TOKEN_URL
import os
import requests
from urllib.parse import quote, unquote, urlparse


username = input("Your TDA username")
password = getpass("Your TDA password")

# implement steps on https://developer.tdameritrade.com/content/simple-auth-local-apps
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

redirect_uri = os.environ.get("REDIRECT_URI")
redirect_uri_encoded = quote(redirect_uri, safe="")

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_key_encoded = quote(consumer_key, safe="")

AUTH_URL_QUERY =  \
    ("https://auth.tdameritrade.com/auth?response_type=code"
     f"&redirect_uri={redirect_uri_encoded}"
     f"&client_id={consumer_key_encoded}%40AMER.OAUTHAP")

response = requests.get(AUTH_URL_QUERY)

# TODO: need selenium to log into TDA using above credentials

parsed_url = urlparse.urlparse(response.url)
code = urlparse.parse_qs(parsed_url.query)["code"][0]
decoded_code = unquote(code)

# TODO: make 
params = {
    "grant_type": "authorization_code",
    "access_type": "offline",
    "code": decoded_code,
    "client_id": consumer_key + "@AMER.OAUTHAP",
    "redirect_uri": redirect_uri
}
response = requests.get(ACCESS_TOKEN_URL, params=params)

{
  "access_token": "string",
  "refresh_token": "string",
  "token_type": "string",
  "expires_in": 0,
  "scope": "string",
  "refresh_token_expires_in": 0
}

# SAVE ACCESS_TOKEN to .env, 
# Save refresh token to env
