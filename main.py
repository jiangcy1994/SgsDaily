import argparse, sys, time 

if sys.platform not in ['win32']:
    raise OSError('Only have Implement on Windows Now')

from utils import *
import win32api, win32con, win32gui
parser = argparse.ArgumentParser()
parser.add_argument('user_name', help='用户名', type=str)
parser.add_argument('pass_word', help='密码', type=str)
parser.add_argument('-l', '--loop_times', help='日常循环次数', default=5, type=int)
args = parser.parse_args()

username = args.user_name
password = args.pass_word
loop_times = args.loop_times
print('用户名：{0}'.format(username))
print('密码：{0}'.format(password))
print('日常循环次数：{0}'.format(loop_times))

default_wait_interval = 3
operation_interval = 3
page_load_interval = 20
battle_interval = 120

browser = 'chrome.exe'
url = 'http://web.sanguosha.com/login/index.html'
title = u'三国杀官方正版_十周年全新资料篇_星火燎原重燃三国！ - Google Chrome'
cmd_args = ['--new-window', '--incognito']

def OpenExplorer():
    win32api.ShellExecute(0, 'open', browser, ' '.join(cmd_args + [url]), '', 0)
    time.sleep(page_load_interval)
    sgs_chrome_handle = win32gui.FindWindowEx(0, 0, None, title)

    win32gui.ShowWindow(sgs_chrome_handle, win32con.SW_RESTORE)
    win32gui.SetWindowPos(sgs_chrome_handle, win32con.HWND_TOP, 0, 0, 1200, 800, win32con.SWP_SHOWWINDOW)

    sgs_chrome_children_handles = []
    win32gui.EnumChildWindows(sgs_chrome_handle, lambda hWnd, param: param.append(hWnd), sgs_chrome_children_handles)
    sgs_host_handle = [*filter(lambda handle: win32gui.GetClassName(handle) == 'Chrome_RenderWidgetHostHWND', 
                               sgs_chrome_children_handles)][0]
    return sgs_chrome_handle, sgs_host_handle

def Login(sgs_host_handle):
    # 输入用户名
    win32gui.SetForegroundWindow(sgs_host_handle)
    time.sleep(operation_interval)
    lbtton_click_wait(sgs_host_handle, 580, 220)
    send_input_wait(sgs_host_handle, username)
    print('已输入用户名')

    # 输入密码
    lbtton_click_wait(sgs_host_handle, 580, 280)
    send_input_wait(sgs_host_handle, password)
    print('已输入密码')

    # 同意用户协议和隐私协议
    lbtton_click_wait(sgs_host_handle, 456, 444)
    print('已同意用户协议和隐私协议')

    # 登录
    lbtton_click_wait(sgs_host_handle, 580, 400)
    print('已登录')

    # 选新服
    lbtton_click_wait(sgs_host_handle, 720, 290)

    # 进入游戏
    lbtton_click_wait(sgs_host_handle, 770, 444, page_load_interval)
    print('已进入游戏')

    # 关闭log和活动
    lbtton_click_wait(sgs_host_handle, 930, 178)
    lbtton_click_wait(sgs_host_handle, 1105, 106)
    lbtton_click_wait(sgs_host_handle, 450, 70)
    lbtton_click_wait(sgs_host_handle, 450, 70)

def Daily(sgs_host_handle):
    # 进逐鹿
    lbtton_click_wait(sgs_host_handle, 815, 455)
    lbtton_click_wait(sgs_host_handle, 550, 300)
    print('已进入逐鹿')

    # 打逐鹿
    for i in range(loop_times):
        print('开始第{0}次'.format(i))
        lbtton_click_wait(sgs_host_handle, 390, 260)
        lbtton_click_wait(sgs_host_handle, 1080, 420)
        lbtton_click(sgs_host_handle, 950, 590)
        if i == 0:
            # 开5倍速
            for j in range(4):
                lbtton_click_wait(sgs_host_handle, 88, 530)
        time.sleep(battle_interval)

        lbtton_click_wait(sgs_host_handle, 550, 300)
        print('结束第{0}次'.format(i))
        
def CloseExplorer(sgs_chrome_handle):
    win32api.PostMessage(sgs_chrome_handle, win32con.WM_CLOSE, 0, 0)

def main():
    sgs_chrome_handle, sgs_host_handle = OpenExplorer()
    Login(sgs_host_handle)
    Daily(sgs_host_handle, loop_times)
    CloseExplorer(sgs_chrome_handle)

if __name__ == '__main__':
    main()