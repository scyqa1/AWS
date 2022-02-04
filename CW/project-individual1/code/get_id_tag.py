import boto3


AWS_KEY = "AKIAQEEOWQHEYXIE2JKU"
AWS_SECRET = "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"
REGION = "us-west-1"


print("Connecting to EC2")
ec2 = boto3.resource('ec2', aws_access_key_id=AWS_KEY,
                   aws_secret_access_key=AWS_SECRET,
                   region_name=REGION)


instances = ec2.instances.all()


for instance in instances:
    print(f'  - Instance ID: {instance.id};  Instance Tag: {instance.tags}')
