import os
import time


# 锁屏
def lockScreen():
    # 26电源键
    z = os.system('adb shell input keyevent 26')


# 解锁屏幕
def openScreen():
    # 82菜单键 唤醒屏幕
    z = os.system('adb shell input keyevent 82')
    if z == 1:
        print('未连接手机')
        return False
    print('已连接手机')

    # 滑动一次 打开输入密码界面
    os.system('adb shell input swipe 500 2000 500 1500  300')
    # 输入密码 3401
    os.system('adb shell input keyevent 10')
    os.system('adb shell input keyevent 11')
    os.system('adb shell input keyevent 7')
    os.system('adb shell input keyevent 8')
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
        result = os.system('adb push %s /storage/sdcard0/DCIM/Screenshots/' % img_path)
        if result == 0:
            time.sleep(3)
            # 刷新相册
            os.system(
                'adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Screenshots/%s' % img)

            # 删除电脑上的文件
            os.remove(img_path)
            openWeiXin(img)
        else:
            print('未连接手机')

    else:
        lockScreen()


def openWeiXin(img):
    # 打开微信
    os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
    time.sleep(1)
    # 按返回键两次 保证微信界面在首页
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    # 再次打开微信
    os.system('adb shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI')
    time.sleep(1)

    # 打开菜单
    os.system('adb shell input keyevent 82')
    time.sleep(2)

    # 点击扫一扫按钮
    os.system('adb shell input tap 900 600')
    time.sleep(2)

    # 选择相册
    os.system('adb shell input tap 900 2000')
    time.sleep(2)

    # 选择第一张照片
    os.system('adb shell input tap 400 300')
    time.sleep(2)

    # 点击加群按钮
    os.system('adb shell input tap 500 1060')
    time.sleep(2)

    # 有可能是个人二维码，点击加好友按钮，按钮位置可能有两种情况
    os.system('adb shell input tap 500 920')
    time.sleep(1)
    os.system('adb shell input tap 500 720')
    time.sleep(3)

    # 点击加好友发送按钮
    os.system('adb shell input tap 950 150')
    time.sleep(2)

    # 返回
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    os.system('adb shell input keyevent 4')
    time.sleep(1)
    os.system('adb shell input keyevent 4')

    # 删除照片
    os.system('adb shell rm /storage/sdcard0/DCIM/Screenshots/%s' % img)
    time.sleep(3)

    # 锁屏 结束
    lockScreen()
