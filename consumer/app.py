import json
import requests
import random

def lambda_handler(event, context):
    print(f"Event: ${event}")
    print(f"Context: ${context}")
    sqs_event = json.loads(event['Records'][0]['body'])
    print(f"SQS Event: ${sqs_event}")

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        print(f"IP: ${ip.text}")
    except requests.RequestException as e:
        print(f"Error Get IP: ${e}")
        raise e

    # allow for error testing
    if (sqs_event['event'] == 5):
        print(f"Error at ${sqs_event}")
        raise Exception(f"Error {sqs_event}")

    randomError = bool(random.getrandbits(1))
    if (randomError):
        print(f"Error at ${sqs_event}")
        raise Exception(f"Random error {sqs_event}")

    print(f"Done ${sqs_event}")