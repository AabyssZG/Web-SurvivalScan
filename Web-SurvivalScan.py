#!/usr/bin/env python
#_*_coding:utf-8_*_
import _thread
import time
import requests, sys, random
from tqdm import tqdm
from termcolor import cprint
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

ua = [
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00"]

def logo():
    logo0 = r'''
              ╦ ╦┌─┐┌┐              
              ║║║├┤ ├┴┐             
              ╚╩╝└─┘└─┘             
╔═╗┬ ┬┬─┐┬  ┬┬┬  ┬┌─┐┬  ╔═╗┌─┐┌─┐┌┐┌
╚═╗│ │├┬┘└┐┌┘│└┐┌┘├─┤│  ╚═╗│  ├─┤│││
╚═╝└─┘┴└─ └┘ ┴ └┘ ┴ ┴┴─┘╚═╝└─┘┴ ┴┘└┘
             Version: 1.01
       Author: 曾哥(@AabyssZG)
Whoami: https://github.com/AabyssZG
'''
    print(logo0)

def file_init():
    # 新建正常目标导出TXT
    f1 = open("output.txt", "wb+")
    f1.close()
    # 新建其他报错导出TXT
    f2 = open("outerror.txt", "wb+")
    f2.close()

def survive(url):
    try:
        header = {"User-Agent": random.choice(ua)}
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url=url, headers=header, timeout=6, verify=False)  # 设置超时6秒
    except:
        cprint("[-] URL为 " + url + " 的目标积极拒绝请求，予以跳过！", "magenta")
        sys.exit()
    if r.status_code == 200:
        cprint("[+] 状态码%d" % r.status_code + ' ' + "存活URL为:" + url + '    ' + "页面长度为:" + str(len(r.content)),"red")
        f3 = open("output.txt", "a")
        f3.write(url + '\n')
        f3.close()
    else:
        cprint("[-] 状态码%d" % r.status_code + ' ' + "无法访问URL为:" + url ,"yellow")
        f4 = open("outerror.txt", "a")
        f4.write('[' + str(r.status_code) + ']' + '  ' + url + '\n')
        f4.close()
    sys.exit()

def end():
    count_out = len(open("output.txt", 'r').readlines())
    if count_out >= 1:
        print('\n')
        cprint("[+][+][+] 发现目标TXT有存活目标，已经导出至 output.txt ，共%d行记录" %count_out,"red")
    count_error = len(open("outerror.txt", 'r').readlines())
    if count_error >= 1:
        cprint("[+][-][-] 发现目标TXT有错误目标，已经导出至 outerror.txt ，共%d行记录" %count_error,"red")

def main():
    logo()
    file_init()
    # 获取目标TXT名称
    txt_name = str(input("请输入目标TXT文件名\nFileName >>> "))
    cprint("================开始读取目标TXT并批量测试站点存活================","cyan")
    # 读取目标TXT
    with open(txt_name, 'r') as temp:
        for url in temp.readlines():
            url = url.strip()
            if url=='':
                continue
            if ('://' not in url):
                url = str("http://") + str(url)
            try:
                _thread.start_new_thread(survive, (url, ))
                time.sleep(0.2)
            except KeyboardInterrupt:
                print("Ctrl + C 手动终止了进程")
                sys.exit()
    end()
    sys.exit()

if __name__ == '__main__':
    main()
