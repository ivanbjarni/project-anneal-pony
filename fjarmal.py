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

#listi af Reikningum (accounts)
accounts = []

def insfields( self, insaccname, insaccinterest, insaccreq, insaccinfl, list ):
	index = self.GetCurrentSelection()
	insaccname.SetValue( list[index].name )
	insaccinterest.SetValue( str(list[index].interests) )
	insaccreq.SetValue( str(list[index].reqtime) )
	insaccinfl.SetValue( list[index].indexadj )

def calcBestWayToPayacc1( paymentbox, amountbox, inflt1, inflt2, drawingPanel, answer ) :
	payment = validateStringToNumber(paymentbox.GetValue())
	amount = validateStringToNumber(amountbox.GetValue())
	infl = calcInflation(inflt1.GetCurrentSelection(),inflt2.GetCurrentSelection(),False)/100
	s=""
	if( amount is False or payment is False ):
		print "Villa"
		s+="Villa"+"\n"
		
		if(paymentbox.GetValue() is ""):
			s+="Fylla þarf út í mánaðarleg greiðsla reitinn.".decode("utf-8")+"\n"
		elif(payment is False):
			s+="Vinsamlegast sláðu inn tölu í mánaðarleg greiðsla reitinn.".decode("utf-8")+"\n"
		elif(payment<0):
			s+="Þú getur ekki borgað neikvæða upphæð á mánuði.".decode("utf-8")+"\n"


		if(amountbox.GetValue() is ""):
			s+="Fylla þarf út í sparnaðar reitinn.".decode("utf-8")+"\n"
		elif( amount is False):
			s+="Vinsamlegast sláðu inn tölu í sparnaðar reitinn.".decode("utf-8")+"\n"
		elif(amount<=0):
			s+="Þetta forrit reiknar bara jákvæðan sparnað!".decode("utf-8")+"\n"

		answer.SetLabel(s)
		return
	if not accounts:
		print "Villa"
		s+="Villa"+"\n"
		print "Engir reikningar eru til".decode("utf-8")+"\n" 
		s+="Engir reikningar eru til".decode("utf-8")+"\n"
		return
#	acctypes = []
#	savingsTimes = []
	profit = 0
	index = 0
	savingsTime = 0
	reqMessage = ""
	if(inflt1.GetCurrentSelection()<inflt2.GetCurrentSelection()):
		s+="Verðbólgu tímabil ógilt, notað var síðasta árið \n \n".decode("utf-8")
	for i in range(0, len(accounts)):
		tempProfit = 0
		tempSavingsTime = 0
#		acctypes.append(accounts[i].acctype)
#		savingsTimes.append(howLong(accounts[i].acctype.interests, amount, payment, accounts[i].balance))
		tempSavingsTime = howLong(accounts[i].acctype.interests, amount, payment, accounts[i].balance)
		tempProfit = int(calcAvgAccProfit(accounts[i].acctype.interests, amount, payment, accounts[i].balance))
		if (tempProfit == -1):
			print ("Þú átt nú þegar " + amount + " kr.").decode("utf-8")
			s += ("Þú átt nú þegar " + amount + " kr.").decode("utf-8")
			return
		if( tempProfit > profit ):
			profit = tempProfit
			savingsTime = tempSavingsTime
			index = i
			if(accounts[i].acctype.reqtime > tempSavingsTime):
				reqMessage = ("Reikningurinn er þó bundinn í " + accounts[i].acctype.reqtime + " mánuði").decode("utf-8")

	[am, acc] = bestAccount(payment, savingsTime, infl, accounts, drawingPanel)
#	print 'am: ' + str(am)
#	print 'acc: ' + str(acc.balance)

	s+= ("Best er að leggja inn á ").decode("utf-8") + acc.acctype.name + (" í " + str(savingsTime) + " mánuði.").decode("utf-8") + "\n"
	s+= ("Mánaðarlegur hagnaður er þá ").decode("utf-8") + str(am/savingsTime-payment) + "\n"
	s+= "Heildar sparnaður er þá ".decode("utf-8")  + str(am-payment*savingsTime)
	s+= reqMessage
#	print ("Borgaðu " + str(payment) + " í " + str(savingsTime) + " mánuði inn á ").decode("utf-8") + accounts[index].acctype.name + "\n"
#	s += ("Borgaðu " + str(payment) + " í " + str(savingsTime) + " mánuði inn á ").decode("utf-8") + accounts[index].acctype.name + "\n"
#	print ("Mánaðarlegur meðaltalshagnaður af því er " + str(profit) + "kr.").decode("utf-8") + "\n"
#	s += ("Mánaðarlegur meðaltalshagnaður af því er " + str(profit) + "kr.").decode("utf-8") + "\n"
#	s += "Þetta fall er ekki tilbúið".decode("utf-8")+"\n"
	answer.SetLabel(s)

def calcBestWayToPayacc2( paymentbox, timebox, inflt1, inflt2, drawingPanel, answer ) :
	payment = validateStringToNumber(paymentbox.GetValue())
	time = validateStringToNumber(timebox.GetValue())
	infl = calcInflation(inflt1.GetCurrentSelection(),inflt2.GetCurrentSelection(),False)/100
	s=""
	if( time is False or payment is False ):
		print "Villa"
		s+="Villa"+"\n"
		
		if(paymentbox.GetValue()==""):
			s+="Fylla þarf út í mánaðarleg greiðsla reitinn.".decode("utf-8")+"\n"
		elif(payment is False):
			s+="Vinsamlegast sláðu inn tölu í mánaðarleg greiðsla reitinn.".decode("utf-8")+"\n"
		elif(payment<0):
			s+="Þú getur ekki borgað neikvæða upphæð á mánuði.".decode("utf-8")+"\n"


		if(timebox.GetValue() is ""):
			s+="Fylla þarf út í tíma reitinn.".decode("utf-8")+"\n"
		elif( time is False):
			s+="Vinsamlegast sláðu inn tölu í tíma reitinn.".decode("utf-8")+"\n"
		elif(time<=0):
			s+="Þú getur ekki breytt fortíðini, notaðu jákvæðan tíma!".decode("utf-8")+"\n"

		answer.SetLabel(s)
		return
	global accounts
	keepaccounts = []
	for a in accounts:
		keepaccounts.append(copy.deepcopy(a))

	[am,acc] = bestAccount(payment, time, infl, accounts, drawingPanel)
	if(inflt1.GetCurrentSelection()<inflt2.GetCurrentSelection()):
			s+="Verðbólgu tímabil ógilt, notað var síðasta árið \n \n".decode("utf-8")
	if(am==0):
		s+= "Enginn reikningur uppfyllir þessar kröfur. ".decode("utf-8") 
	elif(am==-1):
		s+= "Þú átt enga reikninga. Við mælum með að þú stofnir slíkan.".decode("utf-8") 
	else:
		s+="Best er að leggja inn á ".decode("utf-8") + acc.acctype.name +" mánaðarlegur hagnaður er þá ".decode("utf-8") + str(am/time-payment) + "\n"
		s+= "Heildar sparnaður er þá ".decode("utf-8")  + str(am-payment*time)
	accounts[:] = []
	for a in keepaccounts:
		accounts.append(copy.deepcopy(a))
	answer.SetLabel(s)

# Reikna bestu leið til að borga lán, og skrifa það í console
# tekur inn 2 textabox og eitt combobox
def calcBestWayToPayLoan(paymentbox, timebox, inflt1,inflt2, drawingPanel, plotAll, answer):
	count = 0
	profit = []
	infl = calcInflation(inflt1.GetCurrentSelection(),inflt2.GetCurrentSelection(),False)/100
	payment = validateStringToNumber(paymentbox.GetValue())
	time = validateStringToNumber(timebox.GetValue())
	s = ""
	if( time is False or payment is False or payment<0 or time<=0):
		s=""
		print "Villa"
		s+="Villa"+"\n"

		if(paymentbox.GetValue() is""):
			s+="Fylla þarf út í mánaðarleg greiðsla reitinn.".decode("utf-8")+"\n"
		elif(payment is False):
			s+="Vinsamlegast sláðu inn tölu í mánaðarleg greiðsla reitinn.".decode("utf-8")+"\n"
		elif(payment<0):
			s+="Þú getur ekki borgað neikvæða upphæð á mánuði.".decode("utf-8")+"\n"


		if(timebox.GetValue() is ""):
			s+="Fylla þarf út í tíma reitinn.".decode("utf-8")+"\n"
		elif( time is False):
			s+="Vinsamlegast sláðu inn tölu í tíma reitinn.".decode("utf-8")+"\n"
		elif(time<=0):
			s+="Þú getur ekki breytt fortíðini, notaðu jákvæðan tíma!".decode("utf-8")+"\n"

		answer.SetLabel(s)
		return
	if(inflt1.GetCurrentSelection()<inflt2.GetCurrentSelection()):
		s+="Verðbólgu tímabil ógilt, notað var síðasta árið \n \n".decode("utf-8")	
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
		temp = calcTimeToPayLoan(l[0], infl, payment, time, drawingPanel, plotAll, count)
		time -= temp[1]
		p = calcProfitPerTime(l[0], payment, infl)
		profit.append(p)
		loans[l[1]].numberOfP=0
		if(time < 0):
			temp[1] += time
		print ("Borgaðu "+str(payment)+" kr. í "+str(temp[1])+" mánuði af ").decode("utf-8")+l[0].name+"\n"
		s += ("Borgaðu "+str(payment)+" kr. í "+str(temp[1])+" mánuði af ").decode("utf-8")+l[0].name+"\n"
		print ("Mánaðarlegur hagnaður af því er "+str(p)+"kr.").decode("utf-8")
		s += ("Mánaðarlegur hagnaður af því er "+str(p)+"kr.").decode("utf-8")+"\n \n"
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
	if(interests is False or numberOfP is False or balance is False ):
		print "villa"
		s="Villa, fylla þarf í alla reiti. Tölur þar sem við á. ".decode("utf-8")
		answer.SetLabel(s)
		return
	loan = Loan(name, balance, interests/100.0, infl, numberOfP)
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
	if( acc_interests is False or acc_reqtime is False or acc_balance is False ):
		print "villa"
		s="Villa, fylla þarf í alla reiti. Tölur þar sem við á. ".decode("utf-8")
		answer.SetLabel(s)
		return
	accType = AccountType(acc_name, acc_reqtime, float(acc_interests)/100, acc_indexadj, -1, -1)
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