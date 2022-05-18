import io
import os
import json
import urllib.request
import logging

def set_logging():
    """配置日志，记录无法获取的歌曲列表"""
    logging.basicConfig(level=logging.INFO,
                        filename='log.txt',
                        filemode='w',
                        format='%(message)s')

def get_channel_list():
    """ 获取歌曲频道列表 """
    page_url = 'http://fm.baidu.com/dev/api/?tn=channellist' #百度音乐API频道列表
    channel_list = {} #保存歌曲频道的字典：channel_id:channel_name
    try:
        htmlDoc = urllib.request.urlopen(page_url).read().decode('utf8')
        content = json.load(io.StringIO(htmlDoc))
        channel_list_raw = content['channel_list']
        for ch in channel_list_raw:
            channel_list[ch['channel_id']] = ch['channel_name']
        return channel_list
    except Exception as e:
        print(e)
        return {}

def get_song_list(channel_id, channel_name, from_no, to_no):
    """ 获取指定频道的歌曲列表 """
    song_list = {} #保存歌曲信息的字典：song_id:[song_name,song_link,song_size]
    channel_url_pattern = 'http://fm.baidu.com/dev/api/?tn=playlist&format=json&id={}'
    channel_url = channel_url_pattern.format(channel_id)
    song_list_name = "./{0}{1}歌曲下载地址.json".format(channel_id,channel_name)
    try:
        htmlDoc = urllib.request.urlopen(channel_url).read().decode('utf8')
        content = json.load(io.StringIO(htmlDoc))
        song_id_list = content['list']
        for i in range(from_no, to_no): #从from_no到to_no的歌曲信息
            song_id, song_name, song_link, song_size = get_song_real_url(song_id_list[i]['id'])
            song_list[song_id] = [song_name, song_link, song_size]
        with open(song_list_name, mode='w', encoding='utf-8') as file:
            file.write(json.dumps(song_list))
        return song_list
    except Exception as e:
        print(e)
        return {}

def get_song_real_url(song_id):
    """ 获取歌曲的信息：song_id, song_name, song_link, song_size"""
    song_url_pattern = "http://music.baidu.com/data/music/fmlink?type=mp3&songIds={0}"
    song_url = song_url_pattern.format(song_id)
    try:
        htmlDoc = urllib.request.urlopen(song_url).read().decode('utf8')
        content = json.load(io.StringIO(htmlDoc))
        song_link = str(content['data']['songList'][0]['songLink'])
        song_name = str(content['data']['songList'][0]['songName'])
        song_size = str(content['data']['songList'][0]['size'])
    except Exception as e:
        print(e)
        logging.warning('无法获取歌曲信息:{0}'.format(song_id))
        return (None, None, None, 0)
    return str(song_id), song_name, song_link, song_size

def down_mp3_by_link(song_name, song_url, song_size):
    """ 下载超链接为song_link的歌曲到本地文件download/song_name.mp3 """
    file_name = '{0}.mp3'.format(song_name)
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    if os.path.exists(file_path): #已经下载，直接返回
        logging.info("{0}：文件已经存在".format(song_name))
        return

    logging.info("{0}：开始下载（大小为的{1}）".format(song_name, song_size))

    mp3 = urllib.request.urlopen(song_url)
    block_size = 8192
    down_loaded_size = 0
    file = open(file_path, "wb")
    while True:
        try:
            buffer = mp3.read(block_size)
            down_loaded_size += len(buffer)
            if (len(buffer) == 0):
                if down_loaded_size < song_size:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        logging.error('下载失败，删除该文件')
                break
            file.write(buffer)
            if down_loaded_size >= song_size:
                logging.info('{0}: 下载完成'.format(song_name))
                break
        except Exception as e:
            logging.error(e)
            if os.path.getsize(file_path) < song_size:
                if os.path.exists(file_path):
                    os.remove(file_path)
                    logging.error('{0}下载失败，删除该文件'.format(song_name))
    file.close()

def main():
    set_logging() #配置日志
    channel_list = get_channel_list() #获取频道列表
    # 获取哥频道列表下的所有歌曲
    for channel_id in channel_list:
        song_id = get_song_list(channel_id, channel_list[channel_id], 0, 4)
        # break

if __name__ == '__main__':
    main()