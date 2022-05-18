import os
def tree(path, level):
    #如果路径不存在，则返回None
    if not os.path.exists(path): return None
    #递归基本情况：如果是文件，则输出文件名
    if os.path.isfile(path):
        fileName = os.path.basename(path)
        print('\t' * level + '├─ ' + fileName)
    elif os.path.isdir(path): #递归情况
        print('\t' * level + '├─ ' + path)
        for item in os.listdir(path):
            tree(os.path.join(path, item), level + 1)

if __name__ == '__main__':
    tree(r"c:\pythonpa", 0)