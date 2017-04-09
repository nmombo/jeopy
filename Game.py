from lxml import html
import requests
import re

class Game:

	def __init__(self, gameid='5566'):
		self.gameid = gameid
		self.game_url = 'http://www.j-archive.com/showgame.php?game_id=' + self.gameid
		self.page = requests.get(self.game_url)
		# Generate the html page tree
		self.tree = html.fromstring(self.page.content)
		self.setCategories()
		self.setClues()
		self.setAnswers()

	def setCategories(self):
		path = '//*[@class="category_name"]/text()'
		self.categories = self.tree.xpath(path)[0:6]

	def getCategories(self):
		return self.categories

	def setClues(self):
		self.clues = []
		for category in range(0,6):
			rows = []
			for row in range(0,5):
				# Clues
				path = '//*[@id="clue_J_' + str(category+1) + '_' + str(row+1) + '"]/text()'
				if self.tree.xpath(path):
					rows.append(self.tree.xpath(path)[0])
				else:
					rows.append('')
			self.clues.append(rows)

	def getClues(self):
		return self.clues

	def setAnswers(self):
		self.answers = []
		for category in range(0,6):
			rows = []
			for row in range(0,5):
				# Answers
				path = '//div[@onclick="togglestick(\'clue_J_'+ str(category+1) + '_' + str(row+1) + '_stuck\')"]/@onmouseover'
				if self.tree.xpath(path):
					toggle_js = self.tree.xpath(path)[0]
					answer = re.findall(r'correct_response">(.*)</em>', str(toggle_js))
					rows.append(answer[0]) if answer else rows_ans.append('')
				else:
					rows.append('')
			self.answers.append(rows)

	def getAnswers(self):
		return self.answers

	def setI(self, i):
		self.i = i

	def getI(self):
		return self.i