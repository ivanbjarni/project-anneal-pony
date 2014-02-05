from wxgui import *
from calcLoanFun import *

loans = []
# For the focking gui shit
loansName = []

def calc

def makeLoan(nop, infl, name, amount, interests, loansComboBox):	
	name = name.GetValue()
	interests = validateStringToNumber(interests.GetValue())
	numberOfP = validateStringToNumber(nop.GetValue())
	infl = infl.GetValue()
	balance = validateStringToNumber(amount.GetValue())
	if(interests==-1 or numberOfP==-1 or infl==-1 or balance==-1 ):
		print "villa"
		return
	loan = Loan(name, balance, interests, infl, numberOfP)
	loansName.append(loan.name)
	loans.append(loan)
	loansComboBox.SetItems(loansName)



def validateStringToNumber(string):
	try:
		return float(string) if '.' in string else int(string)
	except ValueError:
		return -1;