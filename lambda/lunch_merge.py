import json
import boto3
import os

MASTER_FILE = os.environ['masterFile']
MY_BUCKET = os.environ['myBucket']

def main(event, context):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(MY_BUCKET)
    objects_to_delete = []
    merged_data = read_file(s3, MASTER_FILE)

    #process all files in bucket
    for obj in my_bucket.objects.all():
        #skip the master file
        if obj.key != MASTER_FILE:
            objects_to_delete.append(obj.key)
            data = read_file(s3, obj.key)
            merge_record(merged_data, data)

    #save_master_file(s3, merged_data)
    print (merged_data)
    #cleanup(objects_to_delete)

    success = {"message": "Files were successfully merged.", "files": objects_to_delete}
    return success

def merge_record(merged_data, record):
    restaurant_found = False
    for restaurant in merged_data:
        #update restaurant data if it exists
        if restaurant['name'] == record['restaurant']:
            update_persons_likes(restaurant, record)
            restaurant_found = True
            break
    if not restaurant_found:
        #add the restaurant
        choices = {"person": record['name'], "likes": record['choices']}
        new_record = {"name": record['restaurant'], "choices": [choices]}
        merged_data.append(new_record)

def update_persons_likes(restaurant, record):
    person_found = False
    for choice in restaurant['choices']:
        #update the person's likes
        if choice['person'] == record['name']:
            choice['likes'] = record['choices']
            person_found = True
            break
    if not person_found:
        #add a new likes record
        new_record = {'person': record['name'], 'likes': record['choices']}
        restaurant['choices'].append(new_record)

def read_file(s3, filename):
    s3.Object(MY_BUCKET, filename).download_file('/tmp/file.json')
    return json.loads(open('/tmp/file.json').read())

def save_master_file(s3, merged_data):
    s3.Object(MY_BUCKET, MASTER_FILE).put(Body=merged_data)

def cleanup(s3, objects_to_delete):
    for obj in objects_to_delete:
        s3.delete_object(Bucket=MY_BUCKET, Key=obj)
