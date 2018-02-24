#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\output.txt','r')#Updated Corpus file 
f2 = open('C:\\Users\simran pandey\\Desktop\\IDC\\replace\\rchar.txt','w')# File containing the unicode representation of words in above file
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\char_replaced.txt','w')## File containing the unicode representation of words after replacement
dictionary = []
freq= []
characters= []
for line in f1:
    a , b = line.split( )
    dictionary.append(a)#array for word
    freq.append(b)#array for frequency
for word in dictionary:
	c=list(word) #converting to unicode
	characters.append(c)#storing unicode to array named characters
for word in characters:
	f2.write("%s" % word)# saving array named characters to file f2	
	f2.write('\n')
#===============================================REPLACING 'ख,ग, घ,ङ'  by 'क'====================================	
for line in characters:# for every word in stored in the  array named characters
	for i in xrange(len(line)):
		if line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\x96') or (line[i+2] == '\x97')or(line[i+2] == '\x98') or (line[i+2] == '\x99')):# if the word is 'ख,ग, घ,ङ'  
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\x95'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\x9b') or (line[i+2] == '\x9c')or(line[i+2] == '\x9d') or (line[i+2] == '\x9e')):
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\x9a'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xa0') or (line[i+2] == '\xa1')or(line[i+2] == '\xa2') or (line[i+2] == '\xa3')):
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\x9f'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xa5') or (line[i+2] == '\xa6')or(line[i+2] == '\xa7') or (line[i+2] == '\xa8')):
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\xa4'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xab') or (line[i+2] == '\xac')or(line[i+2] == '\xad') or (line[i+2] == '\xae')):
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\xaa'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xb0') or (line[i+2] == '\xb2')or(line[i+2] == '\xb5') or (line[i+2] == '\xb6')):
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\xaf'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\xb8') or (line[i+2] == '\xb9')):
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\xaf'
		elif line[i]== '\xe0'and line[i+1] =='\xa4'and(( line[i+2] == '\x86') or (line[i+2] == '\x87')or(line[i+2] == '\x88')or (line[i+2] == '\x89')or (line[i+2] == '\x8a')or (line[i+2] == '\x8b')or (line[i+2] == '\x8f')or (line[i+2] == '\x90')or (line[i+2] == '\x93') or (line[i+2] == '\x94')):
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\x85'
			
			
			
			# then replacing by 'क'  the unicode for 'क' is '\xe0''\xa4' '\xaf'
			
#=============================================================================================			
for word in characters:# storing array after replacement in file f3
	f3.write("%s" % word)	
	f3.write('\n')
f2.close()		
f3.close()			