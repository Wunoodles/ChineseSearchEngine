
# coding: utf-8
import jieba
def Judge_word_of_sentence(sen):
    if sen == "":
        return
    sen = sen.decode("utf-8")
    word_speech_list = []
    words = jieba.cut(sen, cut_all=False)
    for word in words:
        f_read = open("./datasource/word_POS.txt","r")
        line = f_read.readline()
#         print word
        a = word.encode('utf8')
        while True:
            if line == "": break
            key,speech = line.split('\t')
            if(a == key):
                s = key+'=>'+speech.strip()
                word_speech_list += [s]
#                 print key , speech
            line = f_read.readline()
    return list(word_speech_list)


def Recommendation(word_list):

    quatity = len(word_list)
    if quatity == 0:
        return
    key = []
    key = " ".join(word_list)
    # print key

    if quatity == 1:
        f_read = open("./datasource/bigram_classical.txt","r")
    elif quatity == 2:
        f_read = open("./datasource/trigram_classical.txt","r")
    elif quatity == 3:
        f_read = open("./datasource/fourgram_classical.txt","r")
    elif quatity == 4:
        f_read = open("./datasource/fivegram_classical.txt","r")
    else:
        f_read = open("./datasource/sixgram_classical.txt","r")

    line = f_read.readline()

    recommendation_list = []
    time = 0
    open_it = 0
    while True:
        if line == "": break
        file_key = line.split("\t")[0]
        if key == file_key :
            recommendation_list.append("\t".join(line.split("\t")[1:-1]))
            open_it = 1
        else:
            if open_it == 1:
                break

        line = f_read.readline()
    f_read.close()

    # for item in recommendation_list:
    #     print item
    #     print "\n"
    return recommendation_list


def Chinese_sentence_system(input_sentence):
    output_dict = {}
    output_dict["word"] = []
    output_dict["speech"] = []
    recommendation_speech_word = []

    word_and_speech = Judge_word_of_sentence(input_sentence)

    for item in word_and_speech:
        output_dict["word"].append(item.split("=>")[0])
        output_dict["speech"].append(item.split("=>")[1])
    answer = Recommendation(output_dict["word"])
    # print answer
    for item in answer:
        for item_item in item.split("\t")[1:]:
            recommendation_speech_word.append( [item_item+"( "+item.split("\t")[0]+" )"] )
            # recommendation_speech_word.append( [item.split("\t")[0]+" => "+item_item] )
    output_dict["recommendation_speech_word"] = recommendation_speech_word
    return output_dict
