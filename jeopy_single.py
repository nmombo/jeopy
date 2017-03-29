# jeopy_single.py
# First attempt at scraping data from J! Archive. The plan is to scrape data
# for just a single file before attempting to present it in a meaningful way
# or iterating through multiple shows.

# Author: Noah Momblanco
#         http://github.com/nmombo/jeopy
# Date: 3/28/2017

from lxml import html
import requests

# Get the page with show #7490
game_url = 'http://www.j-archive.com/showgame.php?game_id=5566'
page = requests.get(game_url)
# Generate the html page tree
tree = html.fromstring(page.content)

# Parse round one categories from tree
path = '//*[@class="category_name"]/text()'
categories_rnd1 = tree.xpath(path)[0:6]

# Parse round one clues from tree
# ID's of clues go from "clue_J_1_1" to "clue_J_6_5"
clues = []
for category in range(0,6):
	rows = []
	for row in range(0,5):
		path = '//*[@id="clue_J_' + str(category+1) + '_' + str(row+1) + '"]/text()'
		if tree.xpath(path):
			rows.append(tree.xpath(path)[0])
		else:
			rows.append("")
	clues.append(rows)

# Parse answers from tree
path = '//*[@id="clue_J_2_1"]/em'
print tree.xpath(path)

# Test scraping
for category in range(0,6):
	print categories_rnd1[category]
	for row in range(0,5):
		print '    clue ' + str(row+1) + ': ' + str(clues[category][row])
