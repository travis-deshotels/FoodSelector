import json
import boto3
import os

def main(event, context):
    s3 = boto3.resource('s3')

    #write input data to file
    with open('/tmp/file', 'w') as outfile:
        json.dump(event, outfile)

    #S3 put
    try:
        s3.Object(os.environ['myBucket'], event['name'] + ".json").put(Body=open('/tmp/file', 'rb'))
    except:
        error_message = {'Error': 'Unable to save file'}
        return error_message
    return_obj = {"message": "file saved"}
    return return_obj