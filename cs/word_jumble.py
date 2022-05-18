#模块：c:\pythonpa\cs\word_jumble.py
import random
#建立英文单词库，以元组的形式表示
WORDS = ['apple','pear','banana','cherry','good','better','best',
         'python','while','tuple','dictionary','jumble','difficult',
         'aesthetic','stereotype','civilization','anniversary']
print("欢迎参加猜单词游戏!\n请把乱序后的字母组成一个单词\n")
isContinue = "Y"
while isContinue in ("Y", "y"):
    #随机挑选一个单词
    word = random.choice(WORDS)
    answer = word  #保存答案
    #将选出的单词进行乱序
    jumble = ""
    for i in word:
        #随机抽取一个位置的字符放入乱序jumble中，并从原word中删除该字符
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position+1):]
    #输出乱序后的单词
    print("乱序后的单词：", jumble)
    #接受玩家猜的单词
    guess = input("请输入您猜测的结果：")
    while guess != answer:
       guess = input("结果不对，请重新猜测：")
    print("恭喜您，猜对了！")
    #询问是否重复游戏
    isContinue = input("是否继续(Y/N)?")
print("谢谢参与，欢迎下次再玩！")
