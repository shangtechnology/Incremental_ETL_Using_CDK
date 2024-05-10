import os
import boto3
import json
import base64
from decimal import Decimal

TABLE_NAME = os.environ["DYNAMO_TABLE_NAME"]


# data from kenisis is encoded for need decode
# cant write float to Dyanmo for convert to Decimal
# we need to convrt data to JSON
# we already specfied the key in other file
def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)

    for record in event["Records"]:
        payload = base64.b64decode(record["kinesis"]["data"])
        data = json.loads(payload.decode("utf-8"), parse_float=Decimal)
        data["ticker"] = data["from_currency_code"] + data["to_currency_code"]
        table.put_item(Item=data)
