# tutorial from http://docs.python-guide.org/en/latest/scenarios/scrape/

# lxml is an extensive library with a module for parsing XML and HTML documents
from lxml import html
# requests is a module for http requests (I think)
import requests

# use requests.get to retrieve the web page with our data
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# parse the page with the html module
tree = html.fromstring(page.content)
	# tree contains the whole html file in a nice structure. We use page.content
	# for tree instead of page.text becase html.fromstring expects bytes for
	# an input. In this example, we will go over the tree structure with XPath.
	# We can also use the chrome inspector to find the XPath of an element by
	# right clicking an element, selecting 'Inspect element', highlighting the
	# code, right clicking again, and selecting 'Copt XPath'.

# The data of the page is stored in two elements. One is a div with title
# 'buyer-name' and the other is a span with class 'item-price'. For example:
 	# <div title="buyer-name">Carson Busses</div>
	# <span class="item-price">$29.95</span>
# Knowing this, we can create the correct XPath query and use the lxml xpath
# function like this:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')
# To test this we can see the output
print 'Buyers: ', buyers
print 'Prices: ', prices

# Ideas for learning more:
	# modify script to iterate through the rest of the pages of the sample data
	# rewrite application to use threads for improved speed