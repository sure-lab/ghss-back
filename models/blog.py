from db import db

class BlogModel(db.Model):
    __tablename__='blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    content = db.Column(db.String(),nullable=False)
    image=db.Column(db.String())

    def json(self):
        return {'title':self.title,'content':self.content,'image':self.image}

    def __init__(self,title,content,image) -> None:
        self.title=title
        self.content=content
        self.image=image

    def find_by_title(title):
        return BlogModel.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()