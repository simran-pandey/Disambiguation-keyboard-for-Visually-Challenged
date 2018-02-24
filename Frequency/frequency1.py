#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\corpus_5k.txt','r')# File containing the unicode representation of words in above file
f2 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\frequency.txt','w')
f3 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\elements.txt','w')
f4 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\input.txt','r')
freq=[]
dict=[]
dict_updated=[]
counter=[]
char=[]
unique=[]
words=[]
input=[]
for word in f1:
	line,fre=word.split()
	freq.append(fre)
	dict.append(line)#array for word
	line = line.replace('\xe0','&\xe0')
	dict_updated.append(line)
for line in dict_updated:
	words = words + line.split('&')	
for line in f4:
	line1=list(line)
	unique.append(line1)
	input.append(line)
for line in words:
	line=list(line)
	char.append(line)
	f3.write("%s" % line)
	f3.write('\n')
x=0	
for line1 in unique:
	x=x+1
	f2.write("%s" % input[x-1])
	count =0
	for line2 in char:
		if line1[0:len(line1)-1]==line2:
			count=count+1
	counter.append(count)
	f2.write("%s" % count)
	f2.write('\n')		
			


	
	