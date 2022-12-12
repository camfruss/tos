from datetime import date, timedelta
import dotenv
from globals import GET_OPTION_CHAIN_URL, MAX_REQUESTS_PER_MIN
import os
import pandas as pd
import requests
from time import sleep

import json
"""

"""


dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
consumer_key = os.environ.get("CONSUMER_KEY")

fromDate = date.today().isoformat()
toDate = (date.today() + timedelta(days=45)).isoformat()

params = lambda x: {
    "apikey": consumer_key,
    "symbol": f"{x}",
    "contractType": "CALL",
    "strikeCount": 10,
    "includeQuotes": True,
    "fromDate": fromDate,
    "toDate": toDate,
    "optionType": "S"
}

tickers = pd.read_csv("data/tickers.csv")
tickers = tickers[(tickers["exchange"] == "NYSE") | (tickers["exchange"] == "NASDAQ")]

def option_stats(symbol):
    option_chain = []
    try:
        response = requests.get(GET_OPTION_CHAIN_URL, params=params(symbol))
        data = response.json()
    
        ticker = data["symbol"]
        underlying = data["underlying"]
        bid = float(underlying["bid"])

        for _, v in data["callExpDateMap"].items():
            for k_, v_ in v.items():
                strike = float(k_)
                option = v_[0]  # data formatted as strike: k: [{data}]
                dte = option["daysToExpiration"]
                premium = option["bid"]

                # TODO: add support for dividend stocks
                # TODO: add max pi
                position_cost = 100 * (bid - premium)
                pts_protection = premium
                percent_protection = pts_protection / bid
                break_even_price = position_cost / 100
                
                # itm vs otm
                if bid > strike:  # ITM, exercised
                    pi_if_unchanged = 100 * strike - position_cost
                else:  # OTM, not exercised
                    pi_if_unchanged = 100 * bid - position_cost
                pi_if_unchanged_percent = pi_if_unchanged / position_cost

                entry = {
                    "ticker": ticker,
                    "dte": dte,
                    "strike": strike,
                    "bid": bid,
                    "premium": premium,
                    "position_cost": position_cost,
                    "pts_protection": pts_protection,
                    "percent_protection": percent_protection,
                    "break_even_price": break_even_price,
                    "pi_if_unchanged": pi_if_unchanged,
                    "pi_if_unchanged_percent": pi_if_unchanged_percent
                }
                option_chain.append(entry)
        
    except Exception as e:
        print(symbol, e, e.with_traceback)
        pass  # Missing mal-formed data is not concerning given amt. of tickers
    finally:
        sleep(60 / MAX_REQUESTS_PER_MIN)
        return option_chain


for symbol in tickers.symbol[:600]:
    option_chain = option_stats(symbol)    
    
    if option_chain:
        directory = f"data/option_chains/{symbol[:1]}"
        if not os.path.exists(directory):
            os.makedirs(directory)

        df = pd.DataFrame(option_chain)
        df = df.round(4)
        df.to_csv(f"{directory}/{symbol}.csv", index=False)

"""

"""



"""
Symbol | DTE | Strike | Bid | Delta | Pts. Protection | % Protection | Investment Cost | Return if Exercised | Return if Exercised % | Return if Unchanged | Return if unchanged % | Break even price


Premium / 100 = Pts. of downside protection ($300 premium...if shares drop $3, will break even)
Percent downside protection = (pts. of protection = Initial stock price - break even price) / initial stock price 
investment cost = stock cost + commissions (stock + option) - premiums received
Return if exercised = stock sales - commissions + (dividends before expiry if applicable) - net investment (divide by net for % return)
Return if unchanged = stock value + dividends - net (divide by net for % return)
Break even price = (total net stock cost @ expiration = net investment - dividends) / shares held
"""


# columns = ["cusip", "symbol", "description", "exchange", "assetType"]
# df = pd.DataFrame(tickers, columns=columns)
# df.to_csv("data/tickers.csv", index=False, header=True)