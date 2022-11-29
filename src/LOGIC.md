# LOGIC

AVOID dividend stocks

Overview: Covered call writing -> sell a call option (& collect premium) while owning obligated num of shares of underlying stock

Sentiment: neutral or mildly bullish

Cons: limits potential profit during strong upwards moves

Premium / 100 = Pts. of downside protection ($300 premium...if shares drop $3, will break even)
Percent protection = stock price - pts / stock price

Have flag that either: rolls options forward or allows shares to be called away (keep track of taxes, put remainder of money into buying more stock)

- need to find stocks that have best potential return 0DTE options 
- flag for margin trading (remember 25k minimum for pattern day trading)


out-of-the-money covered write vs in-the-money covered write

out-of-money has greater potential profit than in-the-money

π = Profit

share list to compare different strike prices at expiration and total profit:
XYZ $44
EXPR | π, 40  | π, 50
35 -200 -900
37 0 -400
40 300 0
45 300 100
50 300 600
60 300 600

Need to calculate total investment cost = stock cost + commissions (stock + option) - premiums received
Return if exercised = stock sales - commissions + (dividends before expiry if applicable) - net investment (divide by net for % return)
Return if unchanged = stock value + dividends - net (divide by net for % return)
Break even price = (total net stock cost @ expiration = net investment - dividends) / shares held
Percent downside protection = (pts. of protection = Initial stock price - break even price) / initial stock price 


Margin (pg 45 - 46)
net margin investment
return if exercised
return if unchanged
break even point on margin
margin downside protection (pg 47) - there is less overall downside protection with margin because of interest payments

margin interest rates = debit((1+interest rate/12)^(mo. to expr.) - 1)

should produce graphs for all this data -> return for each price pt.


net covered writing order = price - premium = "net"
must be etered through a spread order entry / contigent order
net orders are "not held" . meaning they are not guaranteed to be executed

a return if unchanged should be no less than 1%/month

comparing volitile vs non-volitikle stocks = pg 465

downside protetion of 10% is good standard

If stock decreases in price:
rolling action - buying back the call and selling another one at a different strike/expiry
rolling down - selling at a lower strike
rolling down gives protection against further drop in stock price and produces additional income if price stabilizes
find price where rolling down profit = original write

If cross, then do partial roll down (ceil(1/2 of shares)*100, need even num)
Need to determine when to roll down....(after what % decline -> roll down after distance b/t rolled-down profit and current profit is 1/2 max )



If stock increases in price:
if stock comes close to parity, then roll up
downside break even pt. is increased by the debit required to roll up
when rolliong up, a debit is incurred (it required new funds)


if call is trading below parity, will be exercised
time value premium on option = call price + strike price - stock price 