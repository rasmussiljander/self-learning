from aws_cdk import (
    aws_iam as iam,
    core
)

class S3Stack(core.Stack):
    def __init__(self, config, scope: core.Construct, id: str) -> None:
        super().__init__(scope, id)


        self.arn_base = f"arn:aws:iam::{config['arn_number']}"

        # Define the IAM role
        my_role = iam.Role(
            self,
            config['role_name'],
            role_name=config['role_name'],
            description='Role for S3 practice',
            assumed_by=iam.ArnPrincipal(f"{self.arn_base}:root")
        )
