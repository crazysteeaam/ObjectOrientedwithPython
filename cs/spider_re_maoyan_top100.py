import requests
import faker
import re
import json
import csv
import codecs

# 使用fake库，生产伪造数据和http header
fake = faker.Factory.create()
headers = {
    'Connection': 'keep-alive',
    'User-Agent': fake.user_agent()
}

_content = {}  # 保存排行榜信息 index:[image, title, actor, time, score]


def download_parse(url):
    global _content
    # 定义正则表达式，匹配网页中的影片的7中数据信息
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                         + '.*?<img data-src="(.*?)"'
                         + '.*?<p class="name"><a.*?">(.*?)</a>'
                         + '.*?<p class="star">(.*?)</p>'
                         + '.*?<p class="releasetime">(.*?)</p>'
                         + '.*?<p class="score"><i class="integer">(.*?)</i>'
                         + '.*?<i class="fraction">(.*?)</i>.*?</dd>', re.S)
    try:
        response = requests.get(url, headers=headers)
        if not response.ok:  # 如果下载页面失败，则返回None
            return None
        items = re.findall(pattern, response.text)
        # 抽取把正则表达式匹配的结果信息，并放置到全局变量_content中
        for item in items:
            board_index = item[0]
            image_url = item[1]
            name = item[2]
            star = item[3].strip()[3:]
            time = item[4].strip()[5:]
            score = item[5] + item[6]
            _content[board_index] = [name, star, time, score, image_url]
            print(_content[board_index])  # 输出调试
    except Exception as e:
        print(e)
        return None


def save_json(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(_content, ensure_ascii=False))


def save_csv(filename):
    # 先给文件写一个Windows系统用来识别编码的头
    with open(filename, 'wb') as f:
        f.write(codecs.BOM_UTF8)  # 避免乱码
    # 使用append模式打开文件，继续写入
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        f_csv = csv.writer(f, dialect='excel', )
        f_csv.writerow(['排名', '影片名称', '主演', '上演时间', '得分', '电影海报URL'])
        for (k, v) in _content.items():
            f_csv.writerow([k, v[0], v[1], v[2], v[3], v[4]])


def main():
    global _content
    url_pattern = 'http://maoyan.com/board/4?offset={0}'
    for i in range(0, 100, 10):
        url = url_pattern.format(i)
        download_parse(url)
    save_json('maoyan_top100.json')
    save_csv('maoyan_top100.csv')


if __name__ == '__main__':
    main()
