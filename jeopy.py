from Game import Game

# jeopy.py
# Python module for interpreting texts from app.py and scraping J!-Archive.

# Author: Noah Momblanco
#         http://github.com/nmombo/jeopy
# Date: 3/29/2017

def jResponse(sms, myGame):
	'''Main parsing function for app.py

	Recieves sms message that was sent to twilo number and decides what action
	to perform. Then, this returns a reply that will be sent via sms.

	Args:
		sms: string that contains the message sent to the twilio number

	Returns:
		reply: string that contains the message to be sent as a reply to the
			app user as

	'''

	# print the incoming message to the server terminal
	print sms

	# do generic parsing
	sms = sms.rstrip()

	# if incoming message is the initializing message "START"
	if sms == 'START':
		reply = 'Thanks for playing Jeopardy! Text a number 0-29 to recieve a new question. Text "A" to get the answer. Text "CLOSE" to end.'
	# if incoming message is the closing message "STOP"
	elif sms == 'CLOSE':
		reply = 'temp: other message received'
		myGame.setI(0)
	elif sms == 'A':
		reply = getAnswer(myGame)
	else:
		reply = getQuestion(int(sms), myGame)

	return reply

def getQuestion(i, myGame):
	myGame.setI(i)
	row = i / 6
	col = i % 6
	return myGame.getClues()[row][col]

def getAnswer(myGame):
	row = myGame.getI() / 6
	col = myGame.getI() % 6
	return myGame.getAnswers()[row][col]