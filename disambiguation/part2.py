#-*- coding: utf-8 -*-
import unicodedata
# a='की'
# b=list(a)
# print b
f1 = open('C:\Users\simran pandey\Desktop\IDC\disambiguation\output.txt','r')
f2 = open('C:\Users\simran pandey\Desktop\IDC\disambiguation\char.txt','w')
dictionary = []
freq= []
characters= []
wiki=[]
for line in f1:
    a , b = line.split( )
    dictionary.append(a)
    freq.append(b)
for word in dictionary:
	c=list(word)
	characters.append(c)
# e=len(characters)
# print characters
for word in characters:
	f2.write("%s\n" % word)	
#	f2.write(str1)
	f2.write('\n')
f2.close()
	
