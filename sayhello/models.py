from datetime import datetime, timezone
from sayhello import app, db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)#default传入函数对象，意在传入写入数据库记录时调用该函数，而非建表时调用
    


