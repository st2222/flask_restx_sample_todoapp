import awsgi
# import simplejson as json
from src.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
