from mongo import mongo
from bson import json_util
from bson.objectid import ObjectId

import json


def cursor_to_list(cursor):
    result = []
    for item in cursor:
        item['id'] = str(item['_id'])
        item.pop('_id')
        result.append(item)
    return result


def find_by_textscore(text):
    cursor = mongo.db.QnA.find(
        {'$text': {'$search': text}},
        {'score': {'$meta': 'textScore'}})

    cursor.sort([('score', {'$meta': 'textScore'})])
    return cursor


def find_by_asin(asin):
    cursor = mongo.db.qna.find({'asin': asin})
    result = cursor_to_list(cursor)
    return result


def find_by_id(object_id):
    cursor = mongo.db.qna.find({'_id': ObjectId(object_id)})
    result = cursor_to_list(cursor)
    return result


def find_by_asin_with_textscore(asin='', text=''):
    cursor = mongo.db.qna.find(
        {'$text': {'$search': text}, 'asin': asin},
        {'score': {'$meta': 'textScore'}})
    result = cursor_to_list(cursor)
    return result
