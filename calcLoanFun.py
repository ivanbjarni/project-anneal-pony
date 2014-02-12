# Notkun: x = Loan(n,b,i,infl,nr)
# Fyrir: n er nafnid a laninu
# 		 b er thad sem thu att eftir ad borga af laninu 
# 		 i eru vextirnir a laninu 
# 		 infl segir til um hvort lanid se verdtryggt eda ekki 
# 		 nr er fjoldi greidsla sem eftir eru 
# Eftir: x er lan 

from wxgui3 import *
#from fjarmal import *

class Loan: 
	def __init__(self, name, balance, interest, infl, numberOfPayments): 
		self.name = name 
		self.balance = balance 
		self.interest = interest 
		self.infl = infl 
		self.numberOfP = numberOfPayments

# returns the profit of putting your payment on the loan instead of keeping it
def calcProfitPerTime(loan, payment, inflation):
	if(loan.infl):
		return (inflation + loan.interest) * payment
	return loan.interest * payment

# returns the best loan to put your payment on
def calcBestLoan(loans, inflation):
	temp = 0
	Max = 0
	index = 0
	for i in range(0, len(loans)):
		if(loans[i].infl):
			temp = inflation
		else:
			temp = 0
		if (loans[i].interest + temp>Max and loans[i].numberOfP > 0):
			Max = loans[i].interest + temp
			index = i
	if (Max==0):
		return -1
	return [loans[index],index]

# returns [leftover, time] the time it takes to pay the loan with a extra payment and the money you have left
def calcTimeToPayLoan(loan, inflation, payment, drawingPanel):
	temp = loan
	time = 0
	balanceList = [] #hafa 'i huga, sko[a 'asa']
	timeList = []
	while(temp.balance > payment):
		timeList.append(time + 1)
		balanceList.append(temp.balance)
		if(temp.infl):
			temp.balance -= (temp.balance/temp.numberOfP - payment)*(1 + inflation + temp.interest)
			temp.numberOfP -= 1
		else:
			temp.balance -= (temp.balance/temp.numberOfP - payment)*(1 + temp.interest)
			temp.numberOfP -= 1
		time = time + 1
	leftover = payment - temp.balance
	time = temp.balance/payment + time
#	timeList.append(time)
#	balanceList.append(0)
	drawingPanel.draw(timeList, balanceList)
	return [leftover, time]

# Notkun: x = calcLoan(b, int, p, inf, t) 
# Fyrir: b er innistaeda/hofudstoll lans 
# 		 p er greidsla a timaeiningu 
# 		 int eru vextir a grundvelli timaeiningar 
# 		 inf er verdbolga a grundvelli timaeiningar 
# 		 t er fjoldi timaeininga 
# Eftir: x er innistaeda/hofudstoll sem eftir er af lani 
def calcLoan(balance, interest, payment, inflation, time): 
	for i in xrange(0,time):
		balance -= payment 
		balance = balance*(1+interest+inflation) 
		return balance

# returns the median of a list li
def median(li):
	s = 0
	c = 0
	for i in li:
		s += i
	return s/c

#loans=[Loan("Megalan", 10000, 0.12, False, 4), Loan("Lelegtlan", 100000, 0.01, True, 10)]

#print calcTimeToPayLoan(loans[0], 0.0, 10000)