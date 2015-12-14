#This code do the job that make maptable for chinese word to it's speech 
# coding: utf-8

# In[12]:

f_read = open("SBC4.txt","r")
f_write = open("Word_Speech_MapTable.txt","w")
line = f_read.readline()
dict_no_repeat ={}
now = 0

while True:
    if line == "" :break
    line = line.strip().split("|||")
    word_list = line[0].split("\t")
    speech_list = line[1].split("\t")
    if len(word_list)== len(speech_list):
	    for item_index in range(len(word_list)):
	    	if word_list[item_index] not in dict_no_repeat:
	        	f_write.write(word_list[item_index]+"\t"+speech_list[item_index]+"\n")
	        	dict_no_repeat[word_list[item_index]] = 1   
    line = f_read.readline()
    now += 1
    print now

f_read.close()
f_write.close()


# In[ ]:



