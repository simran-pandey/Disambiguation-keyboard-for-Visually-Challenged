#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\frequency\\corpus_w1.txt','r')# File containing the unicode representation of words in above file
f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\frequency\\frequency.txt','w')
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\frequency\\elements.txt','w')
freq=[]
dict=[]
dict_updated=[]
counter=[]
words=[]
for word in f1:
	line,fre=word.split()
	freq.append(fre)
	dict.append(line)#array for word
	line = line.replace('\xe0','&\xe0')
	dict_updated.append(line)
for line in dict_updated:
	words = words + line.split('&')	
unique=set(words)	
print len(unique)
for line in words:
	f3.write(line)
	f3.write('\n')
x=0	
for line1 in unique:
	x=x+1
	print x
	f2.write(line1)
	count =0
	for line2 in words:
		if line1==line2:
			count=count+1
	counter.append(count)
	f2.write("%s" % count)
	f2.write('\n')		
			


	
	