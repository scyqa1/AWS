import boto3

AWS_KEY="AKIAQEEOWQHEYXIE2JKU"
AWS_SECRET="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"
REGION="us-west-1"

print("Connecting to EC2")

ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY,
              aws_secret_access_key=AWS_SECRET,
              region_name=REGION)

ec2.create_tags(Resources=["i-06ae088a767a1285f"], Tags=[{'Key':'name', 'Value':'Project1'}])

