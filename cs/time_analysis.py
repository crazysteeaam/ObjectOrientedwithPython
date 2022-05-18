import time
import random
def timing(f, data):
    """测量函数调用f(data)的运行时间分析"""

    start = time.time() #记录开始时间
    f(data)             #运行f(data)
    end = time.time()   #记录结束时间
    return end - start  #返回执行时间

def timingAnalysis(f, m1, m2, runs, buildData):
    """输出函数f在不同输入规模：10**m1,...,10**m2运行runs次的时间"""

    for n in [10**i for i in range(m1, m2+1)]:  #10**m1,...,10**m2
        data = buildData(n)
        total = 0.0  #初始化总时间
        for i in range(runs): #重复运行runs次
            total += timing(f, data) #运行f并累计运行时间
        strResult = '输入规模{:10}时函数{:10}运行{}次的平均时间为:{}秒.'
        print(strResult.format(n, f.__name__, runs, total/runs))

def buildData(n):
    """构造测试规模为n的输入数据，对于排序，随机n个数的列表"""
    data = [random.randrange(n) for i in range(n)]
    return data
    
#测试代码
if __name__ == "__main__":
    from bubbleSort import bubbleSort
    from selectionSort import selectionSort
    from insertSort import insertSort
    from mergeSort import mergeSort
    from quickSort import quickSort
    def quickSort1(a):
        quickSort(a, 0, len(a)-1)
    #冒泡排序算法时间复杂度分析
    timingAnalysis(bubbleSort, 2, 4, 1, buildData)
    #选择排序算法时间复杂度分析
    timingAnalysis(selectionSort, 2, 4, 1, buildData)
    #插入排序算法时间复杂度分析
    timingAnalysis(insertSort, 2, 4, 1, buildData)
    #归并排序算法时间复杂度分析
    timingAnalysis(mergeSort, 1, 4, 1, buildData)
    #快速排序算法时间复杂度分析
    timingAnalysis(quickSort1, 1, 4, 1, buildData)
    #内置排序算法sort时间复杂度分析
    timingAnalysis(sorted, 1, 4, 1, buildData)
    
