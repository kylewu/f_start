from flask_restplus import Api

from .users import api as user_api

api = Api(
    title='F2F API',
    version='1.0',
)

api.add_namespace(user_api, '/users')


@api.errorhandler(Exception)
def handle_exception(error):
    '''Return a custom message and 400 status code'''
    return {'message': f'Error: {error}'}, 400
