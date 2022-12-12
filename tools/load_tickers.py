import dotenv
from functools import reduce
from globals import SEARCH_INSTRUMENTS_URL
from operator import concat
import os
import pandas as pd
import requests
import string

"""
Query for all listed tickers on TDA
"""

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
consumer_key = os.environ.get("CONSUMER_KEY")

params = lambda x: {
    "apikey": consumer_key,
    "symbol": f"{x}.*",
    "projection": "symbol-regex"
}

tickers = []
for i in string.ascii_uppercase:
    response = requests.get(SEARCH_INSTRUMENTS_URL, params=params(i))
    data = response.json()
    data_ = list(data.values())
    tickers.append(data_)

flat_tickers = reduce(concat, tickers)

columns = ["cusip", "symbol", "description", "exchange", "assetType"]
df = pd.DataFrame(flat_tickers, columns=columns)
df.to_csv("data/tickers.csv", index=False, header=True)
