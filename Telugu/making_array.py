import re
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\telugu\\sorted_matched_1.txt','r')#Wiki file
f3 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\telugu\\wiki_array.txt','w')#unique words in wiki
words = []
wiki=[]
counter= 0

for line in f1:#for every line in wiki corpus
	words = words + line.split()#split a string into a list
words = set(words)#return unique words from the text file
for word in words:
	f3.write(word)#writing unique words to file out
	f3.write('\n')
	counter = counter+1
	print counter
f3.close()

