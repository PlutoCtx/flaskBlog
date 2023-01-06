# 开始

请在开始前确保系统已经正确安装python，且版本大于3.7

## 创建虚拟环境

**macOS/Linux系统**

```
mkdir flaskBlog
cd flaskBlog
python3 -m venv venv
```

**windows系统**

```
mkdir flaskBlog
cd flaskBlog
py -m venv venv
```

创建了项目文件夹venv环境文件夹

## 激活虚拟环境

**macOS/Linux系统**

```
venv/bin/activate
```

**windows系统**

```
venv\Scripts\activate
```

shell提示符将更改为显示激活的环境的名称

## 安装flask

在激活的环境中，使用以下命令安装Flask

```
pip install Flask
```

在安装flask的同时也自动安装了Werkzeug/Jinja/MarkupSafe/ltsDangerous/Click四个依赖!

- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/)实现了WSGl，这是应用程序和服务器之间的标准Python接口。
- Jinja 是一种模板语言，用于呈现应用程序所服务的页面。
- MarkupSafe附带了Jinja。它在呈现模板时转义不受信任的输入，以避免注入攻击。
- ltsDangerous安全地对数据进行签名，以确保其完整性。这用于保护 Flask 的会话 Cookie。
- Click是用于编写命令行应用程序的框架。它提供命令并允许添加自定义管理命令。

pip freeze > req.txt



# flask最简视图

首先创建一个app.py 的文件，以开始我们下来的操作

## 新增app.py文件

现在我们的目录结构看起来像下边这样:

```
flaskBlog
venv
app.py
```

## 创建视图

app.py中写入如下所示代码

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,World!</p>"
```

这就是一个最小的flask应用程序，当我们这个文件默认为 app.py 的时候，我们甚至都不需要配置环境变量就可以使用flask run 的命令来启动该项目!

## 运行项目

在终端运行flask run命令，将启动flask自带的开发服务器，终端输出如下所示:

```
Environment: productionWARIIING: This is a development server. Do not use it in a production deployment.Use a production WSGI server instead.

Debug mode: off

Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

看到这样的信息，即代表启动成功，在浏览器访问该5000端口的地址，即可看到页面会正确输出 He110，word!

## 代码详解

**上边这些代码都做了什么?**

1. 首先，我们导入了Flask类
2. 创建Flask的实例，传入name 其实是给Flask的第一个参数赋值，第一个参数是应用程序模块或包的名称。这个参数是必须的，这里就得需要大家具备一些python的知识，知道_name作为python的内置变量，在什么情况下代表什么，返回值是什么，需要大家自行去了解下!(当然，有阅读源码能力的朋友完全可以看下Flask的源码就明白了!)
3. 函数视图hello_world的route0装饰器是告诉 Flask 哪个URL应该触发我们的函数
4. 函数视图hello_world的返回值默认类型为html，因此浏览器可以自动识别我们的字符串中传入的html元素!

这些 其实就是flask的核心内容，其他的都是在这个基础上使其更加易用来不断新增和添加的一些高级方法，当然本教程不是flask的入门教程，不会对其逐一仔细的讲解，下来我们将直接进入博客的实战环节!



# 目录结构

为保证项目可持续发展，利于后期扩展，我们从开始创建项目就应该先规划好目录结构，一个好的目录结构可以让我们的项目整洁有序，并利于维护和后期进一步扩展!
之前快速上手中创建的app.py的文件便可以删除，亦或者你重新创建一个项目开始以下的内容，建议是新建一个目录来开始我们以下的内容!

## 创建应用目录(app)

在实际开发过程中，一个完整的项目一定是由多个不同的功能模块构成，以我们的博客系统为例，主要由两个大的功能模块构成，一个是负责用户认证以及用户权限操作的模块auth,一个则是我们博客的主应用模块blog，他主要负责博客的内容/分类等一些与博客相关的功能!

为了实现以上需求，我们就需要现在虚拟环境venv的同级目录新建一个app的目录，用这个目录来统一管理各功能模块，并在其内部分别新建auth和blog目录,结构如下所示!

```
__init__py
    /auth
        __init__.py
    /blog
        __init__.py__
```

从以上目录可以看出，我们在每一个文件夹下都内置了一个___init__.py的文件，使其变成一个可互相调用的模块!

## 创建项目目录(RealProject)

为了区别app目录和RealProject目录，我们将分别称起名为 应用目录(app)，项目目录(RealPproject)，在以后的教程中出现对应的字眼请自行甄别和区分!

在app的同级我们创建一个Realproject 的目录，并分别在其内部创建init.py、 settings.py、 wsgi.py三个文件,目录结构如下:

```
/RealProject
    __init__.py
    settings.py
    wsgi.py
```

## 创建入口文件(manage.py)

最后，我们将创建一个manage.py入口文件作为我们整个项目的入口，最后我们只需要运行该文件即可启动我们的项目!

最后，我们完整的目录结构将如下所示:

```
/flaskBlog
    /app
        __init__.py
        /auth
        	__init__.py
    /blog
    	__init__.py
    /RealProject
        __init__.py
        settings.py
        wsei.py
    /venv
```

熟悉django的同学肯定会对这个目录结构不会陌生，本目录结构本身也就是参照django的目录结构来构造!

# 05工厂函数

无论是一个单文件项目还是一个多功能禅块的大型项目，我们始终应该明白，Flask 应用程序是 Flask 类的一个实例。
基于此，那么第一件事就是实例化一个Flask对象!

创建 Flask 应用程序最直接的方法是直接在代码顶部创建一个全局 Fask 实例，就像我们快速上手中的那样!

在大型项目中这种做法是行不通的，而是在一个函故内创建它。此函效被称为应用程序工厂，简称-工厂函数。应用程序所需的任何配置、注册和其他设置都将在函数内部进行，然后应用程序将被返回。

## 创建工厂函数

在项目目录(RealProject)目录下的_init_.py中创建如下代码:

```python
import os
from flask import Flask
def create_app(testconfie = None):

    # create and confiqure the app
    ## instance_relative_config 设置为True则代表开启文件加载配置，默认为False
    app = Flask(__name__, instance_relative_config = True)
    
    # app.config其实调用的是Flask类的config属性，该属性又被设置为了一个config的类
    ## from_mapping则是该config类下的一个方法，用来更新默认配置，返回值为True
    ## 至于Flask的默认配置都有哪些，其实可以深入源码查看default_config属性所列出的项
    # 默认配置
    
    app.config.from_mapping(
        SECRET_KEY='dev",
        DATABA5E = os.path.join(app.instance_path,"flaskr.sqlite")
    # 这里做了判断是否运行时传入了测试配置
    if test_config is None:
        # 如果没有传入，则从py文件加载配置，silent = True代表文件，文件加载成功则返回True
        app.config.from_pyfile('settings.py',silent=True)
    else:
        # 和最开始的配置意思一致
        app.config.from_mapping(test_config)
    
    # 递归创建目录，确保文件项目存在
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app
```



## 代码详解

以上注释在注释中已经有详细说明，但这里有必要再对每一行代码做详细注意解释，顺序依次从上往下。

1、创建一个create_app的函数，并默认传入test_config的参数，默认值为None

```python
def create_app(test_config=None):
```

2、实例化一个Flask对象，第一个参数_name_为必填参数，其意思请参照快速上手中的说明! 第二件关键字参数instance_relative_config是Flask类的一个默认参数，默认值为False，设置为True则代表开启从文件价和文件中加载配置!

```python
app = Flask(__name__, instance_relative_config = True)
```

3、为实例创建配置
app.config其实调用的是Flask类的config属性，该属性又被设置为了一个Config的类
from_mapping则是该Config类下的一个方法，用来更新配置，返回值为True
这个在这里就相当于为我们这个实例添加了一个默认的配置项
至于Flask的默认配置项都有哪些，其实可以深入源码查看default_config属性所列出的项

```python
app.config.from_mapping(
    SECRET_KEY = 'dev',
    DATABASE = os.path.join(app.instance_path,"flaskr.sqlite"),
)
```

4、以下代码对工厂函数传入的参数做了判断，起到切换配置的作用!

```python
if test_config is None:
	#如果没有传入，则从py文件加载配置，silent=True代表文件，文件加截成功则返回True
	app.config.from_pyfile("settings.py', silent = True)
else:
	# 和最丹始的配兰意想一线
	app.config.from_mapping(test_config)
```

5、确保项目目录存在，递归创建目录，这个不太重要，了解即可52

```python
try:
    os.makedirs(app.instance_path)
except OSError:
    pass
```



# 06Flask蓝图应用



## 什么是蓝图

蓝图是一个对象，它允许在不需要应用程序对象的情况下定义应用程序函数，它使用与Flask相同的装饰器，但通过记录它们以供以后注册来推迟对应用程序的需求

## 创建蓝图

学过django的同学应该都知道，应用的视图函数一般都写在应用目录下的views.py中，没学过django也无关紧要，在应用目录app文件夹下创建一个views.py的文件，这里用来集中存储blog的视图代码。

通过蓝图创建一个比克首页的基本视图，代码如下：

```python
from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix = '/blog')

@bp.route('index/')
def index():
    return 'Hello World!'
```

## 代码详解

1、首先引入了蓝图对象，这个蓝图Blueprint与Flask类是

```python
from flask import Blueprint
```

2、实例化一个蓝图对象，需要两个必须参数，第一个是应用的名称，第二个__name__是该应用的位置，其他参数都是可选的，我们这里用关键字参数url_prefix = '/blog'指定了该应用的一个url的命名空间，和django的urls中的app_name类似，这个值会出现在该应用url之前，比如我们现在这个url访问的话应该是：http://127.0.0.1:5000/blog/index/

```python
bp = Blueprint('blog', __name__, url_prefix='/blog')
```

3、创建了blog应用的一个视图，用蓝图实例来绑定route，把该url定义在该应用当中

```python
@bp.route("index/")
def index():
    return render_template()
```



## 注册蓝图

上边我们就说了，这个应用通过蓝图创建，如果不去项目注册的话，他是不会被运行的，这就要我们去工厂函数中注册蓝图

首先，把该views文件引入到blog的__init_.py文件中，以便后续调用

```python
# app/blog/__init__.py
from . import views
```

最后，在项目目录的__init__.py中的工厂函数中通过app实例的提供的register_blueprint方法注册蓝图，代码如下：

```python
def create_app(test_config = None):
    
    app = Flask(__name__, instance_relative_config = True)
    # ... 省略部分代码
    
    # 注册博客蓝图
    from app.blog import views as blog
    app.register_blueprint(blog.bp)
    
    return app
```



## 定义入口

在入口文件manage.py中引入以下代码，代码非常简单，不做过多解释

```python
from RealProject import create_app

app = create_app()

# 当运行这个文件的时候才执行run()方法
if __name__ == '__main__':
    app.run(debug = True)
```



## 运行项目

在终端运行该文件即可成功启动项目，默认我们设置了run方法的debug模式为True，也就是开启了Flask的调试模式

```cmd
py manage.py
```

返回如下内容，说明启动成功

```
 * Serving Flask app 'RealProject'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://192.168.43.127:8000

```

在浏览器我们访问刚才定义的url，[127.0.0.1:8000/blog/hello/index](http://127.0.0.1:8000/blog/hello)



# 07Flask-SQLAlchemy

Flask-SQLAlchemy是Flask 的扩展，它为您的应用程序添加了对 SQLAlchemy 的支持。它旨在通过提供有用的默认值和额外的帮助程序来简化将SQLAlchemy与Flask 结合使用，从而更轻松地完成常见任务。

这是官方的介绍，其实对于刚想写个简单博客的同学来说，这个东西说了等于没说，因为他不知道SQLAIchemy是什么?能干什么?所以自然对以上这段话就无从理解!

我这里简单说一下，无论是博客类网站还是更大的商城类网站，我们在页面上所看到的数据都是存储在数据库，那数据库主要分为关系型数据库和非关系型数据库，那么，如何把数据存储到数据库以及如何把数据库中的数据查询到页面，也就是所谓的增删改查操作，我们都要用到sq语法，当然这又是另外的一个知识点，学起来也是非常的繁琐复杂，那为了我们快速实现增删改查的目的，有大佬就创作了这样一个框架，使用了一种叫做《Object Relation Mapping》对象关系映射的技术，也就是我们所说的ORM，这个在django框架中是自带的，但与SQLAIchemy框架的用法及底层实现有一些区别。这个我们无需去过多关注，我只要知道SQLAIchemy的API提供了执行数据库CRUD操作的方法，因此我们不必在程序中编写复杂难懂的原始SQL语句，就可以达到增删改查的目的。

那么，Flask-SQLAlchemy是对SQLAIchemy的进一步封装，使得更加容易的在Flask项目中使用SQLAIchemy!

## 安装Flask-SQLAlchemy

```bash
pip install Flask-SQLAlchem
或者
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask-sqlalchemy
```

- 官方文档:https://flask-sqlalchemy.palletsprojects.com/en/2.x/

## 使用

1、在项目目录(RealProject)的 init .py中引入SQLAlchemy

```bash
#RealProject/init.py
from flask_sqlalchemy import SQLAlchemy
#安装SQLAlchemy对象
db= SQLAlchemy()
```

2、在工厂函数create_app中与app绑定关系

```python
def create_app(test_config = None):
    # create and configure the app
    app =  Flask(name, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    #绑定数据库
    db.init_app(app)
    # ..省略部分代码
    
    return app
```

3、创建模型数据

这一节我们来先创建一个博客的分类模型数据来认识一下模型的创建。

在app/blog/models.py 中创建模型如下

```python
from datetime import datetime
from RealProject import db

class Category(db.Model):
	'''
		分类模型
	'''

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)
	icon = db.Column(db.String(128), nullable=True)
	add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, )  # 创建时间

	pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # 更新时间

	def __repr__(self):
		return '<Category %r>' % self.name
```

学习过django的同学有没有一股熟悉的味道，和django的创建模型是不是非常相似，只是一些语法上的不同!

我们一起来看下这些字段都做了什么?

- id 该模型的主键，类型为integer，primary_key为True代表主键
- name 分类名称，String类型，可变字符类型，映射到数据库中是varchar类型
- icon 分类图标，类型与name一致，区别是nullable=True,就是允许为空，即默认值是null
- add_date 创建时间，nullable=False不能为空，default=datetime.utcnow设置为当前时区时间
- pub_date 更新时间，主要关注下onupdate=datetime.utcnow,这个可以更新每次编辑时的时间保存

其他更多的类型，我们在以后用到的时候再去了解，基本的类型我也整理了一篇文章，大家可以参考! 类型参考:http://wwwlotdoc.cn/blog/detail/172/









## 配置MySQL数据车

我们最开始已经说过了项目的默认配置在工厂函数中已经引入了,以下就是项目的默认配置

```python
app.config.from_mapping(
    SECRET_KEY = 'dev',
    DATABASE = os.path.jin(app.instance_path,'flaskr.sqlite'),
)
```

但是，一般的做法是配置和代码是区别开的，我们现在要让他从文件中读取配置，所以就直接删除这句，或者注释掉即可，最开始引入是为了介绍Flask加载配置文件的几种方法!

现在我们把所有的配置项移动到项目目录的settings.py文件中，配置如下

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
SECRET_KEY = '1%3ya7fn3moipdpcltj(tdfcv5^@lj=t5d&72levvls+y*@4^'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/flaskdb'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
```

以上几项配置是连接数据库必须的配置，其中SQLALCHEMY_DATABASE_URI就是链接mysq/数据库的url，第一个root是用户名，冒号后的root是密码，3306是mysql数据库默认的端口号，最后一个flaskdb则是数据库名

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 操作数据库
db = SQLAlchemy()

def create_app(test_config = None):
   
    app = Flask(__name__, instance_relative_config = True)

    # 这里做了判断是否运行时传入了测试配置
    if test_config is None:
        CONFIG_PATH = BASE_DIR / 'RealProject/settings.py'
        app.config.from_pyfile(CONFIG_PATH, silent=True)
    else:
        # test_config是一个字典
        app.config.from_mapping(test_config)

    db.init_app(app)

    # 递归创建目录，确保文件项目存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 引入blog的视图文件
    from app.blog import views as blog
    app.register_blueprint(blog.bp)
    return app

from app.blog import models
```



做完以上步骤，如果你的数据库没有问题的话，就已经可以连接到数据库了，但是字段此时还并没有同步到数据库，同步字段到数据库的方法是，进入Flask的shell环境，运行以下两个命令即可:

```bash
from RealProject import db
db.create_all()
```

但是，要进入Flask的shell环境需要先在终端设置项目的环境变量，我这里以Windows系统和本项目为例CMD终端，运行如下命令，即可进入shell环境

```bash
set FLASK_APP = "RealProject"
set FLASK_ENV = "development" 
flask shell
```

Powershel终端，运行如下命令，即可进入shell环境

```bash
$env:FLASK_App = "RealProject"
$env:FLASK_ENV = "development"
flask shell
```

但是，我们不采用这种方法去同步数据库，下一章我们将采用Flask的另外一个扩展Flask-Migrate来同步数据库，他可以进行数据库的版本控制，比如你数据库某些字段已经有了默认数据，他不会去清空重建，而是会进行新增操作，类似于django的makemigrations和migrate两个命令所做的事情!



# 08Flask-Migrate

Flask-Migrate 是一个扩展，他是Alembic的进一步封装，以更好的适配Flask和Flask-SQLAlchemy 应用程序。就实际的数据库迁移而言，所有内容都由Alembic处理，因此您可以获得完全相同的功能。

Alembic 是一款轻量型的数据库迁移工具，它与SQLAIchemy 一起共同为 Python 提供数据库管理与迁移支持。

## 安装Flask-Migrate

```bash
pip install Flask-Migrate
```

## 配置Flask-Migrate

1、首先在工厂函数所在文件中引入

- 路径: RealProject/init.py

```python
from flask_migrate import Migrate
migrate = Migrate()
```

2、在工厂函数中注册,最终

```python
def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    
    # 省略部分代码
    
    db.init_app(app)
    
    # 注册migrate
    migrate.init_app(app, db)
   
    # 省略部分代码
    return app
```

最终，完整的工厂函数如下：

```python
def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)

    if test config is None:
        CONFIG_PATH = BASE_DIR/'RealProject/config.pyapp.config.from_pyfile(CONFIG PATH，silent=True
    else:
        #和最开的配程应思一级
        app.config.from_mapping(test_config)
    db.init_app(app)
    migrate.init_app(app, db)

    #遵归创建目实，确你项目文件存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    #注册视图
    from app.blog import views as blog
    app.register_blueprint(blog.bp)

    #注册模华
    from app.blog import models

    return app
```



## 使用Flask-Migrate

在上一节最后我们说过，需要导出项目的环境变量，才能使用flask的命令，因此在执行以下操作之前，记得先导出环境变量哦!

在此之前，我们已经创建好了一个博客的分类模型，并且将模型数据阴茎在工厂函数中注册

接下来，我们就可以使用以下命令创建迁移存储库

```bash
flask db init
```

这会将迁移文件夹添加到应用程序中。此时，你可以发现项目目录多了一个migrations的文件夹，下边的versions目录下的文件就是生成的数据库迁移文件!

然后，运行以下命令生成迁移

```bash
flask db migrate
```

做完这两步就完成了第一次的初始迁移操作，我们可以看数据库已经有了我们创建的模型字段

之后，每次在新增和修改完模型数据之后，只需要执行以下两个命令即可

```bash
falsk db migrate
flask db upgrade
```

到这里，基本上我们的项目最基本的配置就已经做完了，后边章节我们将开始真正的业务编写，Flask因其自身的灵活性，大部分的东西都得依靠第三方，所以前期的项目配置以及文件夹结构每个人的理念不同，自然设计出来的结构也是不同的，所以这就非常考验python的基础和能力，因此上，再开始项目之前，我们队python的相关基础知识一定要掌握的比较扎实，做起来才可能会更加轻松!

