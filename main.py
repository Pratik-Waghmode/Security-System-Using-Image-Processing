import csv,cv2
import boto3
import data as data
from botocore.client import Config
#this script uploads the image from the local system to S3 bucket and the aws rekognition accesses the image from the S3 bucket and displays the results.
camera = cv2.VideoCapture(0)
image_name = ''
for i in range(1):
    return_value, image = camera.read()
    image_name = 'Camera_Capture'+str(i)+'.png'
    cv2.imwrite(image_name, image)
del(camera)


#enter your credentials
access_key = ""
secret_key = ""
image_path = 'E:/Cloud_Project/' + image_name
photo = image_path
print("*********")
print(photo)
client = boto3.client('rekognition',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key,
                      region_name='us-east-1')

# with open(photo, 'rb') as source_image:
#     source_bytes = source_image.read()

# response = client.detect_faces(Image={'S3OObject': {
#     'Bucket': 'pratik-cloud-bucket',
#     'Name': 'IMG001.jpg'
# }})

# s3 = boto3.resource('s3',
#                     aws_access_key_id=access_key,
#                     aws_secret_access_key=secret_key,
#                     config=Config(signature_version='s3v4')
#                     )
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-east-1'
)
s3 = session.resource('s3')
s3.meta.client.upload_file(Filename=photo, Bucket='pratik-cloud-bucket', Key=image_name)
print("done")

# response = client.detect_faces(
#     Image={
#         'Bytes': source_bytes
#     },
#     Attributes=['ALL'])

response = client.detect_faces(
    Image={
        'S3Object':{
            'Bucket': 'pratik-cloud-bucket',
            'Name': image_name
        }},
    Attributes=['ALL'])

print(response)