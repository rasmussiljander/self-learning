import yaml

import aws_cdk
from aws_cdk import App, Environment
# print(dir(aws_cdk))
pass
# from aws_cdk import core
from s3_stack import S3Stack


with open("env.yml", "r") as file:
    config = yaml.safe_load(file)

# app = core.App()
app = App()

# Set the default region for the CDK app
# app.region = config["region"]

env = Environment(
    region=config["region"]
)

S3Stack(app, "S3Stack", config=config, env=env)
app.synth()
