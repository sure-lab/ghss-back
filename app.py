from flask import Flask
from flask_restful import Api
from services.blog import Blog, BlogFilter
from services.user import User,UserFilter
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)
@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(BlogFilter,'/blog/<string:title>')
api.add_resource(Blog,'/blog')
api.add_resource(User,'/user')
api.add_resource(UserFilter,'/user/<string:email>')

# if __name__ == "__main__":
print('test my code')
from db import db
db.init_app(app)
app.run(port=5000,debug=True)