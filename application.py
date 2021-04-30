# from package.MovieTable import create_movie_table, put_item
import boto3
import flask

application = flask.Flask(__name__)

@application.route('/')
def home():
  client = boto3.client('sts')
  identity = client.get_caller_identity()

  return identity['Arn']

if __name__ == '__main__':
  application.run(debug=True)