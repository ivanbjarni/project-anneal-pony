#!/usr/bin/python
# -*- coding: utf-8 -*-

from wxgui import *
from calcLoanFun import *

loans = []
# For the focking gui shit
loansName = []

def calcBestWayToPayLoan(payment, time):
	profit = []
	infl = 0
	payment = validateStringToNumber(payment.GetValue())
	time = validateStringToNumber(time.GetValue())
	if( time == -1 or payment == -1 ):
		print "villa"
		return
	while(time>0):
		l = calcBestLoan(loans, infl)
		temp = calcTimeToPayLoan(l[0], infl, payment)
		time -= temp[1]
		p = calcProfitPerTime(l[0], payment, infl)
		profit.append(p)
		loans[l[1]].numberOfP=0
		print ("Borgaðu "+str(payment)+" á "+str(time)+" mánuði/ári af "+str(l[0].name)).decode("utf-8")
		print ("Mánaðarlegur/árlegur hagnaður af því er"+str(p)).decode("utf-8")


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