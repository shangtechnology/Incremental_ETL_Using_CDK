#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags

from kinesis_stream.kinesis_stream_stack import KinesisStreamStack
from data_producer.data_producer_stack import DataProducerStack
from data_consumer.data_consumer_stack import DataConsumerStack
from s3_bucket.s3_bucket_stack import S3BucketStack
from decouple import config


AWS_REGION=config("AWS_REGION")

env_AWS_Region = cdk.Environment(account="", region=AWS_REGION)
app = cdk.App()

kinesis_stream = KinesisStreamStack(app, "KinesisStreamStack", env=env_AWS_Region)
data_producer = DataProducerStack(app, "DataProducerStack", env=env_AWS_Region)
data_consumer = DataConsumerStack(app, "DataConsumerStack", env=env_AWS_Region)
s3_bucket = S3BucketStack(app, "S3BucketStack", env=env_AWS_Region)

Tags.of(app).add("ProjectOwner", "Alex-Clark")
Tags.of(app).add("ProjectName", "Crypto_incremental-Pipeline")

app.synth()
