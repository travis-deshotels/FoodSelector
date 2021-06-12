import json
import boto3
import os
import random


def choose_food(data):
    data_out = dict()
    data_out['choices'] = []

    restaurant = random.choice(data)
    data_out['restaurant'] = restaurant['name']

    for row in restaurant['choices']:
        data_out['choices'].append({'person': row['person'], 'choice': random.choice(row['likes'])})
    return data_out


def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    s3.Object(os.environ['myBucket'], os.environ['myDataFile']).download_file('/tmp/file.json')
    data = json.loads(open('/tmp/file.json').read())

    return choose_food(data)
