#encoding:utf-8
#http://www.mwsoft.jp/programming/python/python_aws.html
# https://qiita.com/ketancho/items/6d5137b48d94eced401e

import boto3
from PIL import Image
# client = boto3.client(
#     's3',
#     aws_access_key_id="AKIAJUSXPMR4ZEZHKI3A",
#     aws_secret_access_key="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"
#     # aws_session_token=SESSION_TOKEN,
# )
s3=boto3.resource("s3")
# boto3.DEFAULT_SESSION

# for bucket in s3.buckets.all():
#     print(bucket)


bucket=s3.Bucket("photofortweet")
# obj=bucket.Object("forbot/001.jpg")
obj=bucket.Object("forbot/001.jpg")
# print(obj.content_type)
print(type(obj))

# response=obj.get()
# print(type(response))

image=obj
image=Image.open(obj)
# image.show()
# obj_jpg=Image.open(bucket.Object("forbot/001.jpg"),"r")


# for key in bucket.objects.all():
#     print(key)




# S3上のファイルをダウンロードする
# bucket.download_file(Key='forbot/041.jpg', Filename='photofortweet')
