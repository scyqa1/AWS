import boto3
import pandas

# Creating the low level functional client
client = boto3.client(
    'efs',
    aws_access_key_id = 'AKIAQEEOWQHEXQGR5C5C',
    aws_secret_access_key = '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',
    region_name = 'us-west-1'
)


client.delete_file_system(
    FileSystemId='fs-05adc37d783b6392d'
)
