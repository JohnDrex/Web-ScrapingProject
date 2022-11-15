from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'
#Line 18 - 28 should remain the same for all codes so you can coppy paste that, just will need to change URL
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)

tablecells = soup.findAll("div", attrs={"class":"table-cell"})

range1 = [0,1,2,3,4]
count = 0

for x in range1:
    print(tablecells[0+count].text)
    print("Company Name:      " + tablecells[1+count].text) #Company Name is 1
    print("Percentage Change: " + tablecells[3+count].text) #Change is 3
    print("Todays High:       "+tablecells[5+count].text) #High is 5
    print("Todays Low:        "+tablecells[6+count].text) #Low is 6
    print("Price difference: ", float(tablecells[5+count].text) - float(tablecells[6+count].text))
    count = count+11












#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

