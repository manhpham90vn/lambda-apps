import json
import boto3
import os

def lambda_handler(event, context):
    print(f"Event: ${event}")
    print(f"Context: ${context}")

    for x in range(10):
        new_event = {'event': x}
        send_event_to_sqs(new_event)

    print("Done sending events to SQS")     

def send_event_to_sqs(event):
    sqs = boto3.client('sqs')
    queue_url = os.environ['QUEUE_URL']

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(event)
    )

    print(f"Sent new event to SQS: {response['MessageId']}")