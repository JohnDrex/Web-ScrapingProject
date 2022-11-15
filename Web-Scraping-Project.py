from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = 'https://crypto.com/price'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

tablename = soup.findAll("div", class_='css-0')

btc = (tablename[10].text)
bitcoin= btc.split('$')
bitcoin1 = bitcoin[1]
if ',' in bitcoin1:
    bitcoin2 = bitcoin1.split(',') 
    bitcoin_price = float(bitcoin2[0]+bitcoin2[1])
else:
    bitcoin_price = float(bitcoin[1])

etm = (tablename[11].text)
ethereum= etm.split('$')
ethereum1 = ethereum[1]
if ',' in ethereum1:
    ethereum2 = ethereum1.split(',') 
    ethereum_price = float(ethereum2[0]+ethereum2[1])
else:
    ethereum_price = float(ethereum[1])

import keys
from twilio.rest import Client
client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+1"

myCellPhone = "+1"
message = ()

if bitcoin_price < 40000:
    message = ("The value of Bitcoin is below $40,000! Its current price is " + btc + "!")
    textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = message)
    print(textmessage.status)
    
    
if ethereum_price < 3000:
    message = ("The value of Ethereum is below $3,000! Its current price is " + etm + "!")
    textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = message)
    print(textmessage.status)

rangerank = [0,1,2,3,4]
rangerank2 = [0,1,2,3]
mname = soup.findAll("div", class_='css-16q9pr7')
tname = soup.findAll("div", class_='css-ttxvk0')
print()
print()
print("===================================================")
print("The Top 5 Crypto Currencies According to Crypto.Com")
print("===================================================")
print()
print()

for x in rangerank:
    print("Please press enter to view next stock:")
    Z = input()

    name = (tname[x].text)
    rank = x+1

    splitneed = mname[x].text # price and percentage of 1
    splitneed = str(splitneed)


    if '-' in splitneed:
        pctlist = splitneed.split('-')
        pct = ("-" + pctlist[1])
        usepct = pct.split('%')
        usepct1 = usepct[0]
        usepct2 = usepct1.split('-')
        usepct3 = float(usepct2[1])
        currentprice = (pctlist[0])
        useprice = currentprice.split('$')
        useprice1 = useprice[1]
        if ',' in useprice1:
            comsplit = useprice1.split(',') 
            price1 = float(comsplit[0]+comsplit[1])
        else:
            price1 = float(useprice[1])
        oldprice = (price1) * (1-((usepct3)/100))
    else:
        pctlist = splitneed.split('+')
        pct = ("+" + pctlist[1])
        usepct = pct.split('%')
        usepct1 = usepct[0]
        usepct2 = usepct1.split('+')
        usepct3 = float(usepct2[1])
        currentprice = (pctlist[0])
        useprice = currentprice.split('$')
        useprice1 = useprice[1]
        if ',' in useprice1:
            comsplit = useprice1.split(',') 
            price1 = float(comsplit[0]+comsplit[1])
        else:
            price1 = float(useprice[1])
        oldprice = (price1) * (1+((usepct3)/100))

    oldcost = "${:,.2f}".format(oldprice)
    print("===============================")
    print("Stock Rank: ", rank, "\n", "  Name           :", name, "\n", "  Current Price  :", currentprice, "\n", "  24hr % Change  :", pct, "\n", "  Price 24hrs Ago:", oldcost)
    print("===============================")
