import boto3
def upload_files(file_name, bucket,object_name=None, args=None):
    s3=boto3.client('s3')
    if object_name is None:
        object_name=file_name

    response=s3.upload_file(file_name,bucket,object_name, args)
    print(response)