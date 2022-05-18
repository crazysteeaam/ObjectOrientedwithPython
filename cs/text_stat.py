import re
import collections
def analyze_text(text):
    paragraphs = re.split("\n\n", text)
    paragraph_count = len(paragraphs)
    print("段落数：{0}".format(paragraph_count))
    lines = re.split("\n", text)
    line_count = len(lines)
    print("行数：{0}".format(line_count))
    sentences = re.split("[.?!]", text)
    sentence_count = len(sentences)
    print("句数：{0}".format(sentence_count))
    words = re.split(r"\W+", text)
    word_count = len(words)
    print("单词数：{0}".format(word_count))
    freqs = collections.Counter(words)
    print("频率最高的10个单词：")
    for (w, n) in freqs.most_common(10):
        print("{0:10}:{1:10}".format(w, n))

if __name__ == "__main__":
    filename = "tomsawyer.txt"
    with open(filename,"r") as f:
        text = f.read()
    analyze_text(text.strip())

