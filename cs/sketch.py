import sys
from vector import Vector
class Sketch:
    """计算文本text的k-grams的文档摘要向量（d维）"""
    def __init__(self, text, k, d):
        """初始化函数：计算文本text的文档摘要向量"""
        freq = [0 for i in range(d)] #创建长度为d的列表，初始值0
        for i in range(len(text) - k): #循环抽取k-grams，计算频率
            kgram = text[i:i+k]
            freq[hash(kgram) % d] += 1
        vector = Vector(freq) #创建文档摘要向量
        self._sketch = vector.direction() #归一化并赋值给对象实例变量
        
    def similarTo(self, other):
        """比较两个文档摘要对象Sketch的余弦相似度"""
        return self._sketch.dot(other._sketch)
    
    def __str__(self):
        return str(self._sketch)
    
#测试代码
def main():
    with open("tomsawyer.txt","r") as f:
        text = f.read()
        sketch = Sketch(text, 5, 100)
        print(sketch)
    
if __name__ == '__main__': main()
