from flask_restful import Api, Resource, marshal_with, fields

api=Api(prefix='/api')

blog_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'caption': fields.String,
    'image_url': fields.String,
    'user_id': fields.Integer,
    'timestamp': fields.DateTime,
}

class BlogAPI(Resource):
    pass

api.add_resource(BlogAPI, '/blogs/<int:blog_id>')