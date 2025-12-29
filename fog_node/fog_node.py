import boto3
import random
import json
from datetime import datetime, timezone

lambda_client = boto3.client("lambda")

HUMIDITY_THRESHOLD = 40  # porcentaje

def read_humidity():
    return random.randint(20, 80)

def decide_irrigation(humidity):
    return "ON" if humidity < HUMIDITY_THRESHOLD else "OFF"

def send_to_cloud(humidity, action):
    payload = {
        "humidity": humidity,
        "action": action,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    response = lambda_client.invoke(
        FunctionName="irrigation_cloud_handler",
        InvocationType="RequestResponse",
        Payload=json.dumps(payload)
    )

    print("Cloud response:", response["StatusCode"])

def main():
    humidity = read_humidity()
    action = decide_irrigation(humidity)

    print(f"Humidity: {humidity}% → Irrigation: {action}")

    send_to_cloud(humidity, action)

if __name__ == "__main__":
    main()
