import json
import boto3
import os
from random import randint

def choose_restaurant(data):
    x = randint(0,len(data)-1)
    return data[x]

def choose_food(data):
    data_out = dict()
    data_out['choices'] = []

    restaurant = choose_restaurant(data)
    data_out['restaurant'] = restaurant['name']

    for row in restaurant['choices']:
        likes_count = len(row['likes'])
        choice = randint(0, likes_count-1)
        data_out['choices'].append({'person': row['person'], 'choice': row['likes'][choice]})
    return data_out

def lambda_handler(event, context):
    #download data from S3
    s3 = boto3.resource('s3')
    s3.Object(os.environ['myBucket'], os.environ['myDataFile']).download_file('/tmp/file.json')
    data = json.loads(open('/tmp/file.json').read())

    return choose_food(data)