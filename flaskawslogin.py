from awslogin import AwsCredentials
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/login-aws',methods = ['POST'])
def login_aws():
    if not request.json or 'access_key' not in request.json or 'secret_key' not in request.json or 'region_name' not in request.json:
        return jsonify({'error':'missing required login parameters'}),400
    access_key = request.json.get('access_key')
    secret_key = request.json.get('secret_key')
    region_name = request.json.get('region_name')

    aws_credentials = AwsCredentials(access_key=access_key,secret_key=secret_key,region_name=region_name)
    session = aws_credentials.login_aws()

    if session:
        return jsonify({'success':'aws logged successfully'}),200
    else:
        return jsonify({'error':'failed to connect aws '}),500

@app.route('close-aws-session',methods = ['GET'])
def close_aws_session():
    aws_credentials = AwsCredentials('','','')
    message = aws_credentials.close_aws_session

    return jsonify({'message':message}),200


if __name__ == '__main__':
    app.run(debug=False)