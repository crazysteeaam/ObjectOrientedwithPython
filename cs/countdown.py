import time
def countdown(n):
    """从n倒计数到0"""
    if n <= 0: #基本情况
        print("时间到！！！")
    else: #递归步骤
        time.sleep(1) #睡眠1秒钟
        print(n) #输出倒数的数字
        countdown(n-1) #递归调用

if __name__ == "__main__":
    countdown(3)
