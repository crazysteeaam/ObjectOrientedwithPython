import random

def gamble(stake, goal, trials):
    """返回输掉stake所需要的次数，模拟仿真trials次取平均值"""
    bets = 0      #总下注次数
    wins = 0      #赢的次数
    for t in range(trials):#模拟trials次取平均
        cash = stake  #筹码
        #持续下注直到破产，或达到目标退场
        while cash > 0 and cash < goal:
            #模拟一次下注
            bets += 1
            if random.randrange(0, 2) == 0:
                cash += 1
            else: cash -= 1
        if cash >= goal: wins += 1 #赢的次数 
    return wins/trials, int(bets/trials)
        
if __name__ == "__main__":
    p, n = gamble(10,20,100)
    print("{}赢{}的概率{}%，平均下注次数{}".format(10,20,p*100,n))
    p, n = gamble(10,1000,100)
    print("{}赢{}的概率{}%，平均下注次数{}".format(10,1000,p*100,n))
