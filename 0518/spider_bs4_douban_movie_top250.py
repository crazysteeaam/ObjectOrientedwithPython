import requests
import faker
from bs4 import BeautifulSoup
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
    try:
        response = requests.get(url, headers=headers)
        if not response.ok:  # 如果下载页面失败，则返回None
            return None
        # 使用BeautifulSoup分析获得的html，抓取排行榜信息
        # 将html文档转化为BeautifulSoup对象
        soup = BeautifulSoup(response.text, "lxml")
        tag_ol = soup.find("ol")  # 找到ol
        tags_il = tag_ol.find_all('li')
        for tag in tags_il:
            # <div class="item">
            div_item = tag.find('div', attrs={'class': 'item'})
            # <div class="pic">
            div_pic = div_item.find('div', attrs={'class': 'pic'})
            # 排名
            board_index = div_pic.find('em', attrs={'class': ''}).get_text()
            # 海报url
            image_url = div_pic.find('img')['src']
            # <div class="info">
            div_info = div_item.find('div', attrs={'class': 'info'})
            # <div class="hd">
            div_hd = div_info.find('div', attrs={'class': 'hd'})
            # 影片名
            title = div_hd.find('span', attrs={'class': 'title'}).get_text()
            # <div class="bd">
            div_bd = div_info.find('div', attrs={'class': 'bd'})
            # 演职人员
            cast = div_bd.find('p', attrs={'class': ''}).get_text().strip()
            # 评分
            rate = div_bd.find(
                'span', attrs={'class': 'rating_num'}).get_text()
            # 评价 # 防止有的影片没有评价
            if div_bd.find('span', attrs={'class': 'inq'}):
                quote = div_bd.find('span', attrs={'class': 'inq'}).get_text()
            else:
                quote = ''
            _content[board_index] = [title, cast, rate, quote, image_url]
            print(_content[board_index])  # 调试输出
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
        f_csv = csv.writer(f, dialect='excel')
        f_csv.writerow(['排名', '影片名称', '演职人员', '得分', '评价', '电影海报URL'])
        for (k, v) in _content.items():
            f_csv.writerow([k, v[0], v[1], v[2], v[3], v[4]])


def main():
    global _content
    url_pattern = 'https://movie.douban.com/top250?start={0}'
    for i in range(0, 250, 25):
        url = url_pattern.format(i)
        download_parse(url)
    save_json('douban_movie_top250.json')
    save_csv('douban_movie_top250.csv')


if __name__ == '__main__':
    main()
