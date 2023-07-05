# @Version: python3.10
# @Time: 2023/7/6 0:18
# @Author: MaxBrooks
# @Email: 15905898514@163.com
# @File: app.py.py
# @Software: PyCharm
# @User: chent

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
