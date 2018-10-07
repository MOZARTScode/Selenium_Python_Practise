import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import json

###########################
def get_focusNews():
    focusNews_url = 'https://www.toutiao.com/api/pc/focus/'
    headers = {
    'Host': 'www.toutiao.com',
    'Referer': 'https://www.toutiao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'X-Requested-With': 'XMLHttpRequest',
    }
    try:
        response = requests.get(focusNews_url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_focusNews(focuNewsJson):
    if focuNewsJson:
        items = focuNewsJson.get('data').get('pc_feed_focus')
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标

        # >>>seq = ['one', 'two', 'three']
        # >>> for i, element in enumerate(seq):
        # ...     print i, element
        # ... 
        # 0 one
        # 1 two
        # 2 three

        focusNewsList = []
        for item in items:
            focusNews = {}
            focusNews['title'] = item.get('title')
            focusNews['display_url'] = 'https://www.toutiao.com' + item.get('display_url')
            focusNews['image_url'] = 'https' + item.get('image_url')
            focusNewsList.append(focusNews)
            # yield focusNews
            # yield的作用：？？？  
        print(focusNewsList)
        with open('focusNews.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(focusNewsList, indent=2, ensure_ascii=False))

focus_News_json = get_focusNews()
a = parse_focusNews(focus_News_json)

###########################
