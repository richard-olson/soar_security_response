import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# import boto3
# import mypy_boto3_ec2 as ec2
# import time
# import os


# from botocore.exceptions import ClientError


# def lambda_handler(event, context):

#     ec2_client: ec2.EC2Client = boto3.client("ec2", region_name="us-east-1")
#     ec2_resource: ec2.EC2ServiceResource = boto3.resource("ec2", region_name="us-east-1")

#     ec2_client.
    # ec2 = boto3.client("ec2")
    # ec2_resource = boto3.resource("ec2")
    # # getting VPC ID
    # response = ec2.describe_vpcs()
    # vpc_id = os.environ["VPC_ID"]  # response.get('Vpcs', [{}])[1].get('VpcId', '')


    # print (vpc_id)

    # # Creating security group

    # try:
    #     response = ec2.create_security_group(GroupName='SOAR_IsolatedSG',
    #                                          Description='Isloated security group for infected instances',
    #                                          VpcId=vpc_id)
    #     security_group_id = response['GroupId']
    #     print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    #     security_group = ec2_resource.SecurityGroup(security_group_id)

    #     time.sleep(2)   # Delays for 2 seconds so that SG is ready for tagging below

    #     tag = security_group.create_tags(
    #         Tags=[
    #             {
    #                 'Key': 'Name',
    #                 'Value': 'IsolatedSG'
    #             },
    #         ]
    #     )

    # # configuring SG to let only Forensic WS to connect
    #     data = ec2.authorize_security_group_ingress(
    #         GroupId=security_group_id,
    #         IpPermissions=[
    #             {'IpProtocol': 'tcp',
    #              'FromPort': 3389,
    #              'ToPort': 3389,
    #              'IpRanges': [{'CidrIp': '172.16.0.11/32'}]},
    #             {'IpProtocol': 'tcp',
    #              'FromPort': 22,
    #              'ToPort': 22,
    #              'IpRanges': [{'CidrIp': '172.16.0.11/32'}]}
    #         ])

    #     print('Ingress Successfully Set %s' % data)

    #     # changing the security group ofthe infected instance, please create environment variable
    #     instance = ec2_resource.Instance(os.environ['Compromised_Instance_ID'])

    #     response = instance.modify_attribute(Groups=[security_group_id])

    #     # storing security group id in SSM parameter store to be used later

    #     client = boto3.client('ssm')
    #     sg = client.put_parameter(
    #         Name='/SOAR/BI/SG_ID',
    #         Description='Storing isloation security group ID',
    #         Value=security_group_id,
    #         Type='String',
    #         Overwrite=True,
    #         )

    #     print('success')

    # except ClientError as e:

    #     print(e)

    # return {
    #     'message' : 'success'

    # }
