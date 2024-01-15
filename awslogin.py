import boto3
#imported boto3 module


#aws lgin session
class AwsCredentials:
    def __init__(self,access_key,secret_key,region_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region_name = region_name
        self.session = None

    def login_aws(self):
        try:
            if not self.session:
                self.session = boto3.Session(
                    aws_access_key_id=self.access_key,
                    aws_secret_access_key=self.secret_key,
                    region_name=self.region_name
                )
            return self.session
        except Exception as e:
            return "Error in aws login"
    def close_aws_session(self):
        if self.session:
            self.session=None
            return "seccessfully closed aws session"
        else:
            return "No active aws sessions"
    