from urllib import request, parse
# print(help(request.Request))

url = 'http://httpbin.org/post'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'
    'Host'
}
dicts ={
    'name': 'lzy'
}
data = bytes(parse.url)
req = request.Request(url, data=data, headers=header, method='POST')
print()