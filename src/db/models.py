#!/usr/bin/env python
from bson.json_util import dumps

from db import db
import json

class User(db.Document):
    ''' The data model'''
    handle = db.StringField(required=True)
    def as_dict(self):
        return {
            'id': json.loads(dumps(getattr(self,'pk')))['$oid'],
            'handle': getattr(self, 'handle')
        }