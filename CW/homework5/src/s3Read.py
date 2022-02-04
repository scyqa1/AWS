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

# Create the S3 object
obj = client.get_object(
    Bucket = 'project2-image',
    Key = 'static/text'
)
    
# Read data from the S3 object
data = pandas.read_csv(obj['Body'])
    
# Print the data frame
print('Printing the data frame...')
print(data)
