import time

from win32 import *
from config import *

__all__ = ['Daily', 'QuitLogoAndActivity']

def Daily(hwnd, loop_times):
    '''每日（逐鹿）'''
    LButtonClick(hwnd, 815, 432) # 进逐鹿
    time.sleep(operation_interval)
    
    LButtonClick(hwnd, 450, 50) # 跳过动画
    print('已进入逐鹿')
    time.sleep(operation_interval)
    
    LButtonClick(hwnd, 628, 44) # 困难
    print('已进入困难')
    time.sleep(operation_interval)

    LButtonClick(hwnd, 155, 240) # 第一章
    print('已进入第一章')
    time.sleep(operation_interval)

    # 打逐鹿
    for i in range(loop_times):
        print('开始第{0}次'.format(i + 1))
        LButtonClick(hwnd, 385, 240) # 第一城
        time.sleep(operation_interval)
        
        LButtonClick(hwnd, 1085, 400) # 第五关
        time.sleep(operation_interval)
        
        LButtonClick(hwnd, 950, 570) # 进入挑战
        time.sleep(operation_interval)
        
        if i == 0:
            # 开5倍速
            for j in range(4):
                LButtonClick(hwnd, 100, 512) # 加速
                time.sleep(operation_interval)
        time.sleep(battle_interval)

        LButtonClick(hwnd, 550, 300) # 退出
        print('结束第{0}次'.format(i + 1))
        time.sleep(operation_interval)

def QuitLogoAndActivity(hwnd):
    '''关闭logo和活动'''
    time.sleep(operation_interval)
    LButtonClick(hwnd, 930, 158) # 关logo
    time.sleep(operation_interval)
    
    LButtonClick(hwnd, 1105, 88) # 关活动
    time.sleep(operation_interval)
    
    LButtonClick(hwnd, 450, 50)  # 关莫名其妙的卡屏
    time.sleep(operation_interval)
    
    LButtonClick(hwnd, 450, 50)
    time.sleep(operation_interval)
        