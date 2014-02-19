# -*- coding: cp1252 -*-
#Notkun: x = readInflation(visitala.txt)
#Fyrir: visitala.txt er textaskrá sem inniheldur visitolur manadanna 
#       januar 1990 til januar 2014
#Eftir: x er listi vísitalna í öfugri lesröð(1. janúar er fremstur)
def readInflation(files):
        f = open(files,'r')
        listi = []
        
        done = False
        while(not done):
                s = f.readline()
                if(s != ''):
                        listi.append(s)
                else:
                        done = True
        rightlisti = []
        for item in listi:
                rightlisti.insert(0,item)
                
        return rightlisti
print readInflation('visitala.txt')

#Notkun: man = makeMonths()
#Fyrir: ekkert
#Eftir: man=[januar 2014, desember 2013,...,januar 1990]
def makeMonths():
    man = []
    manudir = ["desember", "nóvember", "október","september", "ágúst", "júlí", "júní", "mai", "apríl", "mars", "febrúar","janúar"]
    print "bla"
    man.append(manudir[0] + str(2014))
    for i in range(2013, 1989, -1):
        for item in manudir:
            man.append(item + str(i))
    return man

#Notkun: inflation = calcInflation(f,t,d)
#Fyrir: from<=too ef default=false
#Eftir: inflation er verðbólgan frá from til too
def calcInflation(froma, to, default):
    if(default):
        return getInflationCoefficient(12)
    listi = readInflation('visitala.txt')
    summ = 0
    count = 0
    for i in range(froma, to + 1):
        summ += float(listi[i])
        count += 1
    return summ/count


#Notkun:x = getInflationCoefficient(months)
#Fyrir: months er fjöldi mánaða sem við ætlum að nota
#Eftir: x er verðbólguspá reiknuð með  vísitölum months marga mánuði aftur í
#       tímann. Þetta er meðaltalsspá.
def getInflationCoefficient(months):
        listi = readInflation('visitala.txt')
        i=0
        summa = 0
        while(i<=months):
                summa+=float(listi[i])
                i+=1
        return summa/i

def infltime(x):
    return {
        0 : 1,
        1: 2,
        2: 6,
        3: 12,
        4: 24,
    }[x]