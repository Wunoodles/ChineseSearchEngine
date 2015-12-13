# This code do the job that get all sequentiall pattern with length 2 
import operator
f_read = open("Sequence_Pattern.txt","r")
f_write = open("Valuable_Sequence_Pattern.txt","w")

line = f_read.readline().strip()
big_dict = {}

now = 0
while True: 
	if line == "": break
	a = line.split("->")[0].split(" ")
	if len(a) == 1 :
		if line not in big_dict:
			big_dict[line] = 1
		else:
			big_dict[line] += 1
	line = f_read.readline().strip()
	now += 1
	print now
f_read.close()
	
for key, value in sorted(big_dict.iteritems(), key=lambda (k,v): (v,k),reverse= True):
 
 	f_write.write(key+"\t"+str(value)+"\n")

f_write.close()