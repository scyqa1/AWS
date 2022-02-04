import json
from datetime import date, datetime
import boto3


AWS_KEY = "AKIAQEEOWQHEYXIE2JKU"
AWS_SECRET = "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"
REGION = "us-west-1"


print("Connecting to EC2")
ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY,
                   aws_secret_access_key=AWS_SECRET,
                   region_name=REGION)

def json_datetime_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))



def describe(INSTANCE_ID):
    response = ec2.describe_instances(
        InstanceIds=[
            INSTANCE_ID,
        ],
    )

    print(f'Instance {INSTANCE_ID} attributes:')

    for reservation in response['Reservations']:
        print(json.dumps(
            reservation,
            indent=4,
            default=json_datetime_serializer
        )
        )

ec2_recourse = boto3.resource('ec2', aws_access_key_id=AWS_KEY,
                   aws_secret_access_key=AWS_SECRET,
                   region_name=REGION)
for i in ec2_recourse.instances.all():
    describe(i.id)
