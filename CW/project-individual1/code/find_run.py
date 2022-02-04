import boto3
from time import sleep

AWS_KEY = "AKIAQEEOWQHEYXIE2JKU"
AWS_SECRET = "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"
REGION = "us-west-1"


print("Connecting to EC2")

ec2 = boto3.resource('ec2', aws_access_key_id=AWS_KEY,
                   aws_secret_access_key=AWS_SECRET,
                   region_name=REGION)

for i in ec2.instances.all():
    if i.state['Name'] == 'running':
        print(i.id)