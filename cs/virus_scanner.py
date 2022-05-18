import os
virus_sig = {'lovebug':'xy5020g2h1azzx33', 'Blaster':'fdp3014k1ks6hgbc'}
def scan(path, virus_sig):
    """扫描文件夹path及其子文件夹中的所有文件，判断是否包含特征码"""
    if os.path.isfile(path):  #基本情况，打开文件，查找特征码
        infile = open(path)
        content = infile.read()
        infile.close()

        for virus in virus_sig:
            # 检查文件内容是否包含特征码
            if content.find(virus_sig[virus]) >= 0:
                print('{0}, found virus {1}'.format(path, virus))
        return

    # 递归情况：递归调用
    for item in os.listdir(path):
        fullpath = os.path.join(path, item)
        scan(fullpath, virus_sig)

if __name__ == '__main__':
    scan('test', virus_sig)