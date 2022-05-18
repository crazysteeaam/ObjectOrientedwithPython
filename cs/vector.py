import math
class Vector:
    """笛卡尔坐标系向量"""
    
    def __init__(self, a):
        """构造函数：切片拷贝列表参数a到对象实例变量_coords"""
        self._coords = a[:]   # 坐标列表
        self._n = len(a)      # 维度

    def __getitem__(self, i):
        """返回第i个元素，即第i维坐标"""
        return self._coords[i]

    def __add__(self, other):
        """返回2个向量之和"""
        result = []
        for i in range(self._n):
            result.append(self._coords[i] + other._coords[i])
        return Vector(result)

    def __sub__(self, other):
        """返回2个向量之差"""
        result = []
        for i in range(self._n):
            result.append(self._coords[i] - other._coords[i])
        return Vector(result)

    def scale(self, n):
        """返回向量与数值的乘积差"""
        result = []
        for i in range(self._n):
            result.append(self._coords[i] * n)
        return Vector(result)

    def dot(self, other):
        """返回2向量的内积"""
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    def __abs__(self):
        """返回向量的模"""
        return math.sqrt(self.dot(self))

    def direction(self):
        """返回向量的单位向量"""
        return self.scale(1.0 / abs(self))

    def __str__(self):
        """返回向量的字符串表示"""
        return str(self._coords)
        
    def __len__(self):
        """返回向量的维度"""
        return self._n
        
#测试代码
def main():
    xCoords = [2.0, 2.0, 2.0]
    yCoords = [5.0, 5.0, 0.0]

    x = Vector(xCoords)
    y = Vector(yCoords)

    print('x = {}, y = {}'.format(x, y))
    print('x + y = {}'.format(x + y))
    print('10x = {}'.format(x.scale(10.0)))
    print('|x| = {}'.format(abs(x)))
    print('<x,y> = {}'.format(x.dot(y)))
    print('|x-y| = {}'.format(abs(x-y)))

if __name__ == '__main__': main()
