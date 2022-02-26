import requests
import boto3
import sys
import json

my-bucket = sys.argv[1]
endpoint = sys.argv[2]
auth = sys.argv[3]

s3 = boto3.resource('s3')
#clear s3 bucket
bucket = s3.Bucket(my-bucket)
for obj in bucket.objects.all():
        s3.Object(mybucket, obj.key).delete()

#push empty masterfile
#s3.Object(my-bucket, "food.json").put(Body="")

headers = {'x-api-key': auth, 'Content-Type': 'application/json'}
#put some files
choices = [ 'steak' ]
data = {'name': 'me', 'restaurant': 'test', 'choices': choices}
requests.put(endpoint, json.dumps(data), headers=headers)
choices = [ 'eggs' ]
data = {'name': 'you', 'restaurant': 'test', 'choices': choices}
requests.put(endpoint, json.dumps(data), headers=headers)

#confirm number of files

#merge
#requests.delete(endpoint, headers=headers)

#confirm number of files

#get request
#requests.get
