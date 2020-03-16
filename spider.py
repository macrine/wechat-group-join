import urllib.request
import re


# 采集
def spider(url):

    page = urllib.request.urlopen(url)
    html_code = page.read()
    data = html_code.decode('GBK')

    print(data)
    reg = r'original = "(.+?\.jpg)'
    reg_img = re.compile(reg)
    img_list = reg_img.findall(data)

    for img in img_list:
        print(img)
        img_path = img.split('/')
        print()
        urllib.request.urlretrieve(img, 'images/'+img_path[len(img_path)-1])
