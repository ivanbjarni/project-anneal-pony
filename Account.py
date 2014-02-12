# -*- coding: cp1252 -*-
from AccountType import *

class Account(object):
    def __init__(self, accType, balance):
#        self.name = name #nafn
        self.acctype = accType #tegund reiknings        
        self.balance = balance #innistaeda reiknings
#        self.interests = interests
#        self.isIndexAdj = isIndAdj
#        self.reqtime = reqtime
        
#    def accountT(self):
#       return self.acctype

#    def setBalance(self, x):
#        self.balance = x
    
#    def getBalance(self):
#        return self.balance

#    def addBalance(self, x):
#        self.balance += x


def calcAccProfit(account):
    return (account.accType.interests / 1200.0) * account.balance - account.balance

#def calcAccProfit(account):
#    profit = (account.accountT().getInterests()/1200.0)*account.getBalance()-account.getBalance()
#    return profit

#hversu mikið þú getur safnað með því að leggja eitthvað ákveðið inn á rkn í ákveðinn tíma
def howMuch(interests, time, amount):
    total = 0.0
    while(time>0):
        total += amount
        total += total * interests
        time -= 1
    return total

#hversu langan tíma það tekur að ná x upphæð á reikningi með y vextií% á mánuði þegar z 
#upphæð er lögð fyrir á mánuði
def howLong(interests, wantam, haveam):
    total = 0.0
    months = 1
    vextir = interests/1200.0
    while(wantam > total):
        total += haveam
        total += total * vextir
        months += 1
    return months


#Velur besta reikning fyrir:
#amount er upphaed sem hægt er að spara á mánuði, time er tíminn sem mun líða í mánuðum,inflcoeff er verðbólgustuðull
#accounts er listi af reikningum. Fallið skilar reikning sem best er að nota
def bestAccount(amount, time, inflcoeff, accounts):
    maxamount = []
    for item in accounts:
        total = 0.0
        if(item.acctype.reqtime <= time and item.acctype.minimum <= amount):
            vextir = item.acctype.interests
            if(item.acctype.indexadj):
                vextir += inflcoeff
            vextirpermonth = time * (1.0 / 12.0) * (vextir / 1200.0)
            for i in range(time, 0, -1):
                total += amount
                profit = vextirpermonth * total
                total += profit
            maxamount.append(total)
        else:
            maxamount.append(total)
    p = max(maxamount)
    return [p, accounts[maxamount.index(p)]]


#Velur besta reikningstýpu fyrir:
#amount er upphaed sem hægt er að spara á mánuði, time er tíminn sem mun líða í mánuðum,inflcoeff er verðbólgustuðull
#acctype er listi af tegundum reikninga. Fallið skilar tegund reiknings sem best er að nota
def bestAccountType(amount, time, inflcoeff, acctype):
    maxamount = []
    for item in acctype:
        total = 0.0
        if(item.reqtime <= time and item.minimum <= amount):
            vextir = item.interests
            if(item.indexadj):
                vextir += inflcoeff
            vextirpermonth = time * (1.0 / 12.0) * (vextir / 1200.0)
            for i in range(time, 0, -1):
                total += amount
                profit = vextirpermonth * total
                total += profit
            maxamount.append(total)
        else:
            maxamount.append(total)
    p = max(maxamount)
    return [p, acctype[maxamount.index(p)]]

#Velur besta reikning fyrir:
#amount er upphaed sem hægt er að spara á mánuði, time er tíminn sem mun líða í mánuðum,inflcoeff er verðbólgustuðull
#acctype er listi af tegundum reikninga. Fallið skilar tegund reiknings sem best er að nota
#def bestAccount(amount, time, inflcoeff, acctype):
#    maxamount = []
#    for item in acctype:
#        total = 0.0
#        if(item.reqTime()<=time and item.minAmount()<=amount):
#            vextir = item.getInterests()
#            if(item.isIndexAdj()):
#                vextir += inflcoeff
#            vextirpermonth = time*(1.0/12.0)*(vextir/1200.0)
#            for i in range(time,0,-1):
#                total += amount
#                profit = vextirpermonth*total
#                total += profit
#            maxamount.append(total)
#        else:
#            maxamount.append(total)
#    p = max(maxamount)
#    return [p,acctype[maxamount.index(p)]]
#Testforrit:

#def tryit2():
#    x = bestAccount(100000.0,2,2.0,AccountType.readAccountTypes())
#    print x[0]
#    x[1].getInfo()
#def tryit3():
#    print howLong(4.0,10000.0,2000.0)
#    
#def tryit4():
#    print howMuch(4.0,3,10000.0)
#tryit2()
