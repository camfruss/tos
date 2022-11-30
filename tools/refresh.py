import dotenv
from globals import ACCESS_TOKEN_URL
import os
import requests


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

refresh_token = os.environ.get("REFRESH_TOKEN")
consumer_key = os.environ.get("CONSUMER_KEY")

params = {
    "grant_type": "refresh_token",
    "refresh_token": refresh_token,
    "client_id": consumer_key + "@AMER.OAUTHAP"
}

response = requests.get(ACCESS_TOKEN_URL, params=params)

# TODO: print response to see if refresh token is new (don't think it is)
# TODO: update new ACCESS TOKEN
