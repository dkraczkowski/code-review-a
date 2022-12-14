import json
import boto3

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    data = client.scan(
        TableName='user_updates'
    )

    response = {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

    return response
