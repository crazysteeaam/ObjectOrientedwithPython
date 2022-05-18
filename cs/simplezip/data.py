import os, zipfile
def get_file_list(path):
    """"返回指定路径path的内容的迭代器"""
    if os.path.isdir(path):
        for item in os.listdir(path):
            p1 = os.path.join(path, item)
            if os.path.isdir(p1):
                size = "文件夹"
            else:
                size = str(os.path.getsize(p1))
            yield (item, size)

def get_zipfile_list(path):
    """"返回给定zip文件的内容的迭代器"""
    zf = zipfile.ZipFile(path)
    zfiles = zf.infolist()
    for f in zfiles:
        name = f.filename
        # python压缩不会有乱码，其它压缩软件中文目录文件名有问题
        # name = name.encode('cp437').decode('gbk') #防止乱码
        size = str(f.file_size)
        yield (name, size)

def uncompress(spath, tpath):
    """解压spath zip文件到tpath目录下"""
    zf = zipfile.ZipFile(spath)
    zflist = zf.namelist()
    for name in zflist: #循环处理zip文件中的文件
        # python压缩不会有乱码，其它压缩软件中文目录文件名有问题
        # name1 = name.encode('cp437').decode('gbk') #避免中文乱码
        name1 = name.replace('/', '\\') #替换路径分隔符保持一致
        print(name1)
        fpath = os.path.join(tpath, name1) #构造路径
        print(fpath)
        if fpath.endswith('\\'): #如果是目录，则创建目录
            os.mkdir(fpath)
        else:                    #如果是文件，则创建文件
            (basename, filename) = os.path.split(fpath)
            if not os.path.exists(basename):
                os.makedirs(basename)
            with open(fpath, "wb+") as f:
                f.write(zf.read(name))
    zf.close()

def compress(files, spath, tpath):
    """压缩spath目录中的files列表中的文件到tpath"""
    print(files)
    print(spath)
    print(tpath)
    spath  = spath + '\\'
    f = zipfile.ZipFile(tpath, 'w', zipfile.ZIP_DEFLATED)
    for fpath in files:
        if os.path.isfile(fpath): #如果是文件，则直接写入
            relativepath = fpath.replace(spath, '')
            print(relativepath)
            f.write(fpath, relativepath)
        else: #如果是目录，则使用os.walk写入目录和所有子目录
            for dirpath, dirnames, filenames in os.walk(fpath):
                for filename in filenames:
                    fullpath = os.path.join(dirpath, filename)
                    relativepath = fullpath.replace(spath, '')
                    print(relativepath)
                    f.write(fullpath, relativepath)
    f.close()
