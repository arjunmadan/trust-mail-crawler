from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

organization = "mozilla"
BASE_URL = "http://" + organization + ".markmail.org/search/?page="
count    = 0
msgCount = 0
pageNo   = 1

def getMessageCount(organization):
	html = urlopen("http://" + organization + ".markmail.org/").read()
	soup = BeautifulSoup(html, "lxml")
	msgCount = soup.findAll("strong")[1:2]
	msgCount = re.sub("[^0-9]", "", str(msgCount))
	return int(msgCount)
	
def getEmailUrls():
	IdList = []
	global pageNo
	global BASE_URL
	html = urlopen(BASE_URL + str(pageNo)).read()
	soup = BeautifulSoup(html, "lxml")
	for tag in soup.findAll("div", "result"):
		IdList.append(tag['id'])
	pageNo = pageNo + 1
	getEmailContent(IdList)

def getEmailContent(IdList):
	msgBody = []
	subject = []
	email   = []
	date    = []
	to      = []
	
	while len(IdList) > 0:
		msgId = IdList.pop();
		html = urlopen("http://markmail.org/message/" + msgId).read()
		soup = BeautifulSoup(html, "lxml")
		
		msgBody.append(soup.find("div", "messagebody").text)
		
		for tag in soup.find("a", "subject"):
			subject.append(tag.string)
		
		for tag in soup.findAll("th"):
			if tag.text == "From:":
				email.append(tag.find_next_sibling("td").text)
			elif tag.text == "Date:":
				date.append(tag.find_next_sibling("td").text)
			elif tag.text == "List:":
				to.append(tag.find_next_sibling("td").text)
	'''
	for i in range (0, 10):
		print "From:" + email[i]
		print "To:" + to[i]
		print "Subject: " + subject[i]
		print "Date: " + date[i]
	'''		
msgCount = getMessageCount(organization)

for i in range(0, msgCount / 10):
	getEmailUrls()


