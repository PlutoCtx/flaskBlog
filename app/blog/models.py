# @Version: python3.10
# @Time: 2023/7/6 14:36
# @Author: MaxBrooks
# @Email: 15905898514@163.com
# @File: models.py
# @Software: PyCharm
# @User: chent

from datetime import datetime
from RealProject import db


class Category(db.Model):
    """
        分类模型
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    icon = db.Column(db.String(128), nullable=True)
    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, )  # 创建时间

    pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # 更新时间

    def __repr__(self):
        return '<Category %r>' % self.name
