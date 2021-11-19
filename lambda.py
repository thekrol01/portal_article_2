import boto3
def lambda_handler(event, context):
  cf_client = boto3.client('cloudformation')
  cf_client.create_stack(
    StackName='CF-wordpress-pipeline-from-lambda',
    TemplateURL='https://my-s3-source-pipeline-cb.s3.us-east-1.amazonaws.com/basic-pipeline.yml',
    Capabilities=[
        'CAPABILITY_IAM','CAPABILITY_NAMED_IAM'
    ],
    Parameters=[
        {
        'ParameterKey':'PipelineName',
        'ParameterValue':'CP-project-A'
        },
        { 
        'ParameterKey':'S3Bucket',
        'ParameterValue':'my-cb-source-bucket-bk'
        },
        {
        'ParameterKey':'SourceS3Key',
        'ParameterValue':'wordpress-single-instance.zip' 
        },
        {
        'ParameterKey':'TemplateFileName',
        'ParameterValue':'wordpress-single-instance.yaml'
        },
        {
        'ParameterKey':'TestStackName',
        'ParameterValue':'Test-MyWordPressSite'
        },
        {
        'ParameterKey':'ProdStackName',
        'ParameterValue':'Prod-MyWordPressSite-cb'
        },
        {
        'ParameterKey':'Email',
        'ParameterValue':'bert.krol@icloud.com'
        },
    ],
)


import json

import json

def lambda_handler(event, context):
    # TODO implement
    passed_param = ''
    for content in event["queryStringParameters"]:
        print(f'key: {content}')
        print(f'value: {event["queryStringParameters"][content]}')
        passed_param += event["queryStringParameters"][content] + ' '
    return {
        'statusCode': 200,
        'body': json.dumps(passed_param)
    }

Parameters=[
        {
        'ParameterKey':'PipelineName',
        'ParameterValue':'CP-project-A'
        },
        { 
        'ParameterKey':'S3Bucket',
        'ParameterValue':'my-cb-source-bucket-bk'
        }]


print(Parameters[0]['ParameterKey'], Parameters[0]['ParameterValue'])