from calcLoanFun import *
import random
from random import randint

# Athugar hvort calcProfitPerTime fallid skili tvi sem buist er vid af tvi
def calcProfitPerTimeTest():
	loans = makeRandomLoans()
	inflation = makeRandomInflation()
	payment = makeRandomPayment()
	for i in range(0,len(loans)):
		l = loans[i]
		if(calcProfitPerTime(l, payment, inflation) != l.interest * payment and not l.infl):
			return False
		if(calcProfitPerTime(l, payment, inflation) != (l.interest + inflation) * payment and l.infl):
			return False
		if(calcProfitPerTime(l, payment, inflation) < 0 and l.infl and inflation < -l.interest):
			return False
	return true

# Athugar hvort calcBestLoan fallid skili tvi sem buist er vid af tvi
def calcBestLoanTest():
	for i in range(0, 100):
		inflation = makeRandomInflation()
		l = randomWithBestLoan(inflation, i):
		for i in range(0, len(l)):
			if( calcBestLoan(l, inflation) != l[i] ):
				print "Villa ekki rétt lán sem var besta lán"

# Byr til random inflation
def makeRandomInflation():
	return random.uniform(-0.5,0.9)

def randomWithBestLoan(infl, index):
	l = []
	length = randint(15,1000)
	max = 0
	for i in range(0, length):
		rBalance = randint(1100,100000000)
		rInterest = random.uniform(0.01, 0.9)
		if(rInterest < 0.5):
			rInfl = False
			if ( rInterest =  )
		else:
			rInfl = True
		rNumP = randint(1, 1000)
		l.append(Loan("", rBalance, rInterest, rInfl, rNumP))

# Byr til helling af random lanum sem meika sens
def makeRandomLoans():
	l = []
	length = randint(15,1000)
	for i in range(0, length):
		rBalance = randint(1100,100000000)
		rInterest = random.uniform(0.01, 0.9)
		if(rInterest < 0.5):
			rInfl = False
		else:
			rInfl = True
		rNumP = randint(1, 1000)
		l.append(Loan("", rBalance, rInterest, rInfl, rNumP))

def mainLoanTest():
	for i in range(0, 1000):
		if ( !calcProfitPerTimeTest(payment, inflation) ):
			print "Villa í calcProfitPerTimeTest!!!"
