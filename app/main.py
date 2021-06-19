import base64
import json
import logging
import os
import boto3
import pandas
from datetime import datetime

logger = logging.getLogger()
bucket_name = os.environ.get("bucket_name")
err_bucket_name = os.environ.get("err_bucket_name")


def get_s3_object():
    return boto3.client('s3')


def get_bucket(s3_client, bucket_name):
    return s3_client.get_bucket(bucket_name)


def get_record_key(date, source, timestamp):
    return f"processed_date={date}/source={source}/{timestamp}"


def push_to_s3(s3_bucket, key, parquet_processed_data):
    s3_bucket.upload_file(key, parquet_processed_data)


def lambda_handler(event, context, s3_client=get_s3_object()):
    # Get the object from the event and show its content type
    for record in event["Records"]:
        try:
            decoded_payload = base64.b64decode(
                record["kinesis"]["data"]
            ).decode("utf-8")
            # fmt: on
            payload = json.loads(decoded_payload)
            stream_item_list = []
            if type(payload) is not dict:
                payload = json.loads(payload)
            source = payload['source']
            if source is not None:
                source = "default"
            stream_item_list.append(payload)
            stream_item_data_frame = pandas.DataFrame.from_dict(stream_item_list)
            datetime_now = datetime.today()

            s3_client = get_s3_object()
            s3_bucket = get_bucket(s3_client, bucket_name)
            record = get_record_key(datetime_now.strftime('%Y-%m-%d'), source,
                                    datetime_now.strftime("%Y-%m-%d %H:%M:%S:%s"))
            push_to_s3(s3_bucket, record, stream_item_data_frame.to_parquet())

        except Exception as err:
            logger.error(f"Error while transforming data to paqrquet {err}")
            raise err
