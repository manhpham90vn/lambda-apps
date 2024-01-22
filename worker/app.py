import json
import requests

def lambda_handler(event, context):
    print(f"event: ${event}")
    print(f"context: ${context}")

    sqs_event = json.loads(event['Records'][0]['body'])
    print(f"sqs_event: ${sqs_event}")

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
        print(f"ip: ${ip.text}")
    except requests.RequestException as e:
        print(f"error: ${e}")
        raise e

    return {
        "data": json.dumps({
            "event": sqs_event,
            "location": ip.text.replace("\n", "")
        })
    }
