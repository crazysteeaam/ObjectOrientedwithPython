import requests
import faker
import re
import json
import csv
import codecs

fake = faker.Factory.create()
headers = {'Connection': 'keep-alive', 'User-Agent': fake.user_agent()}
_content = {}


def download_parse(url):
    global _content
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                         + '.*?<img data-src="(.?)"'
                         + '.*?<p class="name"><a.*?">(.?)</a>'
                         + '.*?<p class="star"><a.*?">(.?)</p>'
                         + '.*?<p class="releasetime"><a.*?">(.?)</p>'
                         + '.*?<p class="score"><i class="integer">(.?)</i>'
                         + '.*?<i class="fraction">(.*?)</i>.*?</dd>', re.S)
    try:
        response = requests.get(url, headers=headers)
        if not response.ok:
            return None
        items = re.findall(pattern, response.text)
        for item in items:
            board_index = item[0]
            image_url = item[1]
            name = item[2]
            star = item[3].strip()[3:]
            time = item[4].strip()[5:]
            score = item[5] + item[6]
            _content[board_index] = [name, star, time, score, image_url]
            print(_content[board_index])
    except Exception as e:
        print(e)
        return None


def save_json(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(_content, ensure_ascii=False))


def save_csv(filename):
    with open(filename, 'wb') as f:
        f.write(codecs.BOM_UTF8)
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        f_csv = csv.writer(f, dialect='excel', )
        f_csv.writerow(['排名', '影片名词', '主演', '上演时间', '得分', '电影海报URL'])
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
