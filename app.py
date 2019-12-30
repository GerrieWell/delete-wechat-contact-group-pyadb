# -*- coding: utf-8 -*-


import pyadb as ADB
import easydict as edict
import time 

config = edict.EasyDict()
config.touch_gap_s = 1
config.PAGE_NUM = 2
xs = [130 + i * 200 for i in range(5) ]
ys = [ 330 + i * 270 for i in range(7)]


def tap_delete(pos):
    gap = 1
    long_gap = 1.5
    adb.shell_command("input tap {} {}".format(int(pos[0]),int (pos[1])))
    time.sleep(gap)
    adb.shell_command("input tap 1000 156")     # "..." 位置
    time.sleep(gap)
    adb.shell_command("input tap 1000 1875")    # "删除" 位置
    time.sleep(gap)
    adb.shell_command("input tap 760 1300")     # 红色的"删除"位置 
    time.sleep(long_gap)

def main():
    adb = ADB.ADB()
    # set ADB path
    adb.set_adb_path('/Users/gerrie/SDKs/platform-tools/adb')

    error,devices = adb.get_devices()
    try:
        adb.set_target_device(devices[0])
    except Exception:
        print("\n[!] Error:\t- ADB: {}\t - Python: {}".format(adb.get_error(),e.args))
        exit(-5)
    for p in range(config.PAGE_NUM):
        for x in xs:
            for y in ys:
        #         print("{}, {}".format(x,y))
                tap_delete([x, y])
    
        # 自动翻页命令
        cmd = "input swipe 550 2070 550 246 5000" # x1 y1 x2 y2 duration(ms)
        adb.shell_command(cmd)