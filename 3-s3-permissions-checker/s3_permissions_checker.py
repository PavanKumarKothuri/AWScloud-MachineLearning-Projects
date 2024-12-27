import boto3
from botocore.exceptions import ClientError

def check_bucket_permissions(bucket_name):
    """
    Checks permissions for a specific S3 bucket.
    """
    s3 = boto3.client('s3')
    print(f"\n[+] Checking permissions for bucket: {bucket_name}")
    
    # Check bucket policy
    try:
        policy = s3.get_bucket_policy(Bucket=bucket_name)
        print("\nBucket Policy:")
        print(policy['Policy'])
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
            print("No bucket policy found.")
        else:
            print(f"Error fetching bucket policy: {e}")

    # Check bucket ACL
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        print("\nBucket ACL:")
        for grant in acl['Grants']:
            grantee = grant['Grantee']
            permission = grant['Permission']
            print(f"Grantee: {grantee.get('URI', grantee.get('DisplayName', 'Unknown'))}, Permission: {permission}")
    except ClientError as e:
        print(f"Error fetching bucket ACL: {e}")
    
    # Check bucket public access block
    try:
        public_access_block = s3.get_bucket_public_access_block(Bucket=bucket_name)
        print("\nPublic Access Block Configuration:")
        print(public_access_block['PublicAccessBlockConfiguration'])
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
            print("No public access block configuration found.")
        else:
            print(f"Error fetching public access block: {e}")

def list_buckets():
    """
    Lists all S3 buckets in the account.
    """
    s3 = boto3.client('s3')
    try:
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return buckets
    except ClientError as e:
        print(f"Error listing buckets: {e}")
        return []

if __name__ == "__main__":
    # Fetch all buckets
    print("Fetching all buckets in the AWS account...")
    buckets = list_buckets()
    
    if not buckets:
        print("No buckets found or unable to fetch bucket list.")
    else:
        print(f"Buckets found: {', '.join(buckets)}")
        # Check permissions for each bucket
        for bucket in buckets:
            check_bucket_permissions(bucket)
