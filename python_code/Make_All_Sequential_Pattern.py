#This code do the job that get all sequentiall pattern with all length 
f_read = open("SBC4.txt","r")
f_write = open("Sequence_Pattern.txt","w")
line = f_read.readline()
while True:
	if line == "": break
	line_handle = line.split("|||")[-1].strip().split("\t")
	for index_i in range(len(line_handle)):
		for index_j in range(index_i+1,len(line_handle)):
			f_write.write(line_handle[index_i])
			for each_item in line_handle[index_i+1:index_j]:
				f_write.write(" "+each_item)
			f_write.write("->"+line_handle[index_j]+"\n")
	line = f_read.readline()

f_read.close()
f_write.close()
