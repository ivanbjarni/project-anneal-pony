# Notkun: x = calcLoan(b,p,int,inf,t)
# Fyrir: b er innistaeda/hofudstoll lans
#		p er greidsla a timaeiningu
#		int eru vextir a grundvelli timaeiningar
#		inf er verdbolga a grundvelli timaeiningar
#		t er fjoldi timaeininga
# Eftir: x er innistaeda/hofudstoll sem eftir er af lani
def calcLoan(balance, payment, interest, inflation, time):
	
	for i in xrange(0,time):
		balance -= payment
		balance = balance*(1+interest)

	return balance


def calcInterest(balance, interest, time):
	return balance * (1+interest)**time

def median(li):
	s = 0
	c = 0
	for i in li:
		s += i
	return s/c

print calcLoan(250000,10000,0.02,0,9)
print calcLoan(250000,0,0.02,0,9)