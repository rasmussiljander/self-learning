import json

from aws_cdk import Stack, Environment #Construct
import aws_cdk.aws_iam as iam
import aws_cdk.aws_s3 as s3
import aws_cdk

# print(dir(aws_cdk))

"""
Without previous AWS CLI use, you are by default using the root user. This has all access by default, 
but using it is not considered best practice, as you cannot limits its permissions. 

Therefore, you should have created a user to configure AWS CLI to before you start. Now, at this point, 
I could create the user with AWS CLI or equivalent by configuring the root user to the CLI, and later change to 
assume the created user, but for this purpose it is just easier for me to create the user manually in the console 
(attach instructi0ons for how to create the user.)

1. Create user
    either attach policies immediately when creating or attach them later (i will do this)

2. Create Access Keys 

3. User AWS configure to set ups access keys

4. Create a policy and attach it to the user.




If you get an error msg similar to this

S3Stack: SSM parameter /cdk-bootstrap/hnb659fds/version not found. Has the environment been bootstrapped? Please run 'cdk bootstrap' (see https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html)

you need to bootstrap, a.k.a setup the correct resources in the correct account and region. This can be done with 
```
cdk bootstrap
```

Usually like this
 aws://<account>/<region>

but we have already set them up with aws configure so cdk should be able to fetch correct values.




In addition, there might be some minor issues with cloud states, but solving them should be easy,
 as cdk deployment is well-documented by aws.

TODO: Describe policies in json


For production purposes one would definitely create more fine-tuned cloudformation policies, 
also ensuring that resources are not setup, updated, or destroyed during wrong situations.
"""

class S3Stack(Stack):
    def __init__(self, scope, id: str, config: dict, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.arn_base = f"arn:aws:iam::{config['arn_number']}"

        # # Create an IAM user
        # s3_user = iam.User(self, config['user_name'])

        # # get policy
        # policy = self.get_json_policy_from_file("../user_policy.json")

        # # # Create an IAM policy from the JSON document
        # policy_document = iam.PolicyDocument.from_json(policy)

        # s3_user_policy = iam.Policy(self, "UserPolicy", document=policy_document)

        # # Attach the custom inline policy to the user
        # s3_user.attach_inline_policy(policy=s3_user_policy)


        # Create the S3 role
        # s3_role = iam.Role(
        #     self, config["role_name"],
        #     description="Role for S3 practice",
        #     assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        # )
        s3_role = iam.Role(
            self, config["role_name"],
            assumed_by=iam.AccountPrincipal(config["user_name"])
        )

        # Create an S3 bucket for staging
        staging_bucket = s3.Bucket(self, "StagingBucket")

        # Grant necessary permissions to the staging bucket
        staging_bucket.grant_read_write(s3_role)

        # policy_for_role = {
        #     "Version": "2012-10-17",
        #     "Statement": [
        #         {
        #             "Effect": "Allow",
        #             "Principal": {"AWS": f"{self.arn_base}:root"},
        #             "Action": ["sts:AssumeRole"]
        #         }
        #     ],
        # }

        # role_policy = iam.PolicyStatement(
        #     effect=iam.Effect.ALLOW,
        #     actions=["sts:AssumeRole"],
        #     principals=[iam.ArnPrincipal(f"{self.arn_base}:root")],
        #     resources=[s3_role.role_arn]
        # )
        # # Attach the policy to the IAM role
        # s3_role.add_to_policy(
        #     role_policy
        # )

        # assert 1 == 0

    def get_json_policy_from_file(self, path):
        with open(path) as f:
            policy = json.load(f)
        return policy
