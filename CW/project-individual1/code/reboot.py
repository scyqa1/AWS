import boto3

AWS_KEY="AKIAQEEOWQHEYXIE2JKU"
AWS_SECRET="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"
REGION="us-west-1"

print("Connecting to EC2")

ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY,
              aws_secret_access_key=AWS_SECRET,
              region_name=REGION)

my_ec2_instance_id = 'i-06ae088a767a1285f' # add ec2 instance id but also best stored in env

def reboot_ec2(ec2_instance_id):
    response = ec2.reboot_instances(
        InstanceIds=[
            ec2_instance_id,
        ],
    )
    return response

reboot_ec2(my_ec2_instance_id)
