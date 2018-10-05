from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)
KEYWORD = 'ipad'

# quote用于转码，给中文、特殊字符转码，ex:quote('手机') 结果为：'%E6%89%8B%E6%9C%BA'
headers = {
    'content-type': 'application/json',
    'Cookie': ('Visitor=1; _bfa=1.1536309898572.1qg27x.1.1538743919365.1538750691904.30.153;'
               '_jzqco=%7C%7C%7C%7C1538743921370%7C1.725073321.1536309901330.1538750720709.1538750730693.'
               '1538750720709.1538750730693.undefined.0.0.115.115; __zpspc=9.29.1538750713.1538750730.'
               '4%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _RF1=118.250.58.75;'
               ' _RSG=fOK9nUoYw8C8odNRPSoQ9A; _RDG=28ad7a3ef245e02c0c3226297142b9b2af; '
               '_RGUID=c23a8b27-b125-4629-a25a-c9c65b5e7c88; _ga=GA1.2.2099963740.1536309902; _abtest_userid='
               '0d0f1fb9-016c-4697-97b5-ba9aa54ba434; appFloatCnt=8; Session=SmartLinkCode=U155952&SmartLinkKeyWord='
               '&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; '
               'Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1538750730036%7D%5D; '
               'traceExt=campaign=CHNbaidu81&adid=index; StartCity_Pkg=PkgStartCity=206; _gid=GA1.2.515659393.1538743921; '
               'MKT_Pagesource=PC; _bfi=p1%3D103046%26p2%3D600000435%26v1%3D152%26v2%3D151; manualclose=1; _bfs=1.6;'
               ' Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; gad_city=567e21b59903cef4b9450db7a9af6f44; _gat=1; '
               'ASP.NET_SessionSvc=MTAuOC4xODkuNTh8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUzNjU3MjYzMjQxNQ; '
               'ASP.NET_SessionId=wajw4hpnahkcgk214unbnai2'),
    'cookieorigin': 'http://vacations.ctrip.com',
    'Host': 'vacations.ctrip.com',
    'origin': 'http://vacations.ctrip.com',
    'Referer': 'http://vacations.ctrip.com/tour/detail/p19653911s206.html?kwd=%e5%87%a4%e5%87%b0',
    'User-Agent': 'Mozilla/5.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Length': '21'
}
r2 = requests.post('http://vacations.ctrip.com/tour/restapi/gateway/10124/GetUserInfo.json', headers=headers)