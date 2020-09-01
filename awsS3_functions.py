import boto3

s3_client = boto3.client('s3')

def upload_file(file_name, bucket):
    object_name = file_name
    response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read'})
    return response


def get_url(file_name, bucket):
    location = s3_client.get_bucket_location(Bucket=bucket)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket, file_name)
    print(url)
    return url


















# def list_files(bucket):
#     """
#     Function to list files in a given S3 bucket
#     """
#     s3 = boto3.client('s3')
#     contents = []
#     try:
#         for item in s3.list_objects(Bucket=bucket)['Contents']:
#             print(item)
#             contents.append(item)
#     except Exception as e:
#         pass
#
#     return contents


# def download_file(file_name, bucket):
#     s3 = boto3.resource('s3')
#     output = f"downloads/{file_name}"
#     s3.Bucket(bucket).download_file(file_name, output)
#     return output
