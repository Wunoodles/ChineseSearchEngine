# -*- coding: utf8 -*-
def Collocation(input_key):
	f_read = open("./datasource/Bigram_Reduce.txt","r")
	line = f_read.readline()
	key = ""
	output = []
	while True:
		if line == "" : break
		key = line.split("\t")[0]
		if key == input_key:
			output.append(line.split("\t")[1])
		line = f_read.readline()
	f_read.close()
	#無法直接輸出中文的list
	return ",".join(output)  #輸出是所有結果用逗號隔開
	