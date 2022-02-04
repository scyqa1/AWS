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
Instance_ID = response['Instances'][0]['InstanceId']

print("Waiting for instance to be up and running")

response = ec2.describe_instances(InstanceIds=[Instance_ID])
status = response['Reservations'][0]['Instances'][0]['State']['Name']
print("Status: " + str(status))

while status == 'pending':
    sleep(10)
    response = ec2.describe_instances(InstanceIds=[Instance_ID])
    status = response['Reservations'][0]['Instances'][0]['State']['Name']
    print("Status: " + str(status))

if status == 'running':
    response = ec2.describe_instances(InstanceIds=[Instance_ID])
    print("\nInstance is now running. Instance details are:")
    print("Intance Type: " +
          str(response['Reservations'][0]['Instances'][0]['InstanceType']))
    print("Intance State: " +
          str(response['Reservations'][0]['Instances'][0]['State']['Name']))
    print("Intance Launch Time: " +
          str(response['Reservations'][0]['Instances'][0]['LaunchTime']))
    print("Intance Public DNS: " +
          str(response['Reservations'][0]['Instances'][0]['PublicDnsName']))
    print("Intance Private DNS: " +
          str(response['Reservations'][0]['Instances'][0]['PrivateDnsName']))
    print("Intance IP: " +
          str(response['Reservations'][0]['Instances'][0]['PublicIpAddress']))
    print("Intance Private IP: " +
          str(response['Reservations'][0]['Instances'][0]['PrivateIpAddress']))
