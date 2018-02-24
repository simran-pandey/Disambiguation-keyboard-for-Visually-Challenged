f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\dictionary\\dictionary.txt','r')# File containing the unicode representation of words in above file
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\dictionary\\result1.txt','w')
f4 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\dictionary\\counterpure.txt','w')
freq=[]
dictionary=[]
counter=[]
pure=[]
for word in f2:
	line, b = word.split( )
	dictionary.append(line)#array for word
	line = line.replace('\xe0\xa5\x80','')
	line = line.replace('\xe0\xa5\x81','')
	line = line.replace('\xe0\xa5\x82','')
	line = line.replace('\xe0\xa5\x87','')
	line = line.replace('\xe0\xa5\x88','')
	line = line.replace('\xe0\xa5\x8b','')
	line = line.replace('\xe0\xa5\x8c','')
	line = line.replace('\xe0\xa4\xbe','')
	line = line.replace('\xe0\xa4\xbf','')
	line = line.replace('\xe0\xa4\x82','')
	line = line.replace('\xe0\xa4\x83','')
	line = line.replace('\xe0\xa4\x81','')
	pure.append(line)
for line1 in pure:
	count=0
	for line2 in pure: 
		if line1 == line2:
			count=count+1
	counter.append(count)	
for line in pure:	
	f3.write(line)
	f3.write('\n')
for word in counter: # storing array after replacement in file f3
    f4.write("%s" % word)	
	f4.write('\n')		