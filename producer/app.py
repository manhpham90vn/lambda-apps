import json
import boto3
import os

def lambda_handler(event, context):
    print(f"event: ${event}")
    print(f"context: ${context}")

    new_event = {'key': 'value'}
    response = send_event_to_sqs(new_event)
    return response

def send_event_to_sqs(event):
    sqs = boto3.client('sqs')
    queue_url = os.environ['QUEUE_URL']

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(event)
    )

    print(f"Sent new event to SQS: {response['MessageId']}")
    return response