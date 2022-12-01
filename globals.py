import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
account_id = os.environ.get("ACCOUNT_ID")

POST_ACCESS_TOKEN_URL = "https://api.tdameritrade.com/v1/oauth2/token"
GET_ACCOUNT_URL = f"https://api.tdameritrade.com/v1/accounts/{account_id}"

ACCESS_TOKEN_EXPIRY = 1800
REFRESH_TOKEN_EXPIRY = 7776000
