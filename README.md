# 自动完成青年大学习
## 声明：👀该脚本代码主要参考<a href = "https://github.com/captain686/Youth-Learning">captain686|Youth-Learning</a>👀<br/>

>我把其中关键代码拿了出来，放到了一个脚本文件中。并且增加了查询学习记录功能，如果最新一期的大学习版本号和当前已经学过的版本号不一致则代表未进行学习，则进行学习。

<br/>
### 代理方式
>😢青年大学习屏蔽大多数的云服务的ip，所以需要使用代理，我改变了原作者使用代理池的方法，使用代理池可能更稳定，但是为了方便，主要是懒😜。我就直接自己定义代理IP了。直接mian.py中修改 ```bash proxy = {'https': 'https://127.0.0.1:7890'} ```即可。这里推荐一个免费的代理池，如果失效的话，可以到🛫<a href = 'https://www.freeproxy.world/'>FreeProxy</a>找到中国的代理（中国的青年大学习，使用中国的代理，国外的我没试过🤦‍♂️）

### 🚀推送方式🚀

我新增加了可以向微信推送的方式，我使用的是<a href = 'https://sct.ftqq.com/'>Server酱</a>，注册拿到SendKey，然后在main.py中修改```bash SCKEY = '' ``` 即可。🙄
> 🍷🍷🍷在以下情况下会向你的微信发送通知：🍷🍷🍷<br/>
> >1.完成最新一期的大学习后
> >2.脚本正常运行，但是大学习未更新，无法完成学习
> >3.大学习已经更新到最新一期，但是无法正常完成学习


>
> 向机器人QQ发送关键字即可获取截图
>
> 周一下午1点后会自动完成本次观看任务
>
> 访问 `http://你的ip:6106/`或 `http://你的ip:6106/img/`即可获取视频完成图片链接或截图
>
> 机器人获取截图样式
> ![](doc/end.png)

***

### 配置

> 1.  抓取本人的青年大学习 `openid`值
>
> > 🍎IOS用户可使用Stream进行抓取
> >
> > > 1.  在设置里设置 `HTTPS`抓包
> > >
> > > 2.  设置抓包模式为白名单模式
> > >
> > > 3.  添加抓包域名 `*.youth54.cn`
> > >
> > > 4.  开启抓包访问青年大学习
> > >
> > > 5.  筛选抓包历史中的 `POST`请求可以找到 `openid`
> >
> > 😊 安卓系统可以使用`HttpCanary`进行抓包（可能需要root）
> >
> > > 1. 在主界面点击加号选择微信
> > > 2. 开启抓包访问青年大学习
> > > 3. 在抓包历史中搜索youth54.cn，找到`POST`请求可以找到`openid`
> > >
> > > 你也可以选择使用电脑微信抓包
> > >
> > > 具体细节`百度谷歌`
>
> 1.  关于 `config.py`
>
> > `info` –> 你需要在图片上添加的水印信息
> >
> > `openid` –>你抓取到的 `openid`
> >
> > `proxyPool_url`  –>代理池地址，无需修改
> >
> > `Keyword` –>机器人触发关键字
>
> 1.  配置机器人
>
> > 配置 `dxx/qbot/config.yml`文件
> >
> > `uin`:  # QQ账号
> >
> > `password`  # QQ密码

### 搭建

🐳安装 `docker`以及 `docker-compose`

> `docker`换源自行搜索

```bash
git clone https://github.com/captain686/young-study.git
cd young-study
git clone https://github.com/jhao104/proxy_pool.git
mv proxy.yml -f proxy_pool/docker-compose.yml
cd proxy_pool && docker-compose up -d
cd ../ && docker-compose up -d
```

### 查看docker容器运行结果

```bash
docker ps
```

### 全部正常运行后进入青年大学习的主环境

```bash
docker exec -it $(docker ps|grep qndxx|awk '{print $1}') /bin/bash
```

### 配置机器人

> 注意：`qbot`文件夹中已经附带 `go-CQHttp`二进制文件，如想使用其他版本请在自行下载，并将 `go-CQHttp`二进制文件放置在 `dxx/qbot`目录下即可

```bash
cd qbot && chmod 777 go-cqhttp
```

```bash
./go-cqhttp
```

> `bash go-cqhttp`命令为启动机器人命令，关闭窗口时机器人会退出，可以使用进程守护执行程序，命令如下

```bash
nohup ./go-cqhttp > /home/dxx/DxxLog/cqhttp.log 2>&1 &
```

> 查看 `cqhttp.log`文件看机器人需不需要登陆验证

```bash
cat cqhttp.log
```

> 如果提示扫码登陆可将本目录下的 `png`文件下载到本地扫码登陆

### 关于视频最后截图

如果你只需要视频最后截图那你并不需要配置机器人

你只需要在微信里面访问

`http://你的ip:6106/`或 `http://你的ip:6106/img/`即可

> 😃`http://你的ip:6106/` 返回图片链接;
>
> ![](./doc/index.png)
>
> 🙈`http://你的ip:6106/img/`
> 返回图片
> ![](./doc/2022-3-25.PNG)

## Update

### 2020-3-25

> 优化了观看结尾截图页面样式，如图，本次更新提供两个版本模板，详细配置请看`config.py`
>
> 默认采取`img`模板，请根据自己需求更改
>
> ![](./doc/2022-3-25.PNG)

### 😊 `To DO`

- [ ] 一个新的想法：使用`github Actions`来完成整套流程，你只需要`fork`本仓库然后再配置个人信息即可使用，截图通过邮箱推送，摆脱没有服务器的限制

### 👼 bug请提issues
