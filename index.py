import spider
import mobile
import random
import time

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
    # while True:
    #     spiderFlow()
    #     time.sleep(360)
    #     # scanFlow()
    #     # 休眠0.5小时到2小时
    #     time.sleep(random.randint(1800, 7200))
    while True:
        # spiderFlow()
        # time.sleep(360)
        scanFlow()
        # 休眠0.5小时到2小时
        time.sleep(random.randint(60, 600))


start()

# mobile.sendFileToMobile()
