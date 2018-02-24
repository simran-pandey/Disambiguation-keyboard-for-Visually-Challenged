#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\replace\\output.txt','r')#Updated Corpus file 
f2 = open('C:\\Users\simran pandey\\Desktop\\IDC\\replace\\char.txt','w')# File containing the unicode representation of words in above file
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
		if (line[i]== '\xe0'and line[i+1] =='\xa4'and line[i+2] == '\x96') or (line[i]== '\xe0'and line[i+1] =='\xa4'and line[i+2] == '\x97')or(line[i]== '\xe0'and line[i+1] =='\xa4'and line[i+2] == '\x98') or (line[i]== '\xe0'and line[i+1] =='\xa4'and line[i+2] == '\x99'):# if the word is 'ख,ग, घ,ङ'  
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\x95'# then replacing by 'क'  the unicode for 'क' is '\xe0''\xa4' '\xaf'
# This block serves as example for replacing 'ख,ग, घ,ङ'  by 'क' ; similarily all replacement according to model can be done			
#=============================================================================================			
for word in characters:# storing array after replacement in file f3
	f3.write("%s" % word)	
	f3.write('\n')
f2.close()		
f3.close()			