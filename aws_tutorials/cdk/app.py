from aws_cdk import (
    aws_iam as iam,
    core
)
from s3_stack import S3Stack
import yaml

import yaml

with open('env.yaml', 'r') as file:
    config = yaml.safe_load(file)

app = core.App()
S3Stack(app, "MyStack")
app.synth()
