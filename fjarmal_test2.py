#!/usr/bin/python
# -*- coding: utf-8 -*-

from calcLoanFun import *
import unittest
from random import randint

def calcProfitPerTimeTest():
	loans = makeRandomLoans()[0]
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
		l = randomWithBestLoan(inflation, i)
		for i in range(0, len(l)):
			if( calcBestLoan(l, inflation) != l[i] ):
				print "Villa ekki rett lan sem var besta lan"

# Byr til random inflation
def makeRandomInflation():
	return random.uniform(-0.5,0.9)

# Byr til random payment
def makeRandomPayment():
	return randint(0, 1000)

# Byr til helling af random lanum sem meika sens og skilar einnig indexin a tvi lani sem er best
def makeRandomLoansWithBestLoan():
	l = []
	length = randint(15,1000)
	MAX = -2
	index = randint(0, length-1)
	for i in range(0, length):
		rBalance = randint(1100,100000000)
		if ( i == index):
			rInterest = 1.0
		else:
			rInterest = random.uniform(0.01, 0.9)
		rNumP = randint(1, 1000)
		l.append(Loan("", rBalance, rInterest, False, rNumP))
	return [l, index]

# Byr til helling af random lanum sem meika sens og skilar einnig indexin a tvi lani sem er best
def makeRandomLoans():
	l = []
	length = randint(15,1000)
	inf=makeRandomInflation()
	for i in range(0, length):
		rBalance = randint(1100,100000000)
		rInterest = random.uniform(0.01, 0.9)
		if(rInterest < 0.5):
			rInfl = False
		else:
			rInfl = True
		rNumP = randint(1, 1000)
		l.append(Loan("", rBalance, rInterest, rInfl, rNumP))
	return l

class TestcalcLoanFun(unittest.TestCase):
	# Athugar hvort calcProfitPerTime se rett reiknad
	def test_calcProfitPerTime_correct(self):
		l = makeRandomLoans()
		for i in range(0, len(l)):
			if(l[i].infl):
				inflation = makeRandomInflation()
			else:
				inflation = 0
			payment = makeRandomPayment()
			self.assertEqual(calcProfitPerTime(l[i], payment, inflation), payment * (inflation + l[i].interest))


	# Athugar hvort calcProfitPerTime se ad skila jakvaedri tolu tegar tad a ad skila jakvaedri tolu
	def test_calcProfitPerTime_negative(self):
		l = makeRandomLoans()
		for i in range(0, len(l)):
			inflation = makeRandomInflation()
			payment = makeRandomPayment()
			self.assertTrue(calcProfitPerTime(l[i], payment, inflation) >= 0, str(payment))

	# athugar hvort calcbestloan skili -1 ef balance og number of payments left eru baedi 0 í öllum lánum
	def test_calcBestLoan_noLoan(self):
		self.assertEqual(calcBestLoan([Loan("",0,0.2,False,0)], 0.3), -1, "Villa tegar tad er enginn hofudstoll a laninu i calcProfitPerTime fallinu")

	# Athugar hvort calcBestLoan se ad skila besta laninu
	def test_calcBestLoan_correct(self):
		loans = makeRandomLoansWithBestLoan()
		l = loans[0]
		index = loans[1]
		self.assertTrue(calcBestLoan(l, 0) == [l[index],index])

	# Athugar hvort calcTimeToPayLoan skili 
	def test_calcTimeToPayLoan(self):
		loans = makeRandomLoans()
		for i in range(0, len(loans)):
			payment = makeRandomPayment()
			inflation = makeRandomInflation()
			self.assertTrue(calcTimeToPayLoan(loans[i], inflation, payment, None, 0)>=0)




suite = unittest.TestLoader().loadTestsFromTestCase(TestcalcLoanFun)
unittest.TextTestRunner(verbosity=2).run(suite)

