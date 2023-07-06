# @Version: python3.10
# @Time: 2023/7/6 11:30
# @Author: MaxBrooks
# @Email: 15905898514@163.com
# @File: views.py
# @Software: PyCharm
# @User: chent

from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/hello')
def index():
    return 'Hello World!'