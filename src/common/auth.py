from functools import wraps

from flask import Flask, request
from flask_restplus import abort

from db.models import User


def login_required(roles=None):
    
    def outter(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if 'Authorization' not in request.headers:
                abort(code=401, message="401")

            user = request.headers['Authorization']

            if not User.objects(handle=user):
                abort(code=401, message="not exist")

            return func(*args, **kwargs)

        return wrapper
    return outter


