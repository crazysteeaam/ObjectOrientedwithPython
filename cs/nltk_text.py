import nltk
filename = "2009-Obama.txt"
with open(filename,"r") as f:
    raw = f.read()
    tokens = nltk.word_tokenize(raw) #分词
    text = nltk.Text(tokens)  #创建Text对象
    print("总单词数：{}".format(len(text)))
    distinct_words=set(text)
    print("词汇量：{}".format(len(distinct_words)))
    long_words = [w for w in distinct_words if len(w) > 15]
    print("字符超过15的单词表：{}".format(long_words))
    w = "America"
    print("{}出现的次数{}".format(w, text.count(w)))
    print(text.concordance(w)) #显示25个包含w="America"的上下文
    print(text.similar(w)) #显示"good"的相似词
    print(text.common_contexts(["America","government"])) #
    text.dispersion_plot(["America","government"])
