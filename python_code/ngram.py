# -*- coding: utf8 -*-
f_read = open("SBC4.txt","r")
f_write_bigram = open("Bigram.txt","w")
f_write_trigram = open("Trigram.txt","w")
f_write_fourgram = open("Fourgram.txt","w")

line = f_read.readline().split("||")[0].decode("utf8").split("\t")


while True:
    if line == "": break
    for i_string in line:
        if len(i_string) > 1:
            f_write.write(i_string [0].encode("utf8")+"\t"+ i_string[1:].encode("utf-8")+"\n")
    		if len(i_string) > 2 :
    			 f_write_trigram.write(i_string [0:2].encode("utf8")+"\t"+ i_string[2:].encode("utf-8")+"\n")
    			 if len(i_string) > 3 :
    			 	 f_write_fourgram.write(i_string [0:3].encode("utf8")+"\t"+ i_string[3:].encode("utf-8")+"\n")
    line = f_read.readline().split("||")[0].decode("utf8").split("\t")

f_write_bigram.close()
f_write_trigram.close()
f_write_fourgram.close()
f_read.close()
