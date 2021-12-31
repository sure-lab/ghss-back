import re
from flask import request
from flask_restful import Resource
from models.user import UserModel
class User(Resource):

    def get(self):
        return list(map(lambda x:x.json(),UserModel.query.all()))

    def post():
        data=request.get_json()
        user=UserModel.find_by_email(data['email'])
        if UserModel.find_by_email(data['email']):
            return {'message':'A blog with title {} already exists'.format(data['email'])},400
        user=UserModel(data['username'],data['email'])
        try:
            user.save_to_db()
        except:
             return {'message':'An error occurred inserting the user.'},500
        return user.json(),201
    
    def delete(self):
        data=request.get_json()
        user=UserModel.find_by_email(data['email'])

        if user:
            UserModel.delete_to_db()
        return {'message':'User deleted'}

class UserFilter(Resource):

    def get(self,email):
        user=UserModel.find_by_email(email)
        if user:
            return user.json()
        return {'message':'user not found'},404

