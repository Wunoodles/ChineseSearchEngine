# -*- coding: utf8 -*-
def Collocation(input_key):
	f_read = open("./datasource/Bigram_Reduce.txt","r")
	line = f_read.readline()
	time = 0
	key = ""
	output = []
	while True:
		if line == "" : break
		key = line.split("\t")[0]
		if key == input_key:
			output.append(line.split("\t")[1])
			time += 1
			if time == 5:
				break
		line = f_read.readline()
	f_read.close()
	#無法直接輸出中文的list
	return ",".join(output)  #輸出是所有結果用逗號隔開

def Give_Word_Speech(word):
    f_read = open("./datasource/word_POS.txt","r")
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
    f_read = open("./datasource/Pattern_sorted_reduce.txt","r")
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
#
# def n_gram(word,len):
# 	if(len == 1):
# 		f_read = open("./datasource/ngram/word_bigram_and_support","r")
#
#     line = f_read.readline()
#     while True:
#         if line == "" :
#             f_read.close()
#             return 'N'
# 		pattern , count = line.split("\t")
#         key, speech = line.split("->")
#         if key == word:
#             f_read.close()
#             return speech
#         line = f_read.readline()
