import re
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\hindidict.txt','r')
f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\corpus_15k.txt' , 'r')
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\out.txt','w')
f4 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\output.txt','w')
dictionary = []
freq= []
words = []
wiki=[]
for line in f2:
    a , b = line.split( )
    dictionary.append(a)
    freq.append(b)
for line in f1:
	words = words + line.split()
words = set(words)
for word in words:
	f3.write(word)
	f3.write('\n')
f3.close()
f5 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\disambiguation\\out.txt','r')

for i in xrange(len(dictionary)):
	if dictionary[i] in words:
		f4.write(dictionary[i])
		f4.write(" ")
		f4.write(freq[i])
		f4.write('\n')

f4.close()
