import nltk
filename = "tomsawyer.txt"
with open(filename,"r") as f:
    raw = f.read()
    print("总字符数：{}".format(len(raw)))
    tokens = nltk.word_tokenize(raw)
    print("总单词数：{}".format(len(tokens)))
    sentences = nltk.sent_tokenize(raw)
    print("总句子数：{}".format(len(sentences)))
