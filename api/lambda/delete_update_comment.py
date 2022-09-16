import uuid
import boto3
import json

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    path_paramters = event["pathParameters"]
    comment_id = path_paramters["id"]

    data = client.delete_item(
        TableName='user_updates_comments',
        Item={
            'comment_id': {
                'S': comment_id
            }
        }
    )

    response = {
        'statusCode': 200,
        'body': f'successfully deleted comment {comment_id}',
        'headers': {
            'Content-Type': 'application/json',
        },
    }

    return response
