from aws_cdk import aws_iam as iam, aws_s3 as s3, core


class S3Stack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # # Create a new S3 bucket
        # bucket = s3.Bucket(self, "MyBucket")

        # Create a new IAM role
        role = iam.Role(self, "MyRole", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        # Add list bucket permissions to the role
        role.add_to_policy(
            iam.PolicyStatement(
                actions=["s3:ListBucket"],
                resources=[bucket.bucket_arn],
            )
        )
