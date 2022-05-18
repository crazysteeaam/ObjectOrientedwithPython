import nltk
filename = "2009-Obama.txt"
with open(filename,"r") as f:
    raw = f.read()
    tokenizer = nltk.RegexpTokenizer('[a-zA-Z]\w+\'?\w*')
    tokens = tokenizer.tokenize(raw) #分词，去掉标点符号
    text = nltk.Text(tokens)  #创建Text对象
    tokens = [ token.lower() for token in tokens] #转换为小写
    stemmer = nltk.LancasterStemmer() 
    tokens = [ stemmer.stem(token) for token in tokens] #提起词干
    stopwords = nltk.corpus.stopwords.words('english') #去掉停词
    content = [w for w in text if w.lower() not in stopwords]
    fdist = nltk.FreqDist(content) #创建FreqDist对象
    print("频率最高的10个单词：",fdist.most_common(10)) #输出前10个频率最高的词
    fdist.plot(50, cumulative=True)
