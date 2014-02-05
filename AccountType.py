# -*- coding: cp1252 -*-
#class sem heldur utan um mismunandi accounts, sem lesnir eru úr skrá.
class AccountType:
    def __init__(self, name, minimum, maximum, reqtime, interests, indexadj, idnum,nextid):
        #set values for attributes
        self.name = name #nafn
        self.minimum = minimum #lagmarksupphaed
        self.maximum = maximum #hamarksupphaed
        self.reqtime = reqtime #lagmarksbinditimi
        self.interests = interests #vextir%
        self.indexadj = indexadj #er reikningurinn verðtryggður?
        self.idnum = idnum #auðkennisnúmer
        self.nextid = nextid #hvert á að fara þegar hamarki er nad
        
    #skilar nafni reiknings(tegund)
    def getName(self):
        return self.name
    
    #skilar hamarksupphaed reiknings
    def maxAmount(self):
        return self.maximum
    
    #skilar lagmarksupphaed reiknings
    def minAmount(self):
        return self.minimum
    
    #skilar lagmarksbinditima reiknings
    def reqTime(self):
        return self.reqtime
    
    #skilar vöxtum reiknings
    def getInterests(self):
        return self.interests
    
    #skilar true ef reikningur er verðtryggður, false annars
    def isIndexAdj(self):
        if(self.indexadj == 1):
            return True
        else:
            return False
        
    #skilar upplysingum um reikning (hugsað fyrir debug)
    def getInfo(self):
        print "The account info is:",self.name,self.minimum,self.maximum,self.reqtime,self.interests,self.indexadj,self.idnum,self.nextid

# notað til að lesa inn týpur reikninga i upphafi keyrslu forrits, skilar lista sem inniheldur allar
# reikningstýpurnar
def readAccountTypes():
    f=open('innlan.txt','r')
    listi = []
    accountslisti=[]
    i = 0
    listi = f.read().splitlines()
    for item in listi:
        temp = item.split(",")
        acc = AccountType(temp[0],int(temp[1]),int(temp[2]),int(temp[3]),float(temp[4]),int(temp[5]),int(temp[6]),int(temp[7]))
        accountslisti.append(acc)
    return accountslisti

#testforrit
def tryit():
    x = readAccountTypes()
    for item in x:
        item.getInfo()

    
