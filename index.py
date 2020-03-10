
import spider
import mobile

url = 'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=%C6%B4%B6%E0%B6%E0%20%BF%B3%BC%DB%C8%BA&un=&rn=10&pn=0&sd=&ed=&sm=1&only_thread=1'


# 采集流程
def spiderFlow():
    # spider.spider(url)
    print('slider')


# 扫码加群流程
def scanFlow():
    print('scan')
    mobile.openScreen()
    mobile.sendFileToMobile()


scanFlow()
