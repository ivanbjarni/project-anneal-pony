import math
golden = input("What kinda' Apples do you like? \n")
primes = [];
cnt = 0;
for i in xrange(2,golden+1):
	fail = 0;
	for a in primes :
		if a>math.sqrt(golden):
			break;
		if i%a==0:
			fail=1;
			break;
	if fail==0:
		primes.append(i);
		cnt+=i;

print cnt;
