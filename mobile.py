import os


def sendFileToMobile():
    imagesPath = os.getcwd() + '/images'
    print(imagesPath)
    print(os.listdir(imagesPath))

    images = os.listdir(imagesPath);
    for img in images:
        print(os.path.join(imagesPath, img))
        imgPath = os.path.join(imagesPath, img)
        os.system('adb push %s /data/images' % imgPath)

    print('send file')
    # os.system('adb devices')
    # os.system('adb push ' + imagesPath +)
    print('send file')
