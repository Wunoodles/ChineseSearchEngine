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
	
def Give_Word_Speech(word):
    f_read = open("./datasource/Word_Speech_MapTable.txt","r")
    line = f_read.readline()
    while True:
        if line == "" :
            f_read.close()
            return 'N'                     
        key, speech = line.split("\t")
        if key == word:
            f_read.close()
            return speech
        line = f_read.readline()
    

def Recommendation(Input_Key):
    f_read = open("./datasource/Recommend_Pattern_Key_1.txt","r")
    answer_list = []
    turn = 0
    line = f_read.readline()
    while True:
        if line == "":
            f_read.close()
            return "No Recommendation!"
        key = line.split("\t")[0].split(" ")[0]
          
        if key == Input_Key:
            value = line.split("\t")[0].split(" ")[1:]
            answer_list.append(value)
            turn = 1
        if key !=Input_Key and turn != 0:
            return answer_list
        
        line = f_read.readline()