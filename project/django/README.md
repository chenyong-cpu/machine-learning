# Django指南

## Django安装

```bash
pip install django==4.1 # 下载4.1版本的django
python -m django version # 查看django版本
```

## 创建一个Django项目

```bash
django-admin startproject mysite
```

```txt
Django项目的目录结构如下：
mysite/ -- 这个目录无关紧要，可以重命名，只是用于储存文件的
    manage.py -- 一个让你交互Django的命令行工具
    mysite/ -- 这个目录是一个事实的Python包
        __init__.py -- 一个空文件，告诉Python这个目录应该被视为一个Python包。
        settings.py -- Django项目的设置
        urls.py -- Django的url配置，把不同的url对应到不同的函数
        asgi.py -- An entry-point for ASGI-compatible web servers to serve your project
        wsgi.py -- An entry-point for WSGI-compatible web servers to serve your project
```

### django-admin and manage.py

```bash
# 三者命令相等
django-admin <command> [options]
manage.py <command> [options]
python -m django <command> [options]
```

1. 获取帮助：django-admin help
2. 查看Django版本：django-admin version
