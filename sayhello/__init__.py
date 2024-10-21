from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4
from flask_moment import Moment


app = Flask(__name__)
# 从文件中加载配置
app.config.from_pyfile('settings.py')
# 配置Jinja2的模板环境
app.jinja_env.trim_blocks = True #从渲染后的块的末尾去除空白行
app.jinja_env.lstrip_blocks = True #从渲染后的块的开始之前去除空白行

db = SQLAlchemy(app)
bootstrap = Bootstrap4(app) #使用flask_bootstrap简化页面调用bootstrap4框架
moment = Moment(app) #用以本地化日期和时间，初始化的同时，moment函数被写入模板上下文


#以防循环依赖导致异常，最后导入子模块
from sayhello import views, errors, commands