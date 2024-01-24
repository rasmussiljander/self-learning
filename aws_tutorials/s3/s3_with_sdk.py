import boto3

# Create an S3 client
s3 = boto3.client("s3")

# Create a new S3 bucket
s3.create_bucket(Bucket="MyBucket")

# Create an IAM client
iam = boto3.client("iam")

# Create a new IAM role
role = iam.create_role(
    RoleName="MyRole",
    AssumeRolePolicyDocument='{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},"Action":"sts:AssumeRole"}]}',
)

# Add list bucket permissions to the role
iam.put_role_policy(
    RoleName="MyRole",
    PolicyName="MyPolicy",
    PolicyDocument='{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"s3:ListBucket","Resource":"arn:aws:s3:::MyBucket"}]}',
)
