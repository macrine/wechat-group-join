import spider
import mobile
import random
import time

# 采集群二维码的贴吧网址列表
urls = [
    'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=%C6%B4%B6%E0%B6%E0%20%BF%B3%BC%DB%C8%BA&un=&rn=10&pn=0&sd=&ed=&sm=1&only_thread=1',
    'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=%C6%B4%B6%E0%B6%E0%20%BF%B3%BC%DB%C8%BA&rn=10&un=&only_thread=1&sm=1&sd=&ed=&pn=2',
    'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=%C6%B4%B6%E0%B6%E0%20%BF%B3%BC%DB%C8%BA&rn=10&un=&only_thread=1&sm=1&sd=&ed=&pn=3',
    'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=%D6%FA%C1%A6%C8%BA&un=&rn=10&pn=0&sd=&ed=&sm=1&only_thread=1',
    'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=%D6%FA%C1%A6%C8%BA&rn=10&un=&only_thread=1&sm=1&sd=&ed=&pn=2',
    'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=%D6%FA%C1%A6%C8%BA&rn=10&un=&only_thread=1&sm=1&sd=&ed=&pn=3',
]


# 采集流程
def spiderFlow():
    # 随机取一条贴吧网站采集二维码
    url = random.choice(urls)
    spider.spider(url)
    print(url)
    print('spider')


# 扫码加群流程
def scanFlow():
    print('scan')
    mobile.openScreen()
    time.sleep(2)
    mobile.sendFileToMobile()


def start():
    start_time = time.time()
    while True:
        if time.time() > start_time + 3600:
            # 一小时采集一次二维码图片
            start_time = time.time()
            spiderFlow()

        scanFlow()
        # 间隔1分钟到10分钟扫码一次
        sleep_time = random.randint(60, 600)
        print('sleepTime:%s' % sleep_time)
        time.sleep(sleep_time)


start()
