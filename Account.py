# -*- coding: cp1252 -*-
import AccountType
class Account:
    def __init__(self,acctype,balance):
        self.acctype = acctype #tegund reiknings
        self.balance = balance #innistaeda reiknings
    def setBalance(self,x):
        self.balance = x
    def getBalance(self):
        return self.x
    def addBalance(self, x):
        self.balance = self.amount + x

#hversu miki� �� getur safna� me� �v� a� leggja eitthva� �kve�i� inn � rkn � �kve�inn t�ma
#hversu langan t�ma �a� myndi taka a� safna x miki� af pening ef a� y mikid er lagt inn i manudi

#amount er upphaed sem h�gt er a� spara � m�nu�i, time er t�minn sem mun l��a � m�nu�um,inflcoeff er ver�b�lgustu�ull
#acctype er listi af tegundum reikninga. Falli� skilar tegund reiknings sem best er a� nota
def howMuch(amount,time,inflcoeff,acctype):
    maxamount = []
    for item in acctype:
        total = 0.0
        if(item.reqTime()<=time):
            vextir = item.getInterests()
            if(item.isIndexAdj()):
                vextir += inflcoeff
            vextirpermonth = time*(1.0/12.0)*(vextir/100.0)
            for i in range(int(time),0,-1):
                total += amount
                profit = vextirpermonth*total
                total += profit
            if(item.minAmount()>total):
                maxamount.appe
            maxamount.append(total)
        else:
            maxamount.append(total)
    p = max(maxamount)
    return [p,acctype[maxamount.index(p)]]
def tryit2():
    x = howMuch(100.0,2.0,2.0,AccountType.readAccountTypes())
    print x[0]
    x[1].getInfo()
    
