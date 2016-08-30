"""
Amazon S3 utilities
"""
import boto3


class S3(object):
    """docstring for S3"""
    def __init__(self):
        super(S3, self).__init__()
        self.s3 = boto3.resource('s3')

    def get_buckets(self):
        return self.s3.buckets.all()

    def get_bucket(self, name):
        buckets = self.get_buckets()
        for bucket in buckets:
            if bucket.name == name:
                return bucket
