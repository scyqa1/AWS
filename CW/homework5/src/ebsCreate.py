import boto3
import pandas

# Creating the low level functional client
client = boto3.client(
    'ebs',
    aws_access_key_id = 'AKIAQEEOWQHERBBHGYMW',
    aws_secret_access_key = '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',
    region_name = 'us-west-1'
)


client.start_snapshot(
    VolumeSize=1
)

