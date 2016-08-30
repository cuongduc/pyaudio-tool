"""
Upload audios to Amazon S3
"""
from __future__ import absolute_import
import os
import json

import boto3
from boto3.s3.transfer import S3Transfer


UPLOAD_FILE_INPUT = 'data/upload_list.json'
AWS_REGION = os.environ.get('AWS_REGION')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


def get_upload_file_list():
    with open(UPLOAD_FILE_INPUT, 'r') as f:
        raw = f.read()
        file_list = json.loads(raw)

        return file_list


def upload():
    client = boto3.client('s3', AWS_REGION,
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    transfer = S3Transfer(client)

    file_list = get_upload_file_list()
    for file in file_list:
        print('Begin uploading file %s' % file)
        local_path = 'data/%s' % file
        remote_path = 'uploads/audios/%s' % file
        transfer.upload_file(local_path, AWS_S3_BUCKET,
                             remote_path, extra_args={'ACL': 'public-read'})

        print('%s uploaded successfully!' % file)

if __name__ == '__main__':
    upload()
