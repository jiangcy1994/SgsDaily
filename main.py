import argparse, sys

if sys.platform not in ['win32']:
    raise OSError('Only have Implement on Windows Now')

from browser import *
from config import *
from utils import *
from win32 import *

parser = argparse.ArgumentParser()
parser.add_argument('username', help='用户名', type=str)
parser.add_argument('password', help='密码', type=str)
parser.add_argument('-l', '--loop_times', help='日常循环次数', default=5, type=int)
args = parser.parse_args()

print('用户名：{0}'.format(args.username))
print('密码：{0}'.format(args.password))
print('日常循环次数：{0}'.format(args.loop_times))

def main():
    driver, title = OpenGame(game_url, args.username, args.password)
    
    sgs_chrome_hwnd = FindWindow(None, title + chrome_appendix)
    RestoreWindow(sgs_chrome_hwnd)
    SetWindowPos(sgs_chrome_hwnd, 0, 0, default_width, default_height)
    sgs_chrome_children_hwnds = EnumChildWindows(sgs_chrome_hwnd)
    sgs_host_hwnd = sgs_chrome_children_hwnds[chrome_render_hwnd]
    
    QuitLogoAndActivity(sgs_host_hwnd)
    Daily(sgs_host_hwnd, args.loop_times)
    
    QuitGame(driver)
    
if __name__ == '__main__':
    main()
