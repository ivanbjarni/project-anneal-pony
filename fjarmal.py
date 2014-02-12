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


def calcBestWayToPayacc2( paymentbox, timebox, infltimebox, answer ) :
	payment = validateStringToNumber(paymentbox.GetValue())
	time = validateStringToNumber(timebox.GetValue())
	infltim = infltime(infltimebox.GetCurrentSelection())
	infl = getInflationCoefficient(infltim)/100

	if( time == False or payment == False ):
		s=""
		print "Villa"
		s+="Villa"+"\n"
		if( time == False):
			s+="Fylla þarf út í tíma reitin".decode("utf-8")+"\n"
		if(payment == False):
			s+="Fylla þarf út í mánaðarleg greiðsla reitin".decode("utf-8")+"\n"
		answer.SetLabel(s)
		return
	global accounts
	keepaccounts = []
	for a in accounts:
		keepaccounts.append(copy.deepcopy(a))

	[am,acc] = bestAccount(payment, time, infl, accounts)
	s+=acc.acctype.name

	for a in keeploans:
		loans.append(copy.deepcopy(a))
	answer.SetLabel(s)

# Reikna bestu leið til að borga lán, og skrifa það í console
# tekur inn 2 textabox og eitt combobox
def calcBestWayToPayLoan(payment, time, inflt, drawingPanel, answer):
	count = 0
	profit = []
	infltim = infltime(inflt.GetCurrentSelection())
	infl = getInflationCoefficient(infltim)/100
	payment = validateStringToNumber(payment.GetValue())
	time = validateStringToNumber(time.GetValue())
	s = ""
	if( time == False or payment == False ):
		s=""
		print "Villa"
		s+="Villa"+"\n"
		if( time == False):
			s+="Fylla þarf út í tíma reitin".decode("utf-8")+"\n"
		if(payment == False):
			s+="Fylla þarf út í mánaðarleg greiðsla reitin".decode("utf-8")+"\n"
		answer.SetLabel(s)
		return
	global loans
	keeploans = []
	for a in loans:
		keeploans.append(copy.deepcopy(a))
	while(time>0):
		count += 1
		l = calcBestLoan(loans, infl)
		if(l==-1):
			print "Þú ert orðinn skuldlaus!!".decode("utf-8")
			s += "Þú ert orðinn skuldlaus!!".decode("utf-8")+"\n"
			loans[:] = []
			for a in keeploans:
				loans.append(copy.deepcopy(a))
			answer.SetLabel(s)
			return
		temp = calcTimeToPayLoan(l[0], infl, payment, drawingPanel, count)
		time -= temp[1]
		p = calcProfitPerTime(l[0], payment, infl)
		profit.append(p)
		loans[l[1]].numberOfP=0
		if(time < 0):
			temp[1] += time
		print ("Borgaðu "+str(payment)+" kr. í "+str(temp[1])+" mánuði/ár af "+str(l[0].name)).decode("utf-8")
		s += ("Borgaðu "+str(payment)+" kr. í "+str(temp[1])+" mánuði/ár af "+str(l[0].name)).decode("utf-8")+"\n"
		print ("Mánaðarlegur/árlegur hagnaður af því er "+str(p)+"kr.").decode("utf-8")
		s += ("Mánaðarlegur/árlegur hagnaður af því er "+str(p)+"kr.").decode("utf-8")+"\n \n"
	loans[:] = []
	for a in keeploans:
		loans.append(copy.deepcopy(a))
	answer.SetLabel(s)


#Býr til lán og bætir því í núverandi lán boxið
def makeLoan(nop, infl, nm, amount, interest, answer, loanlist):	
	global loans
	name = nm.GetValue()
	interests = validateStringToNumber(interest.GetValue())
	numberOfP = validateStringToNumber(nop.GetValue())
	infl = infl.GetValue()
	balance = validateStringToNumber(amount.GetValue())
	if(interests==False or numberOfP==False or balance==False ):
		print "villa"
		s="Villa \n"
		if(interests==False):
			s += ""	
		answer.SetLabel(s)
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
	if( interests == False or reqtime == False or balance==False ):
		print "villa"
		answer.SetLabel("Villa bætti reikningi ekki inn".decode("utf-8"))
		return
	accType = AccountType(acc_name, acc_reqtime, acc_interests, acc_indexadj)
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
		return False;

if __name__ == '__main__':
    initGui()