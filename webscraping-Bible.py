import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://ebible.org/asv/JHN'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)


random_chapter = random.randint(1,21)
if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)




url = webpage+str(random_chapter)+'.htm'
print(url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

#paragraph = soup.findAll("div", attrs={"class":"p"})
paragraph = soup.findAll("div", class_='main')

#print(paragraph)


for verse in paragraph:
    verse_list = (verse.text.split('.'))

#print(verse_list)

myverse = random.choice(verse_list[:len(verse_list)-5])

message = (f"Chapter: {random_chapter} , Verse: {myverse}")

#message = "Chapter:"+random_chapter + " Verse: "+ myverse

print(message)

import keys
from twilio.rest import Client
client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+16293484622"

myCellPhone = "+18325896060"
textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = message)

print(textmessage.status)