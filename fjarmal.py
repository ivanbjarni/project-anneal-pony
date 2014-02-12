#!/usr/bin/python
# -*- coding: utf-8 -*-

from wxgui3 import *
from calcLoanFun import *
from inflation import *
from AccountType import *
from Account import *
import wx
import copy

loans = []
# fylki til að halada utan um lán
loansName = []

#listi af Reikningum (accounts)
accounts = []

# Reikna bestu leið til að borga lán, og skrifa það í console
# tekur inn 2 textabox og eitt combobox
def calcBestWayToPayLoan(payment, time, inflt, drawingPanel):
	profit = []
	infltim = infltime(inflt.GetCurrentSelection())
	infl = getInflationCoefficient(infltim)/100
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
		temp = calcTimeToPayLoan(l[0], infl, payment, drawingPanel)
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


#Býr til lán og bætir því í núverandi lán boxið
def makeLoan(nop, infl, nm, amount, interest, answer, loanlist):	
	global loans
	name = nm.GetValue()
	interests = validateStringToNumber(interest.GetValue())
	numberOfP = validateStringToNumber(nop.GetValue())
	infl = infl.GetValue()
	balance = validateStringToNumber(amount.GetValue())
	if(interests==-1 or numberOfP==-1 or infl==-1 or balance==-1 ):
		print "villa"
		answer.SetLabel("Villa bætti láni ekki inn".decode("utf-8"))
		return
	loan = Loan(name, balance, interests/100.0, infl, numberOfP)
	loansName.append(loan.name)
	loans.append(loan)
	index = loanlist.GetItemCount()
	nop.SetValue("")
	nm.SetValue("")
	amount.SetValue("")
	interest.SetValue("")
	loanlist.InsertStringItem(index, loan.name)
	loanlist.SetStringItem(index, 1, str(loan.balance))
	loanlist.SetStringItem(index, 2, str(loan.interest*100))
	loanlist.SetStringItem(index, 3, str(loan.infl))
	loanlist.SetStringItem(index, 4, str(loan.numberOfP))
	answer.SetLabel("Bætti Láni inn".decode("utf-8"))
	#loanlist.InsertItem(item)
	print "Bætti Láni inn".decode("utf-8")

def makeAccount(name, balance, interests, reqtime, indexadj, answer, accountlist):
	acc_name = name.GetValue()
	acc_balance = validateStringToNumber(balance.GetValue())
	acc_interests = validateStringToNumber(interests.GetValue())
	acc_reqtime = validateStringToNumber(reqtime.GetValue())
	acc_indexadj = indexadj.GetValue()
	if( interests == -1 or reqtime == -1):
		print "villa"
		answer.SetLabel("Villa bætti láni ekki inn".decode("utf-8"))
		return
	accType = AccountType(acc_name, acc_reqtime, acc_interests, acc_indexadj, -1, -1)
	account = Account(accType, acc_balance)
	accounts.append(account)
	index = accountlist.GetItemCount()
	name.SetValue("")
	balance.SetValue("")
	interests.SetValue("")
	reqtime.SetValue("")
	accountlist.InsertStringItem(index, account.acctype.name)
	accountlist.SetStringItem(index, 1, str(account.balance))
	accountlist.SetStringItem(index, 2, str(account.acctype.interests))
	accountlist.SetStringItem(index, 3, str(account.acctype.indexadj))
	accountlist.SetStringItem(index, 4, str(account.acctype.reqtime))
	answer.SetLabel("Bætti reikningi við".decode("utf-8"))
	print "Bætti við reikning".decode("utf-8")

#Athuga hvort strengur er tala og
#skilar tölunni ef strengurinn er tala en annars -1
def validateStringToNumber(string):
	try:
		return float(string) if '.' in string else int(string)
	except ValueError:
		return -1;

if __name__ == '__main__':
    initGui()