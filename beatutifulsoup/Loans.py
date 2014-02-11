import urllib2
from bs4 import BeautifulSoup
from decimal import *


# Stores information about an account and all of its variables
class Account(object):
	name = ""
	interests = []

	def __init__(self, name, interests):
		self.name = name
		self.interests = interests

# Stores the different variables within an account
# interest_rate is stored as decimal.Decimal
class Interest(object):
	description = ""
	interest_rate = 0 

	def __init__(self, description, interest_rate):
		self.description = description
		self.interest_rate = interest_rate


# fetch the information online from landsbankinn
def getNewestData():
	file = open("Data/vextir.txt", "w");
	soup = BeautifulSoup(urllib2.urlopen("http://www.landsbankinn.is/Vextir").read())
	file.write(soup.encode("utf-8"))
	file.close

	return soup

# cached information stored in vextir.txt
def getCachedData():
	file = open("Data/vextir.txt", "r")
	str = file.read()
	soup = BeautifulSoup(str)
	file.close()

	return soup

# Check if an item is the name of an account or not
def isParent(item):
	if( item.find('strong') ):
		return True
	return False

# Car loans need a special treatment, because they split into two parts
def handleCarOutLoans(loans):
	loans[7].name = loans[6].name + " - " + loans[7].name
	loans[8].name = loans[6].name + " - " + loans[8].name

	#removes an unneccesary item
	loans.pop(6)

	return loans

#
#	In Loans
#	newest == True for newest possible data, newest == False for cached data
#	Returns list of Account objects that contain in loans 	
#
def getInLoans(newest):

	if( newest ):
		soup = getNewestData()
	else:
		soup = getCachedData()

	table = soup.find(id="interesttable")
	tr = table.find_all('tr')

	inLoans = []
	j = -1
	for item in tr:
		if( isParent(item) ):
			account = Account(item.strong.text, [])
			inLoans.append(account)
			j += 1
		elif( item['class'] ):
			description = item.contents[1].text.strip()
			interest_rate = Decimal((item.contents[3].text[0:5]).replace(",", "."))
			interests = Interest(description, interest_rate)
			inLoans[j].interests.append(interests)
	
	return inLoans


#
#	Out Loans
#	newest == True for newest possible data, newest == False for cached data
#	Returns list of Account objects that contain out loans
#
def getOutLoans(newest):
	
	if( newest ):
		soup = getNewestData()
	else:
		soup = getCachedData()

	table = soup.find(id="outinteresttable")
	tr = table.find_all('tr')

	outLoans = []
	j = -1
	for item in tr:
		if( isParent(item) ):
			account = Account(item.strong.text, [])
			outLoans.append(account)
			j += 1
		elif( item['class'] ):
			description = item.contents[1].text.strip()
			interest_rate = Decimal((item.contents[3].text[0:5]).replace(",", "."))
			interests = Interest(description, interest_rate)
			outLoans[j].interests.append(interests)

	outLoans = handleCarOutLoans(outLoans)

	return outLoans


# Testing - this can be deleted
inLoans = getInLoans(False)
outLoans = getOutLoans(False)

for account in inLoans:
		print "****************************"
		print account.name
		print "---------"
		for interests in account.interests:
			print interests.description
			print interests.interest_rate

for account in outLoans:
		print "****************************"
		print account.name
		print "---------"
		for interests in account.interests:
			print interests.description
			print interests.interest_rate