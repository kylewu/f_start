# pylint: disable=no-member,no-self-use

from flask_restplus import Namespace, Resource, fields, reqparse, abort
from flask import Flask, request

from services.user_service import get_users, post_user
from common.auth import login_required
import settings

api = Namespace('users', description='Users endpoints')

user_model = api.model('User', {
    'handle': fields.String(required=True, description='The user handle'),
})

user_model_list = api.model('User list', {
    'results': fields.List(cls_or_instance=fields.Nested(user_model), description='User'),
    'current_page': fields.Integer(description='Current page number'),
    'total_pages': fields.Integer(description='Total page number'),
    'per_page': fields.Integer(description='Number of results per page'),
    'total': fields.Integer(description='Total number of results'),
})

# pagination
pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument('page', type=int, required=False, default=1, location='args')
pagination_parser.add_argument('pageSize', type=int, required=False, default=settings.PER_PAGE, location='args')

user_model_parser = reqparse.RequestParser()
user_model_parser.add_argument('handle', type=str, required=True)
user_model_parser.add_argument('groups', type=list, required=False)


@api.route('')
@api.response(200, 'ok')
@api.response(400, 'Bad request')
@api.response(500, 'Internal server error')
class UserResource(Resource):
    """
    The User resource
    """

    @api.doc('Add User')
    @api.expect(user_model)
    @api.marshal_with(user_model, code=201, as_list=False)
    @login_required()
    @api.response(409, 'Conflict')
    def post(self):
        """
        Create User
        """
        user_model_parser.parse_args(strict=True)
        if not 'handle' in request.json:
            abort(400, 'handle could not be empty')  # message: xxx
        user = post_user(api.payload)
        return user, 201

    @api.doc('Get Users.')
    @api.marshal_with(user_model_list)
    @api.expect(pagination_parser, validate=True)
    def get(self):
        """
        List all Users, support pagination
        """
        args = pagination_parser.parse_args()
        if args.page and int(args.page) <= 0:
            abort(400, erros={'page': 'page must be positive integer'})
        if args.pageSize and int(args.pageSize) <= 0:
            abort(400, erros={'pageSize': 'pageSize must be positive integer'})

        return get_users()
