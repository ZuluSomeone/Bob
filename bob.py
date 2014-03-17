def findbiggest(a,b):
        if(a>b):
             return a
        else:
             return b 

print findbiggest(2,4)
print findbiggest(666,99)

def findbiggest(a,b,c):
	if(a>b and a>c):
			return a
	else:
		if(b>a and b>c):
				return b	
		else:
			return c

print findbiggest(2,6,9)


for i in range (1,5000001):
	print i
