golden = input("What kinda' Apples do you like?\n")

for a in xrange(0,golden):
	for b in xrange(a,golden-a):
		c = golden - a -b ;
		if(a**2+b**2-c**2==0):
			print str(a*b*c);
