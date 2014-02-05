#!/usr/bin/python
# -*- coding: utf-8 -*-

from wxgui2 import *
from calcLoanFun import *
from inflation import *
import copy

loans = []
# For the gui combobox
loansName = []

def calcBestWayToPayLoan(payment, time, inflt):
	profit = []
	infltim = infltime(inflt.GetCurrentSelection())
	infl = getInflationCoefficient(infltim)
	payment = validateStringToNumber(payment.GetValue())
	time = validateStringToNumber(time.GetValue())
	if( time == -1 or payment == -1 ):
		print "villa"
		return
	global loans
	keeploans = []
	for a in loans:
		keeploans.append(copy.deepcopy(a))
	while(time>0):
		l = calcBestLoan(loans, infl)
		if(l==-1):
			print "Þú ert orðinn skuldlaus!!".decode("utf-8")
			for a in keeploans:
				loans.append(copy.deepcopy(a))
			return
		temp = calcTimeToPayLoan(l[0], infl, payment)
		time -= temp[1]
		p = calcProfitPerTime(l[0], payment, infl)
		profit.append(p)
		loans[l[1]].numberOfP=0
		if(time < 0):
			temp[1] += time
		print ("Borgaðu "+str(payment)+" kr. í "+str(temp[1])+" mánuði/ár af "+str(l[0].name)).decode("utf-8")
		print ("Mánaðarlegur/árlegur hagnaður af því er "+str(p)+"kr.").decode("utf-8")
	for a in keeploans:
		loans.append(copy.deepcopy(a))



def makeLoan(nop, infl, name, amount, interests, loansComboBox):	
	global loans
	name = name.GetValue()
	interests = validateStringToNumber(interests.GetValue())
	numberOfP = validateStringToNumber(nop.GetValue())
	infl = infl.GetValue()
	balance = validateStringToNumber(amount.GetValue())
	if(interests==-1 or numberOfP==-1 or infl==-1 or balance==-1 ):
		print "villa"
		return
	loan = Loan(name, balance, interests/100.0, infl, numberOfP)
	loansName.append(loan.name)
	loans.append(loan)
	loansComboBox.SetItems(loansName)



def validateStringToNumber(string):
	try:
		return float(string) if '.' in string else int(string)
	except ValueError:
		return -1;

if __name__ == '__main__':
    initGui()