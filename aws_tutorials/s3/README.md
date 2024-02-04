

In this project I practice CDK and SDK methods for setting up AWS resources.

I recognize that these resources could be easily created manually in the console or with other methods, but I personally wanted to practice the AWS developer tools for Python. 


The project starts from zero, where the only thing that has been done is create an AWS account and a user manually in the AWS Console. 

We will be using the Free S3 pricing tier which *should* support up to 5GB of storage, meaning that this project shouldnt incrue any additional expenses.


TODO: Write how we're testing both SDK and CDKs, because we want to test both. (Also write a line about the diffrence between the twoI)

The notebook TODO: Fill in name outlines the full discovery process of S3 infra with 

# Setup

## Prerequisites

- An AWS account + you have created an AWS user.
- Mac environment: If you use some other environment, you can use Google to access resources that execute similar configurations as outlined below. You can hence skip these instructions.
- [Homebrew](https://brew.sh/) for running CLI commands.


Again, remember that you can run these projects in what ever environment you choose, and as seen in this repo, I often also use, for example, conda.
However, below I have just written instructions for using virtual environment.
For instance, I believe conda manages the correct Python versions by default, and hence you do not need to worry about separately installing Python 3.11 as I do below.

## Creating a virtual environment

### 1. Installing Python 3.11

We are using a newer (as of 01/2024) version of Python to ensure that we have the latest versions of packages.
At this time Python 3.12 is already out but since it might not be as stable as 3.11, it is not favored.
You install Python 3.11 with `homebrew`: 

```
brew install python@3.11
```

You can verify installation with running `python3.11 --version`. For me the command returns `Python 3.11.7`.


### 2. Creating the venv

A new venv is created with the command `python3.11 -m venv <name_of_env>`.
So for this project I will create a venv `aws_tutorial`

```
python3.11 -m venv aws_tutorial
```

and it can be activated with `source`

```
source aws_tutorial/bin/activate
```

### 3. Install packages

The packages needed for all AWS tutorials in this project can be found in `aws_tutorials/requirements.txt`.
These can be installed with

```
pip install -r <path_to_requirements>
```

and you can verify the installed packages with `pip list`. The environment should be now ready to use.


## Configuring `boto3` 

`boto3` requires that you have your AWS Credentials setup before you can start using them. 
This you can do by with the CLI command `aws configure`.
This creates a prompt where you can input a user AWS Secret Access Key and AWS Secret Access Key ID. 
If you do not have them yet, you can create them in the AWS IAM Console (Google or Chat GPT has detailed instructions for that).

You should have a user to create the keys from. I named mine `s3-tutorials`, but you can choose any name.

## Deploying the CDK 


To deploy a CDK stack with Python, you need to follow these steps:

1. Install AWS CDK: AWS CDK is a Node.js package, so you need to install it using npm:

```
npm install -g aws-cdk
```

After installation you can check the installation with

```
which cdk
```
or
```
cdk --version
```

Note that if you dont already have the node package manager `npm` then you might need to install that as well. With MacOS, you can install this with brew: `brew install node`.

2. Test your S3 Stack by running 

```
cdk synth S3Stack -c config=XXX (CHECK LATER)
```

The synth command creates an CloudFormation template (JSON/YAML) showing what your infrastructre will contain.
It doesnt actually deploy the changes to AWS, but instead, creates the information file for the deploy. 
With synth we can see if the changes are actually deployable or if they will break something.

3. If the Synth goes to plan, we can finally deploy our Stack:

```
cdk deploy S3Stack -c config=XXX (CHECK LATER)
```

If we want to clean our infra, we can execute a cdk destroy command.