#!/usr/bin/env python
# encoding: utf-8
f1 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\dev.txt','r')# File containing the unicode representation of words in above file
f2 = open('C:\\Users\\simran pandey\\Desktop\\IDC\\unicode\\uni.txt','w')
for line in f1:
	line1=list(line)
	print line1
	f2.write("%s" % line1)