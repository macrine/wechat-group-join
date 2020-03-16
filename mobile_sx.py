# 三星手机
import os
import time
import spider


# 锁屏
def lockScreen():
    # 26电源键
    z = os.system('adb shell input keyevent 26')


# 解锁屏幕
def openScreen():
    # 82菜单键
    z = os.system('adb shell input keyevent 3')
    if z == 1:
        print('未连接手机')
        return False
    print('已连接手机')
    print('解锁屏幕')


# 发送文件到手机相册
def sendFileToMobile():
    images_path = os.getcwd() + '/images'
    print(images_path)
    if not os.path.exists(images_path):
        os.mkdir(images_path)

    print(os.listdir(images_path))

    images = os.listdir(images_path)

    if len(images) > 0:
        print(images[0])
        img = images[0]
        print(os.path.join(images_path, img))
        img_path = os.path.join(images_path, img)
        result = os.system('adb push %s /storage/sdcard0/DCIM/Camera/' % img_path)
        if result == 0:
            time.sleep(3)
            # 刷新相册
            os.system(
                'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/%s' % img)

            # 删除电脑上的文件
            os.remove(img_path)
            openWeiXin(img)
        else:
            print('未连接手机')

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
    os.system('adb shell input tap 900 1520')
    time.sleep(2)

    # 选择一张照片
    os.system('adb shell input tap 400 300')
    time.sleep(2)

    # 点击加群按钮
    os.system('adb shell input tap 500 1060')
    time.sleep(2)

    # 点击加好友按钮
    os.system('adb shell input tap 500 920')
    time.sleep(1)
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
