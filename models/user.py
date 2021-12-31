from db import db

class UserModel(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self,username,email) -> None:
        self.username=username
        self.email=email
    
    def json(self):
        return {'username':self.username, 'email':self.email}

   
    @classmethod
    def find_by_email(cls,email):
        return cls.query.filter_by(email=email).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()


    