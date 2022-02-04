import boto3
from time import sleep

AWS_KEY="AKIAQEEOWQHE3H2OHTNL"
AWS_SECRET="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"
REGION="us-west-1"

INSTANCE_TYPE="db.t2.micro"
ID="MySQL-db-instance"
USERNAME='root'
PASSWORD='password'
DB_PORT=3306
DB_SIZE=5
DB_ENGINE='mysql'
DB_NAME='mytest'
SECGROUP_ID='sg-06c43b0d'

print("Connecting to RDS")

rds = boto3.client('rds', aws_access_key_id = AWS_KEY, aws_secret_access_key = AWS_SECRET, region_name = REGION)

print ("Creating an RDS instance")

response = rds.create_db_instance(DBName = DB_NAME, DBInstanceIdentifier = ID, AllocatedStorage = DB_SIZE, DBInstanceClass = INSTANCE_TYPE, Engine = DB_ENGINE, MasterUsername = USERNAME, MasterUserPassword = PASSWORD, Port = DB_PORT)

print (response)
print ("Waiting for instance to be up and running")

sleep(30)
response = rds.describe_db_instances(DBInstanceIdentifier = ID)
status = response['DBInstances'][0]['DBInstanceStatus']

while not status == 'available':
  sleep(10)
  response = rds.describe_db_instances(DBInstanceIdentifier = ID)
  status = response['DBInstances'][0]['DBInstanceStatus']
  print ("Status: " + str(status))

if status == 'available':
  response = rds.describe_db_instances(DBInstanceIdentifier = ID)
  print ("\nRDS Instance is now running. Instance details are:")
  print ("Instance ID: " + str(response['DBInstances'][0]['DBInstanceIdentifier']))
  print ("Instance Status: " + str(response['DBInstances'][0]['DBInstanceStatus']))
  print ("Instance Type: " + str(response['DBInstances'][0]['DBInstanceClass']))
  print ("Engine: " + str(response['DBInstances'][0]['Engine']))
  print ("Allocated Storage: " + str(response['DBInstances'][0]['AllocatedStorage']))
  print ("Endpoint: " + str(response['DBInstances'][0]['Endpoint']))
