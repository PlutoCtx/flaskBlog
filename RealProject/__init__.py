# @Version: python3.10
# @Time: 2023/7/6 11:09
# @Author: MaxBrooks
# @Email: 15905898514@163.com
# @File: __init__.py.py
# @Software: PyCharm
# @User: chent

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from RealProject.settings import BASE_DIR
from flask_migrate import Migrate

# 安装SQLAlchemy对象
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    # instance_relative_config 设置为True则代表开启文件加载配置，默认为False
    app = Flask(__name__, instance_relative_config=True)

    # 这里做了判断是否运行时传入了测试配置
    if test_config is None:
        # 如果没有传入，则从py文件加载配置，silent = True代表文件，文件加载成功则返回True
        CONFIG_PATH = BASE_DIR / 'RealProject/settings.py'
        app.config.from_pyfile(CONFIG_PATH, silent=True)
    else:
        # 和最开始的配置意思一致
        app.config.from_mapping(test_config)

    # 绑定数据库
    db.init_app(app)
    migrate.init_app(app, db)

    # 引入blog视图文件
    from app.blog import views as blog
    app.register_blueprint(blog.bp)

    # 注册数据库模型
    from app.blog import models

    return app
