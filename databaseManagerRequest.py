from FirebaseController import FirebaseController
import re
import time
import Constants


def databaseManagerRequest(requestType, request):

	success = True
	firebaseController = FirebaseController()
	queryResults = ''
	try:
		
	
			
			
		if requestType == Constants.REQUEST_TYPE_UPLOAD:

			originalUrlKeywords = request.args.get(Constants.GET_ARG_ORIGINAL_URL_KEYWORDS)

			kwicUrlKeywords = request.args.get(Constants.GET_ARG_KWIC_URL_KEYWORDS)

			noiseWords = request.args.get(Constants.GET_ARG_NOISE_WORDS)

			originalUrlKeywords = formatUploadUrlsKeywords(originalUrlKeywords)
			kwicUrlKeywords = formatUploadUrlsKeywords(kwicUrlKeywords)
			noiseWords = formatUploadNoiseWords(noiseWords)

			firebaseController.upload(originalUrlKeywords, kwicUrlKeywords, noiseWords)

		elif requestType == Constants.REQUEST_TYPE_QUERY:
			keywords = request.args.get(Constants.GET_ARG_KEYWORDS)

			keywords = formatKeywordsQuery(keywords)

			queryResults = firebaseController.getQueryResults(keywords)		

	except Exception:
		success = False

	finally:
		# Close the client connection after the try or except block
		if requestType == Constants.REQUEST_TYPE_QUERY:
			if success:
				return queryResults
			else:
				return Constants.SERVER_RESPONSE_QUERY_FAILURE
		else:
			if success:
				return Constants.SERVER_RESPONSE_UPLOAD_SUCCESS
			else:
				return Constants.SERVER_RESPONSE_UPLOAD_FAILURE



def formatUploadUrlsKeywords(UrlsKeywords):
	formattedUrlsKeywords = []
	UrlsKeywords = UrlsKeywords.split('\n')
	if UrlsKeywords[-1] == '': UrlsKeywords.pop()

	for i in range(len(UrlsKeywords)):
		lis = UrlsKeywords[i].split()
		url = lis[0]
		keywords = " ".join(lis[1:])
		formattedUrlsKeywords.append({Constants.ARG_URL : url, Constants.ARG_KEYWORDS: keywords})
		

	return formattedUrlsKeywords

def formatUploadNoiseWords(noiseWords):
	return noiseWords.split()


def formatKeywordsQuery(keywords):
	return keywords.split()
