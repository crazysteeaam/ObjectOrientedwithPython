import time


def countdown(n):
    if n <= 0:
        print("时间到！！！")
    else:
        time.sleep(1)
        print(n)
        countdown(n-1)


if __name__ == "__main__":
    countdown(3)
