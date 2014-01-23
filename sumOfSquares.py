x=input("Enter a number: ");
smm=sqr=0;
for i in xrange(1,x+1):
	smm += i;
	sqr += i**2;
smm=smm**2;
print smm-sqr;
