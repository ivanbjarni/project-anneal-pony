from Account import *
from AccountType import *
from random import randint 
import unittest

#By til lista af tegundum reikninga og reikningum.  Baeti vid tveimur bestu gildunum i thessu skjali.
acctypes = []
accounts = []
BestAcctype = AccountType(101, 2, 0.5, True, -1, -1) 
acctypes.append(BestAcctype) 
BestAcc= Account(BestAcctype, 999999)
accounts.append(BestAcc)

#Fall sem baetir tegundum reikninga og reikningum i videigandi lista.
def makeRandomAccounts():
    for i in range (0, 100):
        i = AccountType(i, randint(0, 120), randint(0,6), (randint(0, 1) == 1), -1, -1)
        acctypes.append(i)
        account = Account(i, randint(0, 100000))
        accounts.append(account)


class TestAccountFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(100000)

    def test_howMuch(self):
        self.assertTrue(howMuch(0.02, 20, 1000) > 0)
        self.assertEqual(round(howMuch(0.05, 10, 5000)), 66034)
        self.failUnless(howMuch(0.2, 20, 100000))
        self.assertAlmostEqual(howMuch(0.05, 10, 5000), 66033.9358116)


    def test_howLong(self):
        self.failUnless(howLong(0.04, 1000000, 100))
        self.assertTrue(howLong(0.05, 5000, 1000))

    def test_bestAccount(self):
        makeRandomAccounts()
        self.failUnless(bestAccount(1000, 25, 0.04, accounts))

    def test_bestAccountType(self):
        self.failUnless(bestAccountType(1000,  15, 0.05, acctypes))

    def test_calcAccProfit(self):
        self.failUnless(calcAccProfit(BestAcc))
        self.assertAlmostEqual(calcAccProfit(BestAcc), 499999.5)


suite = unittest.TestLoader().loadTestsFromTestCase(TestAccountFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)