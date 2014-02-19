# -*- coding: cp1252 -*-
#Notkun: x = readInflation(visitala.txt)
#Fyrir: visitala.txt er textaskr� sem inniheldur visitolur manadanna 
#       januar 1990 til januar 2014
#Eftir: x er listi v�sitalna � �fugri lesr��(1. jan�ar er fremstur)
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
    manudir = ["desember", "n�vember", "okt�ber","september", "�g�st", "j�l�", "j�n�", "mai", "apr�l", "mars", "febr�ar","jan�ar"]
    print "bla"
    man.append(manudir[0] + str(2014))
    for i in range(2013, 1989, -1):
        for item in manudir:
            man.append(item + str(i))
    return man

#Notkun: inflation = calcInflation(f,t,d)
#Fyrir: from<=too ef default=false
#Eftir: inflation er ver�b�lgan fr� from til too
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
#Fyrir: months er fj�ldi m�na�a sem vi� �tlum a� nota
#Eftir: x er ver�b�lgusp� reiknu� me�  v�sit�lum months marga m�nu�i aftur �
#       t�mann. �etta er me�altalssp�.
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