from Account import *
from AccountType import *
import unittest

class TestAccountFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_howMuch(self):
        self.assertTrue(howMuch(0.02, 20, 1000)> 0)



"""
        def test_calcProfitPerTime_negative(self):
        l = makeRandomLoans()
        for i in range(0, len(l)):
            inflation = makeRandomInflation()
            payment = makeRandomPayment()
            self.assertTrue(calcProfitPerTime(l[i], payment, inflation) >= 0, str(payment))
"""

suite = unittest.TestLoader().loadTestsFromTestCase(TestAccountFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)