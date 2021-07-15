# from package.MovieTable import create_movie_table, put_item
import boto3
import flask
import time
from botocore.exceptions import EndpointConnectionError

application = flask.Flask(__name__)

@application.route('/')
def home():
	start = time.time()
	client = boto3.client('sts')
	while (time.time() - start < 300):
		try:
			identity = client.get_caller_identity()
			return identity['Arn']
		except EndpointConnectionError:
			time.sleep(5)
			continue

if __name__ == '__main__':
	application.run(debug=True)