import os
import time


# 锁屏
def lockScreen():
    # 26电源键
    os.system('adb shell input keyevent 26')


# 解锁屏幕
def openScreen():
    # 82菜单键
    os.system('adb shell input keyevent 82')
    os.system('adb shell input swipe 500 2000 500 1500  300')
    print('解锁屏幕')


# 发送文件到手机相册
def sendFileToMobile():
    imagesPath = os.getcwd() + '/images'
    print(imagesPath)
    print(os.listdir(imagesPath))

    images = os.listdir(imagesPath)
    if len(images) > 0:
        print(images[0])
        img = images[0]
        print(os.path.join(imagesPath, img))
        imgPath = os.path.join(imagesPath, img)
        os.system('adb push %s /storage/sdcard0/DCIM/Screenshots/' % imgPath)
        time.sleep(3)

        # 刷新相册
        os.system(
            'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Screenshots/%s' % img)

        # 删除电脑上的文件
        os.remove(imgPath)
        openWeiXin(img)
    else:
        lockScreen()


# 删除文件
# adb shell rm /storage/sdcard0/DCIM/Screenshots/3a345242ad4bd113dea4374d4dafa40f4afb0583.jpg


def openWeiXin(img):
    os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
    time.sleep(1)
    # 4返回键 保证微信界面在首页
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
    time.sleep(1)

    # 打开菜单
    os.system('adb shell input keyevent 82')
    time.sleep(2)

    # 打开扫一扫
    os.system('adb shell input tap 900 600')
    time.sleep(2)

    # 打开相册
    os.system('adb shell input tap 900 2000')
    time.sleep(2)

    # 选择一张照片
    os.system('adb shell input tap 400 300')
    time.sleep(2)

    # 点击加群按钮
    os.system('adb shell input tap 500 1060')
    time.sleep(2)

    # 点击加好友按钮
    os.system('adb shell input tap 500 720')
    time.sleep(3)

    # 点击加好友发送按钮
    os.system('adb shell input tap 950 150')
    time.sleep(2)

    os.system('adb shell input keyevent 4')
    time.sleep(1)
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    os.system('adb shell input keyevent 4')

    # 删除照片
    os.system('adb shell rm /storage/sdcard0/DCIM/Screenshots/%s' % img)
    time.sleep(3)

    lockScreen()


