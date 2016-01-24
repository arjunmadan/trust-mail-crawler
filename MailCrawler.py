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
	while len(IdList) > 0:
		msgId = IdList.pop();
		html = urlopen("http://markmail.org/message/" + msgId).read()
		soup = BeautifulSoup(html, "lxml")
		#Message Content
		msgBody.append(soup.find("div", "messagebody").text)
		#Subject
		for tag in soup.find("a", "subject"):
			subject.append(tag.string)
		#for tag in soup.findAll("td", "from"):
		#	print tag	
				#$("table#headers").children().children().each(function(i, element){
				#	var a = $(this);
				#	switch($(this).children('th').text()) {
				#		case 'From:':
				#			console.log("From: " + $(this).children('td').text());
				#			break;
				#		case 'Date:':
				#			console.log("Date: " + $(this).children('td').text());
				#			break;
				#		case 'List:':
				#			console.log("List: " + $(this).children('td').text());
				#			break;
				#		default:
				#			break;
				
				#console.log($("div.messagebody").text());
			
msgCount = getMessageCount(organization)

for i in range(0, 1):
	getEmailUrls()


