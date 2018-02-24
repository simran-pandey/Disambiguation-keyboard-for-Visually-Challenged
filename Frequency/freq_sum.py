f1 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\counter.txt','r')
f2 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\corpus_1k.txt','r')
f3 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\temp.txt','w')
f5 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\freq_count.txt','w')
freq=[]
frequency=[]
counter=[]
for line in f1:
	counter.append(int(line))
for line in f2:
	a,b=line.split()
	freq.append(int(b))
	d=max(counter)
for i in xrange(0,d):
	f3.write(str(0))
	f3.write('\n')
f3.close()
	
f4 = open('C:\\Users\\pande\\Desktop\\IDC\\frequency\\temp.txt','r')	
for line in f4:
	frequency.append(int(line))
i=0	
for line in counter:
	i=i+1
	frequency[int(line)-1]=frequency[int(line)-1]+freq[i-1]
i=0	
for line in frequency:
	f5.write(str(i)+ '=' + str(line))	
	f5.write('\n')
	i=i+1
	
		
	

	