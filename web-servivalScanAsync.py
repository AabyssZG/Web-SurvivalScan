import asyncio
from enum import Enum
import datetime
import random
from httpx import request,ConnectError
from typing import List, Literal, Optional, Tuple
from pydantic.dataclasses import dataclass
from aiofiles import open as aioOpen
from termcolor import cprint

taskList:List['TaskNode'] = []

ua = [
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00"]

class EServival(Enum):
    REJECT = -1
    SURVIVE = 1
    DIED = 0

def Timer(func):
    def wapper():
        starTime = datetime.datetime.now().timestamp()
        func()
        endTime = datetime.datetime.now().timestamp()
        print(f"finished {starTime - endTime}s")
    return wapper

@dataclass
class TaskNode:
    url:str
    clock:float
    currentTime:float

async def createTask(filename,tiklock=10):
    async for url in  asyncGetUrlByFile(filename=filename):
        now = datetime.datetime.now()
        taskList.append(TaskNode(url=url,clock=now.timestamp()+ tiklock,currentTime=now.timestamp()))

async def getTask():
    """创建任务
    
    [description]
    
    Yields:
        [description]
        [type]
    """
    for task in taskList:
        yield task 

async def asyncGetUrlByFile(filename=""):
    """从文件中读取记录
    
    [description]
    
    Args:
        filename (str): [description] (default: `""`)
    
    Yields:
        [description]
        [type]
    """
    async with aioOpen(file=filename,mode="+r",encoding="utf8") as file:
      async for line in file:
        yield line

async def asyncFetch(url,headers={},timeout=0,method:Literal['GET','POST','OPTIONS','PUT','DELETE']="GET"):
    try:
        # res = request(method=method,url=url,timeout=timeout,headers=headers,proxies="your proxy url")
        res = request(method=method,url=url,proxies=proxies,timeout=timeout,headers=headers)
        return res
    except Exception as err:
        print("please setting proxy")

def scanLogger(result:Tuple[EServival,Optional[int],str]):
    (status,code,url) = result
    if status == EServival.SURVIVE:
        cprint(f"[+] 状态码为: {code} 存活URL为: {url} 页面长度为:  ","green")
    if(status == EServival.DIED):
        cprint(f"[-] 状态码为: {code}  无法访问URL为: {url} ","yellow")
    if(status == EServival.REJECT):
        cprint(f"[-]   URL为: {url} 的目标积极拒绝请求，予以跳过！", "magenta")

async def asyncScan(url):
    """开始扫描
    
    [description]
    
    Args:
        url ([type]): [description]
    """
    header = {"User-Agent": random.choice(ua)}
    # try:
    res = await asyncFetch(url=url,headers=header,timeout=6)
    if res != None:
        if(res.status_code == 200 or res.status_code == 403):
            return (EServival.SURVIVE,res.status_code,url)
        else:
            return (EServival.DIED,res.status_code,url)
    else:
        return None
    # except Exception:
    #     return (EServival.REJECT,None,url)

async def asyncServival():
    filename =  input("Star Scan!\nplease input filename>>>")
    await createTask(filename=filename)
    async for task in getTask():
        result = await asyncScan(task.url.strip())
        if result:
            scanLogger(result=result)
    return 0

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncServival())

if __name__ == '__main__':
    main()
    
