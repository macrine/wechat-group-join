import urllib.request
import re

# 采集
def spider(url):

    page = urllib.request.urlopen(url)
    htmlCode = page.read()
    data = htmlCode.decode('GBK')

    print(data)
    reg = r'original = "(.+?\.jpg)'
    reg_img = re.compile(reg)
    imgList = reg_img.findall(data)

    for img in imgList:
        print(img)
        imgPath = img.split('/')
        print()
        urllib.request.urlretrieve(img, 'images/'+imgPath[len(imgPath)-1])