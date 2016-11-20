#!/usr/bin/env python3
import requests

def woof(BARK_TOKEN, message):
	'''
	preconditions:
		@param BARK_TOKEN is a valid Bark Partner API Token
		@param message is something the Bark Partner API will find meaningful
	postconditons:
		If the preconditions are met it will return the Bark Patner API's appraisal of @param message
		Otherwise it returns the HTTP Status Code of the request
	'''
	url = "https://partner.bark.us/api/v1/messages"
	headers = {"Content-Type" : "application/json; charset=utf-8",
				"X-Token-Auth" : BARK_TOKEN}
	data = {"message" : message}
	request = requests.post(url, json=data, headers=headers)

	'''
	preconditions:
		@BARK_TOKEN is a valid Bark Patner API Token
	postconditions:
		returns the response 
	'''
	if request.status_code == 200:
		return request.text
	else:
		return request.status_code