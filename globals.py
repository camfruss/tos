import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
account_id = os.environ.get("ACCOUNT_ID")

POST_ACCESS_TOKEN_URL = "https://api.tdameritrade.com/v1/oauth2/token"
GET_ACCOUNT_URL = f"https://api.tdameritrade.com/v1/accounts/{account_id}"
SEARCH_INSTRUMENTS_URL = "https://api.tdameritrade.com/v1/instruments"
GET_OPTION_CHAIN_URL = "https://api.tdameritrade.com/v1/marketdata/chains"

OPTION_COMISSION = 0.65  # per contract, ignored since small

MAX_REQUESTS_PER_MIN = 120

ACCESS_TOKEN_EXPIRY = 1800
REFRESH_TOKEN_EXPIRY = 7776000
