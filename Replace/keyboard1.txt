#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\input.txt','r')#Updated Corpus file 
f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\result.txt','w')# File containing the unicode representation of words in above file
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\char_replaced.txt','r')## File containing the unicode representation of words after replacement
f4 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\counter.txt','w')
f5 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\output.txt','r')
input = []
freq= []
incharacters= []
characters= []
counter= []
dictionary = []
freq= []
characters= []
counter= []
for line in f5:
    a , b = line.split( )
    dictionary.append(a)#array for word
    freq.append(b)#array for frequency
for word in dictionary:
	c=list(word) #converting to unicode
	characters.append(c)#storing unicode to array named characters
#===============================================REPLACING'====================================	
for line in characters:# for every word in stored in the  array named characters
	for i in xrange(len(line)):
		if line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\x96') or (line[i+2] == '\x97')or(line[i+2] == '\x98') or (line[i+2] == '\x99')):# if the word is 'ख,ग, घ,ङ'  
			line[i+2]= '\x95'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\x9b') or (line[i+2] == '\x9c')or(line[i+2] == '\x9d') or (line[i+2] == '\x9e')):
			line[i+2]= '\x9a'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xa0') or (line[i+2] == '\xa1')or(line[i+2] == '\xa2') or (line[i+2] == '\xa3')):
			line[i+2]= '\x9f'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xa5') or (line[i+2] == '\xa6')or(line[i+2] == '\xa7') or (line[i+2] == '\xa8')):
			line[i+2]= '\xa4'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xab') or (line[i+2] == '\xac')or(line[i+2] == '\xad') or (line[i+2] == '\xae')):
			line[i+2]= '\xaa'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xb0') or (line[i+2] == '\xb2')or(line[i+2] == '\xb5') or (line[i+2] == '\xb6')):
			line[i+2]= '\xaf'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xb8') or (line[i+2] == '\xb9')):
			line[i+2]= '\xaf'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\x86') or (line[i+2] == '\x87')or(line[i+2] == '\x88')or (line[i+2] == '\x89')or (line[i+2] == '\x8a')or (line[i+2] == '\x8b')or (line[i+2] == '\x8f')or (line[i+2] == '\x90')or (line[i+2] == '\x93') or (line[i+2] == '\x94')):
			line[i+2]= '\x85'	
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xbe') or (line[i+2] == '\xbf')):
			line[i+2]= '\x85'
		elif line[i]== '\xe0'and line[i+1] =='\xa5'and((line[i+2] == '\x80') or (line[i+2] == '\x81') or (line[i+2] == '\x82') or (line[i+2] == '\x83') or (line[i+2] == '\x84') or (line[i+2] == '\x85') or( line[i+2] == '\x86') or (line[i+2] == '\x87')or(line[i+2] == '\x88')or (line[i+2] == '\x89')or (line[i+2] == '\x8a')or (line[i+2] == '\x8b')or (line[i+2] == '\x8f')or (line[i+2] == '\x90')or (line[i+2] == '\x93') or (line[i+2] == '\x94')):
			line[i+1]='\xa4'
			line[i+2]= '\x85'			
# for word in f3:
	# characters.append(word)#storing unicode to array named characters
for line in f1:
    input.append(line)#array for word
    #freq.append(b)#array for frequency
for word in input:
	c=list(word) #converting to unicode
	incharacters.append(c)#storing unicode to array named characters	
#===============================================REPLACING'====================================	
for line1 in incharacters:
	c=len(line1)-3
	i=0
	for line2 in characters: 
		i=i+1
		if line1[3:len(line1)] == line2[0:len(line1)-3]:
			save=dictionary[i-1]
			f2.write(save)
			f2.write('\n')		
f2.close()			
