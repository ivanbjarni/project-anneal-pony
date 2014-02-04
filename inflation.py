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
