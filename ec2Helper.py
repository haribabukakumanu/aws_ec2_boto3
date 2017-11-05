import boto3


def getlistregions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    regions = response["Regions"]
    for region in regions:
        print region


def get_list_region_AZ():
    ec2 = boto3.client('ec2')
    response = ec2.describe_availability_zones()
    AvailabilityZones = response["AvailabilityZones"]

    for az in AvailabilityZones:
        print az


def get_list_key_pairs():
    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()

    KeyPairs = response.get('KeyPairs')
    for keypair in KeyPairs:
        print keypair


def get_list_of_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()
    SecurityGroups = response.get('SecurityGroups')
    for sg in SecurityGroups:
        print sg


def get_list_of_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    # print response
    Reservations = response.get('Reservations')
    for r in Reservations:
        Instances = r["Instances"]
        for item in Instances:
            # print item
            print "Instance ID's : {}".format(item["InstanceId"])

def terminate_instance(client, instanceids):
    response = client.terminate_instances(InstanceIds=instanceids)
    print response
    get_list_of_instances()

def create_key_pair(client, keyname):
    response = client.create_key_pair(
        KeyName=keyname
    )
    print response


def create_instance(client):
    amiid = 'ami-8c1be5f6'
    instancetype = 't2.micro'
    keypair = 'aws_boto3'

    response = client.create_instances(
        ImageId=amiid,
        InstanceType=instancetype,
        KeyName=keypair,
        MaxCount=1,
        MinCount=1,
    )

    print response

if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    # getlistregions()
    # get_list_region_AZ()
    # get_list_key_pairs()
    # get_list_of_security_groups()
    # get_list_of_instances()

    '''
    terminate_instance(ec2,['i-0776a879469dcd511',
                            'i-085df5180c7f26326'])
    '''

    #create_key_pair(ec2, "aws_sdk_boto3")

    ec2resource = boto3.resource('ec2')
    create_instance(ec2resource)
