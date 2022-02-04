import boto3
import pandas

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id = 'AKIAQEEOWQHEXQGR5C5C',
    aws_secret_access_key = '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',
    region_name = 'us-west-1'
)

# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIAQEEOWQHEXQGR5C5C',
    aws_secret_access_key = '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',
    region_name = 'us-west-1'
)

# Creating a bucket in AWS S3
location = {'LocationConstraint': 'us-west-1'}
client.create_bucket(
    Bucket ='hw5-demo-1',
    CreateBucketConfiguration= location
)

