import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import json

######连接mongodb##################
import pymongo
uri =  'mongodb://' + 'crawler' + ':' + 'crawler' + '@' + '39.108.231.106' + ':' + '27017' +'/'+ 'crawlPractise'
client = pymongo.MongoClient(uri)
db = client.crawlPractise
collection = db.headlines
# db.authenticate('crawler', 'crawler')


###########################
def get_focus_news():
    focus_news_url = 'https://www.toutiao.com/api/pc/focus/'
    headers = {
    'Host': 'www.toutiao.com',
    'Referer': 'https://www.toutiao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'X-Requested-With': 'XMLHttpRequest',
    }
    try:
        response = requests.get(focus_news_url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_focus_news(focu_news_json):
    if focu_news_json:
        items = focu_news_json.get('data').get('pc_feed_focus')
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标

        # >>>seq = ['one', 'two', 'three']
        # >>> for i, element in enumerate(seq):
        # ...     print i, element
        # ... 
        # 0 one
        # 1 two
        # 2 three

        focus_news_list = []
        for item in items:
            focus_news = {}
            focus_news['title'] = item.get('title')
            focus_news['display_url'] = 'https://www.toutiao.com' + item.get('display_url')
            focus_news['image_url'] = 'https' + item.get('image_url')
            focus_news_list.append(focus_news)
            yield focus_news
            
        # yield之后，生成不了json文件
        # with open('focus_news.json', 'w', encoding='utf-8') as file:
        #     file.write(json.dumps(focus_news_list, indent=2, ensure_ascii=False))

def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to the mongodb!')

# if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == '__main__':
    focus_News_json = get_focus_news()
    # Python中，（*）会把接收到的参数形成一个元组，而（**）则会把接收到的参数存入一个字典
    results = parse_focus_news(focus_News_json)
    for result in results:
        print(result)
        save_to_mongo(result)

###########################
