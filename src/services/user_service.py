#!/usr/bin/env python
from models.user import User
from config import db
from werkzeug.exceptions import NotFound

def get():
    '''
    Get all entities
    :returns: all entity
    '''
    return User.objects()

def post(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    user = User(**body).save()
    return user
