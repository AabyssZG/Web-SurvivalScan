#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

import _thread
from enum import Enum
import os
import time

import requests, sys, random
from tqdm import tqdm
from typing import Optional, Tuple
from termcolor import cprint
from requests.compat import json
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

class EServival(Enum):
    REJECT = -1
    SURVIVE = 1
    DIED = 0

reportData = []

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
    if not os.path.exists(".data"):
        os.mkdir(".data")
    report = open(".data/report.json","w")
    report.close()

def scanLogger(result:Tuple[EServival,Optional[int],str,int]):
    (status,code,url,length) = result
    if status == EServival.SURVIVE:
        cprint(f"[+] 状态码为: {code} 存活URL为: {url} 页面长度为: {length} ","red")
    if(status == EServival.DIED):
        cprint(f"[-] 状态码为: {code}  无法访问URL为: {url} ","yellow")
    if(status == EServival.REJECT):
        cprint(f"[-]   URL为: {url} 的目标积极拒绝请求，予以跳过！", "magenta")
    
    if(status == EServival.SURVIVE):
        fileName = "output.txt"
    elif(status == EServival.DIED):
        fileName = "outerror.txt"
    if(status == EServival.SURVIVE or status == EServival.DIED):
        with open(file=fileName, mode="a") as file4:
            file4.write(f"[{code}]  {url}\n")
    collectionReport(result)

def survive(url:str):
    try:
        header = {"User-Agent": random.choice(ua)}
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url=url, headers=header, timeout=6, verify=False)  # 设置超时6秒
    except:
        cprint("[-] URL为 " + url + " 的目标积极拒绝请求，予以跳过！", "magenta")
        return (EServival.REJECT,0,url,0)
    if r.status_code == 200 or r.status_code == 403:
        return (EServival.SURVIVE,r.status_code,url,len(r.content))
    else:        
        return (EServival.DIED,r.status_code,url,0)

def collectionReport(data):
    global reportData
    (status,statusCode,url,length) = data
    state = ""
    if status == EServival.DIED:
        state = "deaed"
    elif status == EServival.REJECT:
        state = "reject"
    elif status == EServival.SURVIVE:
        state = "servival"
    reportData.append({
        "url":url,
        "status":state,
        "statusCode":statusCode
    })

def dumpReport():
    with open(".data/report.json",encoding="utf-8",mode="w") as file:
        file.write(json.dumps(reportData))

def getTask(filename=""):
    if(filename != ""):
        with open(file=filename,mode="r") as file:
            for url in file:
                yield url.strip()

def end():
    count_out = len(open("output.txt", 'r').readlines())
    if count_out >= 1:
        print('\n')
        cprint(f"[+][+][+] 发现目标TXT有存活目标，已经导出至 output.txt ，共 {count_out} 行记录\n","red")
    count_error = len(open("outerror.txt", 'r').readlines())
    if count_error >= 1:
        cprint(f"[+][-][-] 发现目标TXT有错误目标，已经导出至 outerror.txt ，共行{count_error}记录\n","red")

def main():
    logo()
    file_init()
    # 获取目标TXT名称
    txt_name = str(input("请输入目标TXT文件名\nFileName >>> "))
    cprint("================开始读取目标TXT并批量测试站点存活================","cyan")
    # 读取目标TXT
    for url in getTask(txt_name):
        if('://' not in url):
            url = f"http://{url}"
        try:
            _thread.start_new_thread(lambda url: scanLogger(survive(url)), (url, ))
            time.sleep(0.2)
        except KeyboardInterrupt:
            print("Ctrl + C 手动终止了进程")
            sys.exit()
    dumpReport()
    end()
    sys.exit()

if __name__ == '__main__':
    main()
