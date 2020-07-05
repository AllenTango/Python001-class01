# 学习笔记

解决week01 作业问题

## 作业一：

- 为 Scrapy 增加代理 IP 功能
- 将保存至 csv 文件的功能修改为保存到 MySQL，并在下载部分增加异常捕获和处理机制。

备注：代理 IP 可以使用 GitHub 提供的[免费 IP 库](https://github.com/jhao104/proxy_pool)

PS：数据库什么的，第一次结束，从开始安装到简单的查询，耗了我好几天时间，差点想放弃了。😭😭😭，现在也还懵着·····

1. Mac 下简单使用命令：
   1. 启动 MySQL `sudo /usr/local/mysql/support-files/mysql.server start`  [也可以在系统偏好设置启动(感觉好像没啥变化，慌得一批)] 原来进一步操作，要登录的🤦‍♂️
   2. 登录 MySQL `/usr/local/mysql/bin/mysql -u root -p` 我这是以管理员身份登录
   3. `CREATE DATABASE maoyan CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;` 创建新数据库命令，可指定存储格式
   4. `SHOW DATABASES;` 可以查看当前所存在的数据库，[SQL语句以';'🔚结束]
   5. `USE maoyan` 选择要使用数据库maoyan
   6. `CREATE TABLE movie (movie_id INT NOT NULL AUTO_INCREMENT,);` 插入新表
   7. `SELECT * FROM movie;` 查看表
   8. 停止 MySQL `sudo /usr/local/mysql/support-files/mysql.server stop`
2. 随机代理IP，使用类，改动的比较少 [期间复制下来IP无效了，没发觉，导致整个程序运行不了🤦‍♂️] 使用 `scrapy crwal maoyan --nolog` 也可以查看调试，

补充些 MySQL 知识，[MySQL用户及权限](https://zhuanlan.zhihu.com/p/55798418)

[MySQL 插入数据](https://geek-docs.com/mysql/mysql-basic/mysql-insert-data.html)

[爬取多个页面与MySQL数据库的存储](https://zhuanlan.zhihu.com/p/41010643)

## 作业二：

使用 requests 或 Selenium 模拟登录[石墨文档](https://shimo.im)

> PS: 之前一直是微信登录石墨文档的，因为要模拟密码登录石墨文档，跑去设置初始密码，但是设置密码不成功😭，放弃！继续用微信登录。

使用 Selenium 模拟点击跳转到微信授权页，用手机微信扫码登录，因为 chromedriver 不会保存 Cookies 每次浏览石墨文档都需要扫码很麻烦，所以采取了初次登录时获取授权保存 Cookies，再次浏览时携带 Cookies 浏览，减少微信授权操作
参考文档 👉 [selenium+requests进行cookies保存读取操作](https://www.jianshu.com/p/c443be410987)

> 啊哈，使用邮箱绑定，改密码成功！✌️ 可以使用账号密码登录了，使用 requests 模拟登录石墨文档