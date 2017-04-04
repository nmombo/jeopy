# jeopy.py
# Python module for interpreting texts from app.py and scraping J!-Archive.

# Author: Noah Momblanco
#         http://github.com/nmombo/jeopy
# Date: 3/29/2017

from lxml import html
import requests
import re

def response(sms):
	'''Main parsing function for app.py

	Recieves sms message that was sent to twilo number and decides what action
	to perform. Then, this returns a reply that will be sent via sms.

	Args:
		sms: string that contains the message sent to the twilio number

	Returns:
		reply: string that contains the message to be sent as a reply to the
			app user

	'''

	# print the incoming message to the server terminal
	print sms

	# if incoming message is the initializing message "START"
	if removeEndingWhiteSpace(sms) = 'START':
		reply = 'temp: start message received'
	# if incoming message is the closing message "STOP"
	elif removeEndingWhiteSpace(sms) = 'STOP':
		reply = 'temp: close message received'
	else:
		reply = 'temp: other message received'

	return reply

def removeEndingWhiteSpace(str):
	while(str[str.length() - 1] == ' ' or str[str.length() - 1] == '\n'):
		str = str[:str.length() - 1]
	return str
