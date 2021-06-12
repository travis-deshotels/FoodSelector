import json
import boto3
import os


def main(event, context):
    if not is_valid_data(event):
        return {'Error': 'Bad syntax! Please include name, restaurant, and choices!'}
    write_data_to_file(event)
    if not copy_to_s3(event['name']):
        return {'Error': 'Cannot save to S3 bucket!'}
    return {"message": "file saved"}


def copy_to_s3(name):
    try:
        s3 = boto3.resource('s3')
        s3.Object(os.environ['myBucket'], name + ".json").put(Body=open('/tmp/file', 'rb'))
    except:
        return False


def write_data_to_file(event):
    with open('/tmp/file', 'w') as outfile:
        json.dump(event, outfile)


def is_valid_data(event):
    try:
        print("Input contains:")
        print("name" + event['name'])
        print("restaurant" + event['restaurant'])
        print("choices" + event['choices'])
        return True
    except KeyError:
        return False
