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