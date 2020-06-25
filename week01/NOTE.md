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
- 创建项目 `scrapy startproject magic_spiders`
- `cd magic_spiders/magic_spiders` 需要再进入下一层目录，进入刚创建的项目文件里爬虫项目文件
- 创建爬虫 `scrapy gensipder maoyan maoyan.com`
- items 设置对应要爬取的内容 `name = scrapy.Field()` scrapy.Field 只返回一个值，使用管道 piplines，需在 setting 开启
- 运行爬虫命令 `scrapy crawl maoyan`
- 保存 cvs 可选命令行运行保存 `scrapy crawl maoyan -o maoyan_movie.csv`
  
  
```python
# 使用 CsvItemExporter 类导出 csv
# csv 追加模式 a+
from scrapy.exporters import CsvItemExporter

with open("./maoyan_movies.csv", "a+b") as f:
    exporter = CsvItemExporter(f, include_headers_line=False)
    exporter.start_exporting()
    exporter.export_item(item)
    exporter.finish_exporting()
```

### 疑惑：

- 错误与异常处理不太确定“该何时需要、如何捕捉”
- 猫眼电影，获取某一影片的名称、上映时间、类型、评分，在电影列表上就可以获取，而影片详情则只能在电影详情页[也含有影片的名称、上映时间、类型、评分]上获取，如果同时需要获取影片的名称、上映时间、类型、评分、详情，我是在列表页上获取影片的[名称等信息]呢，还是只获取详情页链接，再在详情页获取[名称等信息+影片详情]