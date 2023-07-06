# 01前言

本套教程命名为《**flask博客项目开发实战**》，开发这套教程的目的旨在免费分享知识，记录个人学习成果，梳理个人知识体系， 如若还有更高的使用价值，那便是希望能给初学flask的朋友、同学一些微末的参考！

本教程所载入的内容均来自个人学习的一些成果总结，可能会存在一些不准确、不规范之处，请各位参考学习的同学自行分辨！

教程内所有功能均未经严格测试，请勿用于生产环境，如若产生任何后果均与本人无关！

## **疑惑**

但凡对python Web开发感兴趣的同学，一般都应该知道django和flask框架，而初学者经常会有以下疑问？

**python web应该选django还是flask？**

这是很多初学者最爱纠结的问题，以网络比较流行的一个说法来回答这个问题，**“小孩子才做选择，大人是全都要”**，我个人觉得非常贴切。

为什么这么说？以成年人的视角，那就是学好框架去挣钱，会的多就挣得多，这是一个原因！

另外我们可以看看下边这组数据，截止我写这篇教程时django与flask在github的star数分别为64.1k和59k。 单从star数量就可以看出，这两个框架在python web方面所占的比例以及使用人群的广泛程度，更加印证了学好两个框架可以挣更多钱，有人用就有市场，有市场就有需求，有需求就有我们存在的意义！

当然这个又是小孩子的逻辑，但有时候成年人会把简单的问题复杂化，反而我个人认为小孩子的逻辑才是最睿智的！

## **建议**

以我个人的学习经验，特别是那种基础薄弱的人，别犹豫先从django开始学习，django相比flask是一个大而全的框架，它内置了开发网站基本上可以说所有的工具以及应用场景所给出的解决方案， 甚至python只要有一点点基础，就可以按照django的学习步骤做出项目，他的脚手架工具也会让我们对网站的基础布局以及网站开发的相关知识有更全面的认识和了解！

而flask是一个微框架，微即代表它内置的东西非常少，也使其更具灵活性，但越灵活的东西就越需要多的知识储备，更需要自己有更强的编程能力，很多功能需要自己去实现，或者依赖第三方框架， 过多的依赖第三方框架无疑会增加学习成本，同时项目的未来也会有很多不确定性，某个第三方依赖一旦爆出问题或者不再维护，也会直接影响到我们的项目。

这也不是说flask全是缺点，flask最大的优点就是轻量，简单。

这也就是为什么我说学完django再学flask，你反过来在flask中实现django的一些功能，就会更加有逻辑和意识，别抬杠，django中的很多内置的东西，flask开发网站都需要！

这也就是，网络上很多flask的教程往往会把某些知识点用django作为参考的原因所在！

## 适合人群

- 知道域名、端口等基础的概念
- 对python有基础的了解
- 有js、css、html基础
- 会用pip安装第三方库
- 会django更加完美

## 技术栈及工具

- python 3.10
- flask 2.1 版 - https://flask.palletsprojects.com/en/2.1.x/
- bulma css框架 - https://bulma.io/
- sqlit3
- vscode编辑器

# 02开始

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



# 03flask最简视图

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



# 04目录结构

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
def create_app(test_config=None):
    # create and configure the app
    # instance_relative_config 设置为True则代表开启文件加载配置，默认为False
    app = Flask(__name__, instance_relative_config=True)

    # app.config其实调用的是Flask类的config属性，该属性又被设置为了一个config的类
    # from_mapping则是该config类下的一个方法，用来更新默认配置，返回值为True
    # 至于Flask的默认配置都有哪些，其实可以深入源码查看default_config属性所列出的项
    # 默认配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABA5E=os.path.join(app.instance_path, "flaskr.sqlite"),
    )
    # 这里做了判断是否运行时传入了测试配置
    if test_config is None:
        # 如果没有传入，则从py文件加载配置，silent = True代表文件，文件加载成功则返回True
        app.config.from_pyfile('settings.py', silent=True)
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
    pass
```

2、实例化一个Flask对象，第一个参数_name_为必填参数，其意思请参照快速上手中的说明! 第二件关键字参数instance_relative_config是Flask类的一个默认参数，默认值为False，设置为True则代表开启从文件价和文件中加载配置!

```python
from flask import Flask
app = Flask(__name__, instance_relative_config = True)
```

3、为实例创建配置
app.config其实调用的是Flask类的config属性，该属性又被设置为了一个Config的类
from_mapping则是该Config类下的一个方法，用来更新配置，返回值为True
这个在这里就相当于为我们这个实例添加了一个默认的配置项
至于Flask的默认配置项都有哪些，其实可以深入源码查看default_config属性所列出的项

```python
import os
from flask import Flask
app = Flask(__name__, instance_relative_config = True)

app.config.from_mapping(
    SECRET_KEY = 'dev',
    DATABASE = os.path.join(app.instance_path,"flaskr.sqlite"),
)
```

4、以下代码对工厂函数传入的参数做了判断，起到切换配置的作用!

```python
from flask import Flask
app = Flask(__name__, instance_relative_config = True)
if test_config is None:
	#如果没有传入，则从py文件加载配置，silent=True代表文件，文件加截成功则返回True
	app.config.from_pyfile('settings.py', silent = True)
else:
	# 和最丹始的配兰意想一线
	app.config.from_mapping(test_config)
```

5、确保项目目录存在，递归创建目录，这个不太重要，了解即可52

```python
import os
from flask import Flask
app = Flask(__name__, instance_relative_config = True)
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
from flask import Blueprint
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
from flask import Flask
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

