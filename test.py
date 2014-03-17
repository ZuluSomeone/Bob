minfil=open('majs.txt','w')

for k in range (1,10):
  s = '%5d' %(k)
  minfil.write(s)
minfil.close()
