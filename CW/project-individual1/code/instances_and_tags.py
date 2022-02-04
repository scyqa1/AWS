import boto3
from time import sleep

AWS_KEY = "AKIAQEEOWQHEYXIE2JKU"
AWS_SECRET = "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"
REGION = "us-west-1"
AMI_ID = "ami-011996ff98de391d1"
EC2_KEY_HANDLE = "Project1KeyPair"
INSTANCE_TYPE = "t2.micro"
SECGROUP_ID = "sg-0aeffd14f430d4848"

print("Connecting to EC2")

ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY,
                   aws_secret_access_key=AWS_SECRET,
                   region_name=REGION)

print("Launching instance with AMI-ID %s, with keypair %s, \
     instance type %s, security group \
     %s" % (AMI_ID, EC2_KEY_HANDLE, INSTANCE_TYPE, SECGROUP_ID))

response = ec2.run_instances(ImageId=AMI_ID,
                             KeyName=EC2_KEY_HANDLE,
                             InstanceType=INSTANCE_TYPE,
                             SecurityGroupIds=[SECGROUP_ID, ],
                             MinCount=1,
                             MaxCount=1)

print(response)
Instance_ID1 = response['Instances'][0]['InstanceId']
ec2.create_tags(Resources=[Instance_ID1], Tags=[{'Key':'name', 'Value':'Project1_1'}])

response = ec2.run_instances(ImageId=AMI_ID,
                             KeyName=EC2_KEY_HANDLE,
                             InstanceType=INSTANCE_TYPE,
                             SecurityGroupIds=[SECGROUP_ID, ],
                             MinCount=1,
                             MaxCount=1)

print(response)
Instance_ID2 = response['Instances'][0]['InstanceId']
ec2.create_tags(Resources=[Instance_ID2], Tags=[{'Key':'name', 'Value':'Project1_1'}])

response = ec2.run_instances(ImageId=AMI_ID,
                             KeyName=EC2_KEY_HANDLE,
                             InstanceType=INSTANCE_TYPE,
                             SecurityGroupIds=[SECGROUP_ID, ],
                             MinCount=1,
                             MaxCount=1)

print(response)
Instance_ID3 = response['Instances'][0]['InstanceId']
ec2.create_tags(Resources=[Instance_ID3], Tags=[{'Key':'name', 'Value':'Project1_1'}])

response = ec2.run_instances(ImageId=AMI_ID,
                             KeyName=EC2_KEY_HANDLE,
                             InstanceType=INSTANCE_TYPE,
                             SecurityGroupIds=[SECGROUP_ID, ],
                             MinCount=1,
                             MaxCount=1)

print(response)
Instance_ID4 = response['Instances'][0]['InstanceId']
ec2.create_tags(Resources=[Instance_ID4], Tags=[{'Key':'name', 'Value':'Project1_2'}])

response = ec2.run_instances(ImageId=AMI_ID,
                             KeyName=EC2_KEY_HANDLE,
                             InstanceType=INSTANCE_TYPE,
                             SecurityGroupIds=[SECGROUP_ID, ],
                             MinCount=1,
                             MaxCount=1)

print(response)
Instance_ID5 = response['Instances'][0]['InstanceId']
ec2.create_tags(Resources=[Instance_ID5], Tags=[{'Key':'name', 'Value':'Project1_2'}])