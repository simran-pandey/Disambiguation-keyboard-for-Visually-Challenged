import re
import unicodedata
f1 = open('C:\Users\Akshay\Desktop\IDC\output.txt','r')
f2 = open('C:\Users\Akshay\Desktop\IDC\hindic.txt','w')
freq= []
dictionary = []
for line in f1:
    a , b = line.split( )
    dictionary.append(a) 
    freq.append(b)
	
dict_sort=sorted(dictionary)
answer = [unicode(item) for item in dict_sort]	
for word in dict_sort:
	f2.write(word)
	f2.write('\n')
	
f2.close()
