# Week01 学习笔记

> 作业一：
> 
> 安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
> 
> 作业二：
> 
> 使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
> 
> 要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。

## 作业一：

版本1[`m_maoyan_movie.py`]: 偷个懒，使用猫眼电影手机版网页爬取[因为其页面简单，一次加载也刚好是10个]

## 作业二：
  
继续爬取对应手机页面，
- 运行爬虫命令 `scrapy crawl maoyan`
- 保存 cvs 可选命令行运行保存 `scrapy crawl maoyan -o maoyan_movie.csv`