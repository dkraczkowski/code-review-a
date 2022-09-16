import uuid
import boto3
import json

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    body = json.loads(event["body"])
    data = client.put_item(
        TableName='user_updates_comments',
        Item={
            'comment_id': {
                'S': str(uuid.uuid4())
            },
            'comment': {
                'S': body["comment"]
            },
            'user_name': {
                'S': body["user_name"]
            }
        }
    )

    response = {
        'statusCode': 201,
        'body': 'successfully commented to an update!',
        'headers': {
            'Content-Type': 'application/json',
        },
    }

    return response
