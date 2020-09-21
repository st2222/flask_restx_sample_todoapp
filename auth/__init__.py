from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

import boto3
from botocore.exceptions import ClientError
import awsgi
# import simplejson as json

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API',
          )
ns = api.namespace('/auth', description='Auth operations')


@ns.route('/change_pass')
class AuthController(Resource):
    def post(self):
      print(api.payload)
      cognito_idp = boto3.client('cognito-idp')
      username = 's07065024217@ezweb.ne.jp'
      user_pool_id = api.payload['user_pool_id']
      client_id = api.payload['client_id']
      old_password = api.payload['old_password']
      new_password = api.payload['new_password']

      response = cognito_idp.admin_initiate_auth(
          UserPoolId=user_pool_id,
          ClientId=client_id,
          AuthFlow='ADMIN_NO_SRP_AUTH',
          AuthParameters={'USERNAME': username, 'PASSWORD': old_password},
      )
      print("response→　", response)
      session = response['Session']
      # パスワードを変更する。
      response = cognito_idp.admin_respond_to_auth_challenge(
          UserPoolId=user_pool_id,
          ClientId=client_id,
          ChallengeName='NEW_PASSWORD_REQUIRED',
          ChallengeResponses={'USERNAME': username, 'NEW_PASSWORD': new_password},
          Session=session
      )

      return response


if __name__ == '__main__':
    app.run(debug=True)


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
