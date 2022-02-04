import boto3
import pandas

# Creating the low level functional client
client = boto3.client(
    'efs',
    aws_access_key_id = 'AKIAQEEOWQHEXQGR5C5C',
    aws_secret_access_key = '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',
    region_name = 'us-west-1'
)


client.create_file_system(
    CreationToken='efs-demo1',
    Tags=[
        {
            'Key': 'aws',
            'Value': 'efs-demo1'
        },
    ]
)
