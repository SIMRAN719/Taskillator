from application.__init__ import db
from datetime import datetime

class credentials(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(20),nullable=False)
    data_created=db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"credentials('{self.name}','{self.email}')"
    
db.create_all()