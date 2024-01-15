from flask import Flask,jsonify,request

from awslogin import AwsCredentials
app = Flask(__name__)


def list_s3_objects():
    access_key = request.json.get('access_key')
    secret_key = request.json.get('secret_key')
    region_name = request.json.get('region_name')
    bucket_name = request.json.get('bucket_name')
    file_name = request.json.get('file_name')
    aws_credentials = AwsCredentials(access_key=access_key,secret_key=secret_key,region_name=region_name)

    s3_client = aws_credentials.login_aws().client('s3')

    response = s3_client.get_object(Bucket=bucket_name,Key=file_name)
    data = response['Body'].read().decode('utf-8')

    return jsonify({"s3-FileData":data})

