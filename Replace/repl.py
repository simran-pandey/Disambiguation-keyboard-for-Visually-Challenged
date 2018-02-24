#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\Users\simran pandey\Desktop\IDC\replace\output.txt','r')#Updated Corpus file 
f2 = open('C:\Users\simran pandey\Desktop\IDC\replace\char.txt','w')# File containing the unicode representation of words in above file
f3 = open('C:\Users\simran pandey\Desktop\IDC\replace\char_replaced.txt','w')## File containing the unicode representation of words after replacement
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
#===============================================REPLACING====================================	
for line in characters:# for every word in stored in the  array named characters
	for i in xrange(len(line)):
		if line[i]== '\xe0'and line[i+1] =='\xa4' and line[i+2] == '\xb0':# if the word is 'र'  the unicode for 'र' is '\xe0''\xa4' '\xb0'
			line[i]= '\xe0' 
			line[i+1]= '\xa4'
			line[i+2]= '\xaf'# then replacing 'र' by 'य'  the unicode for 'य' is '\xe0''\xa4' '\xaf'
# This block serves as example for replacing 'र' by 'य' ; similarily all replacement according to model can be done			
#=============================================================================================			
for word in characters:# storing array after replacement in file f3
	f3.write("%s" % word)	
	f3.write('\n')
f2.close()		
f3.close()			