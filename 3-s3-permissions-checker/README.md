# S3 Permissions Checker

## Overview

The **S3 Permissions Checker** is a Python-based tool designed to automate the process of checking the permissions on AWS S3 buckets. It helps verify if the correct permissions are set for each S3 bucket in your AWS account, ensuring security and compliance by providing a detailed report of the bucket permissions.

This project uses the AWS SDK for Python (`boto3`) to interact with the AWS S3 service and check various permissions associated with the buckets.

## Features

- Fetches a list of all S3 buckets in your AWS account.
- Checks the permissions for each bucket to ensure they comply with security best practices.
- Provides a detailed report on the permissions for each bucket.
- Easy to set up and use.

## Requirements

To run the **S3 Permissions Checker**, you need the following:

- Python 3.x
- AWS Account with S3 buckets
- IAM User with permissions to list and get information about S3 buckets (`s3:ListAllMyBuckets`, `s3:GetBucketAcl`)

### Required Libraries

The script requires the following Python libraries:

- `boto3` (AWS SDK for Python)
- `awscli` (for configuring AWS credentials)

You can install the required libraries using `pip`:

```bash
pip install boto3 awscli
```

---