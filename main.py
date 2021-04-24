from flask import Flask, request
from databaseManagerRequest import databaseManagerRequest
import Constants

app = Flask(__name__)

@app.route('/', methods=['GET',])
def runDatabaseManager():
	requestType = request.args.get(Constants.GET_ARG_REQUEST_TYPE)
	requestType = requestType.text

	return databaseManagerRequest(requestType, request)