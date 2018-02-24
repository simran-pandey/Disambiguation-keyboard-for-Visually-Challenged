#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\corpus_10k.txt','r')# File containing the unicode representation of words in above file
f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\replaced.txt','w')
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\result.txt','w')
f5 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\counter.txt','w')
f7 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\flatfile.txt','w')
freq=[]
dictionary=[]
counter=[]
dict=[]
pure=[]
for line in f1:
	dict.append(line)#array for word
	line = line.replace('\xe0\xa4\x96','\xe0\xa4\x95')#ख - क
	line = line.replace('\xe0\xa4\x97','\xe0\xa4\x95')#ग - क
	line = line.replace('\xe0\xa4\x98','\xe0\xa4\x95')#घ - क
	line = line.replace('\xe0\xa4\x99','\xe0\xa4\x95')#ङ - क
	
	line = line.replace('\xe0\xa5\x98','\xe0\xa4\x95')
	line = line.replace('\xe0\xa4\x99','\xe0\xa4\x95')
	line = line.replace('\xe0\xa4\x9a','\xe0\xa4\x95')
	
	line = line.replace('\xe0\xa4\x9b','\xe0\xa4\x9a')
	line = line.replace('\xe0\xa4\x9c','\xe0\xa4\x9a')
	line = line.replace('\xe0\xa4\x9d','\xe0\xa4\x9a')
	line = line.replace('\xe0\xa4\x9e','\xe0\xa4\x9a')
	
	line = line.replace('\xe0\xa5\x9b','\xe0\xa4\x9a')
	
	line = line.replace('\xe0\xa4\xa0','\xe0\xa4\x9f')
	line = line.replace('\xe0\xa4\xa1','\xe0\xa4\x9f')
	line = line.replace('\xe0\xa4\xa2','\xe0\xa4\x9f')
	line = line.replace('\xe0\xa4\xa3','\xe0\xa4\x9f')
	
	line = line.replace('\xe0\xa5\x9c','\xe0\xa4\x9f')
	line = line.replace('\xe0\xa5\x9d','\xe0\xa4\x9f')
	
	line = line.replace('\xe0\xa4\xa5','\xe0\xa4\xa4')
	line = line.replace('\xe0\xa4\xa6','\xe0\xa4\xa4')
	line = line.replace('\xe0\xa4\xa7','\xe0\xa4\xa4')
	line = line.replace('\xe0\xa4\xa8','\xe0\xa4\xa4')
	line = line.replace('\xe0\xa4\xa9','\xe0\xa4\xa4')
	
	line = line.replace('\xe0\xa4\xab','\xe0\xa4\xaa')
	line = line.replace('\xe0\xa4\xac','\xe0\xa4\xaa')
	line = line.replace('\xe0\xa4\xad','\xe0\xa4\xaa')
	line = line.replace('\xe0\xa4\xae','\xe0\xa4\xaa')
	
	line = line.replace('\xe0\xa5\x9e','\xe0\xa4\xaa')
	
	line = line.replace('\xe0\xa4\xb0','\xe0\xa4\xaf')
	line = line.replace('\xe0\xa4\xb1','\xe0\xa4\xaf')
	line = line.replace('\xe0\xa4\xb2','\xe0\xa4\xaf')
	line = line.replace('\xe0\xa4\xb5','\xe0\xa4\xaf')
	line = line.replace('\xe0\xa4\xb6','\xe0\xa4\xaf')
	
	line = line.replace('\xe0\xa5\x9f','\xe0\xa4\xaf')
	
	line = line.replace('\xe0\xa4\xb8','\xe0\xa4\xb7')
	line = line.replace('\xe0\xa4\xb9','\xe0\xa4\xb7')
	
	line = line.replace('\xe0\xa4\xbf','\xe0\xa4\x80')
	line = line.replace('\xe0\xa5\x80','\xe0\xa4\x80')
	
	line = line.replace('\xe0\xa5\x81','\xe0\xa4\x82')
	line = line.replace('\xe0\xa5\x82','\xe0\xa4\x82')
	
	line = line.replace('\xe0\xa4\x87','\xe0\xa4\x88')
	line = line.replace('\xe0\xa5\x88','\xe0\xa5\x88')#group2
	
	line = line.replace('\xe0\xa5\x8b','\xe0\xa5\x8c')
	line = line.replace('\xe0\xa5\x8c','\xe0\xa5\x8c')
	
	line = line.replace('\xe0\xa5\x8c','\xe0\xa5\x80')
	line = line.replace('\xe0\xa4\x83','\xe0\xa5\x80')

	line = line.replace('\xe0\xa4\x86','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x87','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x88','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x89','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x8a','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x8b','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x8f','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x90','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x93','\xe0\xa4\x85')
	line = line.replace('\xe0\xa4\x94','\xe0\xa4\x85')
	
	#dicriatic
	line = line.replace('\xe0\xa4\x81','\xe0\xa4\x81')#chandrabindu
	line = line.replace('\xe0\xa5\x84','\xe0\xa4\x81')
	line = line.replace('\xe0\xa5\x86','\xe0\xa4\x81')
	line = line.replace('\xe0\xa5\x89','\xe0\xa4\x81')
	line = line.replace('\xe0\xa5\x8a','\xe0\xa4\x81')
	line = line.replace('\xe0\xa5\xa4','\xe0\xa4\x81')
	line = line.replace('\xe0\xa5\xb2','\xe0\xa4\x81')
	line = line.replace('\xe0\xa4\xbd','\xe0\xa4\x81')
	line = line.replace('\xe0\xa4\x91','\xe0\xa4\x81')
	line = line.replace('\xe0\xa5\x8d','\xe0\xa4\x81')
	
	pure.append(line)
for line in pure:
	f2.write(line)
f2.close()
f4 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\replaced.txt','r')	
dictionary = []
freq= []
characters= []
counter= []
for line in f4:
    a , b = line.split( )
    dictionary.append(a)#array for word
    freq.append(b)#array for frequency
for word in dictionary:
	c=list(word) #converting to unicode
	characters.append(c)#storing unicode to array named characters
x=0			
for line1 in characters:
	x=x+1
	print x
	c=len(line1)
	i=0
	save=dictionary[x-1]
	f7.write("%s" % save)
	f7.write('\n')
	count=0
	for line2 in characters: 
		#print line2
		i=i+1
		if line1 == line2:
			save1=dict[i-1]
			#save2=freq[i-1]
			f7.write(save1 + '  ')
			#f7.write(save2 + '  ')
			#f7.write('\n')
			count=count+1
	counter.append(count)
	f7.write("%s" % count)
	f7.write('\n')		
for word in counter:# storing array after replacement in file f3
	f5.write("%s" % word)	
	f5.write('\n')	
f5.close()		
			
