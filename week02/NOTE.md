# 学习笔记

解决week01 作业问题

## 作业一：

- 为 Scrapy 增加代理 IP 功能
- 将保存至 csv 文件的功能修改为保存到 MySQL，并在下载部分增加异常捕获和处理机制。

备注：代理 IP 可以使用 GitHub 提供的[免费 IP 库](https://github.com/jhao104/proxy_pool)

补充些 MySQL 知识，[MySQL用户及权限](https://zhuanlan.zhihu.com/p/55798418)

## 作业二：

使用 requests 或 Selenium 模拟登录[石墨文档](https://shimo.im)

> PS: 之前一直是微信登录石墨文档的，因为要模拟密码登录石墨文档，跑去设置初始密码，但是设置密码不成功😭，放弃！继续用微信登录。

使用 Selenium 模拟点击跳转到微信授权页，用手机微信扫码登录，因为 chromedriver 不会保存 Cookies 每次浏览石墨文档都需要扫码很麻烦，所以采取了初次登录时获取授权保存 Cookies，再次浏览时携带 Cookies 浏览，减少微信授权操作
参考文档 👉 [selenium+requests进行cookies保存读取操作](https://www.jianshu.com/p/c443be410987)

> 啊哈，使用邮箱绑定，改密码成功！✌️ 可以使用账号密码登录了，使用 requests 模拟登录石墨文档