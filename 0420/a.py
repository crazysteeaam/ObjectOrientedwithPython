import math


class Vector:
    def __init__(self, a):
        self._coords = a[:]
        self._n = len(a)

    def __getitem__(self, i):
        return self._coords[i]

    def __add__(self, other):
        result = []
        for i in range(self._n):
            result.append(self._coords[i] + other._coords[i])
        return Vector(result)

    def __sub__(self, other):
        result = []
        for i in range(self._n):
            result.append(self._coords[i] - other._coords[i])
        return Vector(result)

    def scale(self, n):
        result = []
        for i in range(self._n):
            result.append(self._coords[i] * n)
        return Vector(result)

    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    def __abs__(self):
        return math.sqrt(self.dot(self))

    def direction(self):
        return self.scale(1.0 / abs(self))

    def __str__(self):
        return str(self._coords)

    def __len__(self):
        return self._n


if __name__ == '__main__':
    xCoords = [2.0, 3.0, 2.0]
    yCoords = [5.0, 5.0, 0.0]
    x = Vector(xCoords)
    y = Vector(yCoords)
    print('x={},y={}'.format(x, y))
    print('x+y={}'.format(x + y))
    print('10x={}'.format(x.scale(10.0)))
    print('|x|={}'.format(abs(x)))
    print('<x,y>={}'.format(x.dot(y)))
    print('|x-y|={}'.format(abs(x - y)))
