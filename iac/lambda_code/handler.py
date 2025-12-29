import json
import os
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    timestamp = datetime.utcnow().isoformat()

    humidity = event.get("humidity", "unknown")
    action = event.get("action", "none")

    table.put_item(
        Item={
            "timestamp": timestamp,
            "humidity": str(humidity),
            "action": action
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Event stored",
            "timestamp": timestamp
        })
    }
