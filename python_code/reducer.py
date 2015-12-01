f_read = open("./file/Fourgram_utf8_sort.txt","r")
f_write = open("Fourgram_Reduce.txt","w")

line = f_read.readline()

old_key = line.split("\t")[0]
new_key = ""
value_dict = {}
total = 0
average = 0 
difference = 0 

while True:
	if line == "" : break 
	new_key = line.split("\t")[0]
	if old_key != new_key:
		average = float(total) / float(len(value_dict))
		for item in value_dict:
			difference = difference+ ((average - value_dict[item])**2)
		difference = (difference / len(value_dict))**0.5
		#for item in value_dict:
		#	if value_dict[item] >= (average+difference):
		#		f_write.write(old_key+"\t"+ item.strip()+"\t"+str(value_dict[item])+"\n")
		for key, value in sorted(value_dict.iteritems(), reverse=True, key=lambda (k,v) : (v, k)):
			if value > (average+difference):
				f_write.write(old_key+"\t"+ key.strip()+"\t"+str(value)+"\n")
		value_dict = {}
		total  = 0 
		average = 0
		difference = 0
	old_key = new_key
	value = line.split("\t")[-1]
	if value in value_dict:
		value_dict[value] += 1
	else:
		value_dict[value] = 1
	total += 1
	line = f_read.readline()
f_write.close()
f_read.close()