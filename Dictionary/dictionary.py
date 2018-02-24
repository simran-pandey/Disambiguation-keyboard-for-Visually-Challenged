f2 = open('C:\\Users\\simran pandey\\Desktop\\dictionary\\output_56k.txt','r')# File containing the unicode representation of words in above file
f3 = open('C:\\Users\\simran pandey\\Desktop\\dictionary\\result1.txt','w')
f1 = open('C:\\Users\\simran pandey\\Desktop\\dictionary\\pureflat.txt','w')
f4 = open('C:\\Users\\simran pandey\\Desktop\\dictionary\\counterpure.txt','w')
freq=[]
dictionary=[]
counter=[]
pure=[]
for word in f2:
	line, b = word.split( )
	dictionary.append(line)#array for word
	freq.append(b)#array for word
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
count=0
x=0
for line1 in pure:
	x=x+1
	print x
	c=len(line1)
	i=0
	f1.write("%s" % line1)
	f1.write('\n')
	count=0
	for line2 in pure: 
		i=i+1
		if line1 == line2:#[0:len(line1)]:
			count=count+1	
			save1=dictionary[i-1]
			save2=freq[i-1]
			f1.write(save1 + '  ')
			f1.write(save2 + '  ')
			f1.write('\n')
	counter.append(count)
	f1.write("%s" % count)
	f1.write('\n')

for line in pure:	
	f3.write(line)
	f3.write('\n')
for word in counter:# storing array after replacement in file f3
	f4.write("%s" % word)	
	f4.write('\n')		