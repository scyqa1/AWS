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

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
