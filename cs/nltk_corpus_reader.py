from nltk.corpus import gutenberg
print("{:25}{:10}{:10}{:10}".format("文件名","字符数","单词数","句子数"))
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    print("{:25}{:10}{:10}{:10}".format(fileid,num_chars,num_words,num_sents))
