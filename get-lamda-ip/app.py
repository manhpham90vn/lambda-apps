import json
import requests


def lambda_handler(event, context):
    print(f"event: ${event}")
    print(f"context: ${context}")

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        print(f"error: ${e}")
        raise e

    return {
        "data": json.dumps({
            "location": ip.text.replace("\n", "")
        })
    }
