import os
import time
import multiprocessing

def get_file_list(path) :
    #获取目录下的文件list
    fileList = []
    for root, dirs, files in list(os.walk(path)):
        for f in files:
            if f.endswith('.txt') or f.endswith('.py'):
                fileList.append(root + "\\" + f)
    return fileList

def process_file(filename) :
    #统计每个文件中行数和字符数，并返回
    line_counts = 0  # 行数
    word_counts = 0  # 单词个数
    character_counts = 0  # 字符数
    try:
        with open(filename, 'r', encoding='utf8') as f:
            for line in f:
                words = line.split()  # 分离出单词
                line_counts += 1  # 行数加1
                word_counts += len(words)  # 单词个数加1
                character_counts += len(line)  # 字符数加1
    except UnicodeDecodeError as e:
        pass
    return filename, line_counts, word_counts, character_counts

if __name__ == "__main__":
    #创建多个进程去统计目录中所有文件的行数和字符数
    path = "C:\Program Files\Python36\Lib"
    files = get_file_list(path)
    # print(len(files))
    # 串行处理测试
    start_time = time.time()  # 结束时间
    with open("res1.txt","w") as outf:
        for f in files:
            r = process_file(f)
            outf.writelines("文件：{} 行数：{} 单词：{} 字符：{}\n".format(r[0], r[1], r[2], r[3]))
    end_time = time.time()
    print("串行处理消耗时间：{}".format(end_time - start_time))
    # 并行处理测试
    start_time = time.time()  # 开始时间
    pool = multiprocessing.Pool(4)
    resultList = pool.map(process_file, files)
    pool.close()
    pool.join()
    with open("res2.txt","w") as outf:
        for r in resultList:
            outf.writelines("文件：{} 行数：{} 单词：{} 字符：{}\n".format(r[0], r[1], r[2], r[3]))
    end_time = time.time() # 结束时间
    print("并行处理消耗时间：{}".format(end_time - start_time))
