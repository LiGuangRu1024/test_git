# @time     ：2024/8/15 15:05
# @author   : 莉光哈哈哈
# @file     : test61_cloud_computing.py
# @software : PyCharm
'''
Python与AWS S3交互
'''
import boto3


def list_buckets(s3_client):
    '''
    :param s3_client: 列出所有的S3存储桶
    :return:
    '''
    response = s3_client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]


def create_bucket(s3_client, bucket_name):
    '''
    :param s3_client: 创建一个新的s3存储桶
    :param bucket_name:
    :return:
    '''
    s3_client.create_bucket(Bucket=bucket_name)


def upload_file(s3_client, file_path, bucket_name, key):
    '''
    :param s3_client: 上传文件到s3
    :param file_path:
    :param bucket_name:
    :param key:
    :return:
    '''
    s3_client.upload_file(file_path, bucket_name, key)


def download_file(s3_client, bucket_name, key, destination_path):
    '''
    :param s3_client: 从s3下载文件
    :param bucket_name:
    :param key:
    :param destination_path:
    :return:
    '''
    s3_client.download_file(bucket_name, key, destination_path)


def delete_object(s3_client, bucket_name, key):
    '''
    :param s3_client: 删除s3中的对象
    :param bucket_name:
    :param key:
    :return:
    '''
    s3_client.delete_object(Bucket=bucket_name, Key=key)


def delete_bucket(s3_client, bucket_name):
    '''
    :param s3_client: 删除s3存储桶及其内容
    :param bucket_name:
    :return:
    '''
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    for obj in response.get('Contents', []):
        s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
    s3_client.delete_bucket(Bucket=bucket_name)


if __name__ == '__main__':
    s3_client = boto3.client('s3')

    # 创建一个新的存储桶
    bucket_name = 'example-bucket'
    create_bucket(s3_client, bucket_name)

    # 上传文件
    file_path = '/path/to/local/file.txt'
    key = 'file.txt'
    upload_file(s3_client, file_path, bucket_name, key)

    # 列出存储桶
    buckets = list_buckets(s3_client)
    print("Current buckets:", buckets)

    # 下载文件
    destination_path = '/path/to/download/file.txt'
    download_file(s3_client, bucket_name, key, destination_path)

    # 删除文件
    delete_object(s3_client, bucket_name, key)

    # 删除存储桶
    delete_bucket(s3_client, bucket_name)
