![Web-SurvivalScan](https://socialify.git.ci/AabyssZG/Web-SurvivalScan/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&pattern=Solid&stargazers=1&theme=Dark)

**By 曾哥(AabyssZG) && jingyuexing**


## ✈️ 一、工具概述

在日常工作的渗透测试过程中，经常会碰到渗透测试项目，而Web渗透测试通常是渗透项目的重点或者切入口

通常拿到正规项目授权后，会给你一个IP资产列表和对应的Web资产地址，这时候就需要我们进行快速存活验证

![资产列表](/img/资产列表.png)

如图，这个项目给了一万多个IP，并列出了对应的Web资产地址，这个时候就需要快速验证资产存活

网上找了一圈，都没什么好用的工具。于是，就写了这个Web资产存活检测小工具：Web-SurvivalScan  

**如果这个工具帮助到了你，欢迎赏个Star~哈哈**


## 📝 二、TODO

* [x] 支持在导出HTML界面里面显示标题，更方便确认资产信息
* [x] 支持对HTTP代理进行校验，检验代理可用性
* [x] 支持使用HTTP/HTTPS代理所有流量，并可以使用HTTP认证
* [x] 支持将 `:443` 自动识别转换为 `https://`
* [x] 支持读取多种编码格式的TXT（ANSI和UTF-8均支持）
* [x] 支持导出HTML文件，方便资产的可视化整理
* [x] 多线程扫描，1万条Web资产实测20分钟左右跑完
* [x] 存活验证时使用随机User-Agent请求头
* [x] 解决目标SSL证书问题 (自签名证书请改成 `http://` 即可)
* [x] 智能识别目标地址 (`example.com` 和`http://example.com:8080` 以及`http://example.com` 都不会报错)


## 🚨 三、安装Python依赖库

```
pip3 install -r requirements.txt
```


## 🐉 四、工具使用

首先，需要将目标Web资产批量复制到TXT内，并将该TXT放到本脚本同目录，如下图：

![TXT](/img/TXT.png)

**注：本脚本能智能识别目标地址 (`example.com` 和`http://example.com:8080` 以及`http://example.com` 都不会报错)**

```
# python3 Web-SurvivalScan.py

              ╦ ╦┌─┐┌┐
              ║║║├┤ ├┴┐
              ╚╩╝└─┘└─┘
╔═╗┬ ┬┬─┐┬  ┬┬┬  ┬┌─┐┬  ╔═╗┌─┐┌─┐┌┐┌
╚═╗│ │├┬┘└┐┌┘│└┐┌┘├─┤│  ╚═╗│  ├─┤│││
╚═╝└─┘┴└─ └┘ ┴ └┘ ┴ ┴┴─┘╚═╝└─┘┴ ┴┘└┘
             Version: 1.06
Author: 曾哥(@AabyssZG) && jingyuexing
 Whoami: https://github.com/AabyssZG

请输入目标TXT文件名
FileName >>> 【TXT文件名】
请输入代理IP和端口（无则回车）
Proxy >>> 【HTTP认证账号:HTTP认证密码@代理IP:端口】
Proxy >>> 【代理IP:端口（没有HTTP认证的情况下）】
```

![Run](/img/Run.png)

跑完后，即可拿到导出的两个文件：`output.txt` 和 `outerror.txt`

- `output.txt`：导出验证存活成功（状态码200）的Web资产
- `outerror.txt`：导出其他状态码的Web资产，方便后期排查遗漏和寻找其他脆弱点
- `.data/report.json`：所有资产的运行数据，按JSON格式导出，方便处理
- `report.html`：将所有资产进行HTML可视化导出，方便整理

![HTML](/img/HTML-Out.png)


## 五，感谢各位师傅

### Stargazers

[![Stargazers repo roster for @AabyssZG/Web-SurvivalScan](http://reporoster.com/stars/AabyssZG/Web-SurvivalScan)](https://github.com/AabyssZG/Web-SurvivalScan/stargazers)


### Forkers

[![Forkers repo roster for @AabyssZG/Web-SurvivalScan](http://reporoster.com/forks/AabyssZG/Web-SurvivalScan)](https://github.com/AabyssZG/Web-SurvivalScan/network/members)


### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AabyssZG/Web-SurvivalScan&type=Date)](https://star-history.com/#AabyssZG/Web-SurvivalScan&Date)
