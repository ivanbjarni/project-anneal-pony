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
