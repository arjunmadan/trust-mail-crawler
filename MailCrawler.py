from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

organization = "mozilla"
BASE_URL = "http://" + organization + ".markmail.org/search/?page="
count    = 0
msgCount = 0
IdList   = []
pageNo   = 1

def getMessageCount(organization):
	html = urlopen("http://" + organization + ".markmail.org/").read()
	soup = BeautifulSoup(html, "lxml")
	msgCount = soup.findAll("strong")[1:2]
	msgCount = re.sub("[^0-9]", "", str(msgCount))
	return int(msgCount)
	
def getEmailUrls():
	global IdList
	global pageNo



msgCount = getMessageCount(organization)
pageNo = getEmailUrls()
print msgCount

