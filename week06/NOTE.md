# Week06 学习笔记

> 作业背景
> 
> 数据经过分析和清洗之后，需要使用适当的方式对数据进行展示，Web 就是当前最流行的展示方式之一。
> 
> 作业要求：使用 Django 展示豆瓣电影中某个电影的短评和星级等相关信息：
> 
> - 要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级；
> - 展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级；
> - 选做) 在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评。

### 简单创建 Django 2.2.13 虚拟运行环境

```shell
python3.7 -m venv env # 创建3.7的虚拟环境 env
source env/bin/activate # 激活 env 环境
pip list # 展示虚拟环境中安装的所有包
pip freeze > requirements.txt # 将已安装的包列表 导出到requirements.txt 文件中
cat requirements.txt # 查看文件
pip install -r requirements.txt # 安装该环境导出的包
deactivate # 退出虚拟环境
```

### 创建 Django 工程

```shell
django-admin startproject website
cd website # 切换到工程目录website
# django-admin <command> [options]
# 建立并管理 Django 工程
# 建立并管理 Django 工程使用的数据库
# 控制调试或日志信息
# 
# python manage.py <command> [options]
#

python manage.py startapp douban    # 创建 douban 应用
python manage.py runserver # 运行 Django
```