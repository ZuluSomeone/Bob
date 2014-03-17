minfil=open('Desktop/Data.dat','r')
while 1: # infinte loop
   s = minfil.readline()
   if s ==":
        break
   m = int(s)
   print m * 5
f.close()
