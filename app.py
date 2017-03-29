# app.py
# App that will allow you to play the most recent jeopardy game after you
# request it via text.

# Author: Noah Momblanco
#         http://github.com/nmombo/jeopy
# Date: 3/29/2017

from jeopy import *
from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient
import urllib

myTwilioSID = 'ACd7173182fbfbee0265e86f88929fb005'
myTwilioToken = 'secret'
client = TwilioRestClient(account=myTwilioSID, token=myTwilioToken) 
app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def inbound_sms():
	response = twiml.Response()
	response.message(jeopy.response(request.form(['Body'])))
	return str(response)