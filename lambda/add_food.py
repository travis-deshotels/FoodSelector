import json
import boto3
import os

def main(event, context):
    s3 = boto3.resource('s3')
    if not is_valid_data(event):
        return {'Error': 'Bad syntax! Please include name, restaurant, and choices!'}

    #write input data to file
    with open('/tmp/file', 'w') as outfile:
        json.dump(event, outfile)

    #S3 put file
    try:
        s3.Object(os.environ['myBucket'], event['name'] + ".json").put(Body=open('/tmp/file', 'rb'))
    except:
        error_message = {'Error': 'Unable to save file'}
        return error_message
    return {"message": "file saved"}

def is_valid_data(event):
    try:
        print ("Input contains:")
        print ("name" + event['name'])
        print ("restaurant" + event['restaurant'])
        print ("choices" + event['choices'])
        return True
    except (KeyError):
        return False
