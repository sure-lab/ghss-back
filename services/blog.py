import re
from flask_restful import Resource
from models.blog import BlogModel
from flask import request
class Blog(Resource):
    
    def get(self):

        return {'blogs':list(map(lambda x:x.json(),BlogModel.query.all()))}
      
    def post(self):
        data=request.get_json()
        if BlogModel.find_by_title(data['title']):

            return {'message':'A blog with title {} already exists'.format(data['title'])},400

        blog=BlogModel(data['title'],data['content'],data['image'])
        try:
            blog.save_to_db()
        except:
            return {'message':'An error occurred inserting the blog.'},500

        return blog.json(),201

    def delete(self):
        data=request.get_json()
        blog=BlogModel.find_by_title(data['title'])

        if blog:
            BlogModel.delete_to_db()
        return {'message':'Blog deleted'}

class BlogFilter(Resource):
    def get(self,title):
        blog=BlogModel.find_by_title(title)
        if blog:
            return blog.json()
        return {'message':'Blog not found'},404





        



