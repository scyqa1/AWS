import boto3


AWS_KEY = "AKIAQEEOWQHEYXIE2JKU"
AWS_SECRET = "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"
REGION = "us-west-1"


print("Connecting to EC2")
ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY,
                   aws_secret_access_key=AWS_SECRET,
                   region_name=REGION)

response = ec2.describe_instances()

# iterate over each host.
for each_res in response['Reservations']:
    for each_inst in each_res['Instances']:
        # I set this matchhost as a flag as I iterate through each host.
        matchhost = True
        # On each host, I iterate through all the tags on the host.

        # Now that I've run through all tags on this 1 host, if I matched the values, then I create a new tag.
        if matchhost:
            response = ec2.create_tags(
                Resources=[each_inst['InstanceId']],
                Tags = [
                    {
                        'Key': 'name',
                        'Value': 'Project1'
                    }
                ]
            )