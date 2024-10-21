'''
在单独的文件中定义配置时
可以不使用config字典对象添加配置
而是使用键值对的形式给出
'''
import os, sys
from sayhello import app

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///' #windows 系统使用///
else:
    prefix = 'sqlite:////' #否则使用////


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
