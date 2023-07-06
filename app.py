# @Version: python3.10
# @Time: 2023/7/6 0:18
# @Author: MaxBrooks
# @Email: 15905898514@163.com
# @File: app.py.py
# @Software: PyCharm
# @User: chent

from RealProject import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
