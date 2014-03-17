minfil=open('Desktop/prov.txt','w')   #This line creates a text document on the desktop

for k in range (1,11): #This line sets the range from 1-10
  s = '%5d\n' %(k) #This sets the spacing to 5 and makes it a list
  minfil.write(s)  #This writes it out
minfil.close()     #This closes it



minfil=open('Desktop/prov.txt','r') #This line opens the text document
print minfil.read() #This line reads the file and print it out
minfil.close() #This line closes it





