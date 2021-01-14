import json

import boto3


if __name__ == '__main__':

    with open('../../configuration.json') as f:
        configuration = json.load(f)
    with open('../../template_webflow_aws.yaml') as f:
        template_body = f.read()
    client = boto3.client('cloudformation')

    response = client.create_stack(
        StackName=configuration['stack_name'],
        TemplateBody=template_body,
        TimeoutInMinutes=5,
        Capabilities=['CAPABILITY_IAM'],
        OnFailure='DO_NOTHING',
        Parameters=[
            {
                'ParameterKey': 'BucketName',
                'ParameterValue': configuration['bucket_name']
            },
            {
                'ParameterKey': 'SupportBucketName',
                'ParameterValue': configuration['support_bucket_name']
            }
        ]
    )
    print(response)