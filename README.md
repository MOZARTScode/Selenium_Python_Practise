# Selenium_Python_Practise
This repository is uesed for all kinds of selenium practising.I want to use selenium skilled to crawl pages in the end.
During my Junior Pratical trainning, I used to crawl some data from Ctrip, but it has some contents genereted by JS so that I can't easily 
crawl the data. So, after the PT, I plan to spend some time on it and try to learn about it systematicly!
I will have learned the main content before the National day over!Please obey the time!

10.5
发现携程的反爬很多，微薄可以直接通过json的链接得到渲染的数据，但是携程得不到，即便是将请求头做好了；
微博博主主页信息json：https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&page=2 （可以直接访问）
景点信息相关json访问url：http://vacations.ctrip.com/tour/restapi/online/12447/ProductDetailTimingV5；
主要难点有两个：应该需要selenium等来模拟浏览器来获取数据、json数据比较繁杂（提取数据比较复杂）

10.7
今天爬取了今日头条的新闻，主要是熟悉爬取ajax获取的数据

10.8
今天在服务器上安装了mongoDB服务器，配置了基本的环境，同时试图在python中进行连接，但出现了一些问题