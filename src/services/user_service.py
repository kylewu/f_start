#!/usr/bin/env python
import math

from db.models import User

def get_users():
    '''
    Get all entities
    :returns: all entity
    '''
    page = 1
    pageSize = 10
    users = User.objects()
    return {
        'results': users[(page - 1) * pageSize: page * pageSize],
        'current_page': page,
        'total_pages': math.ceil(1.0 * len(users) / pageSize),
        'per_page': pageSize,
        'total': len(users)
    }

def post_user(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''
    user = User(**body).save()
    return user
