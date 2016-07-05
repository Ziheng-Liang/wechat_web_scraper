import urllib
from bs4 import BeautifulSoup
import re
import csv
from textblob.blob import TextBlob

### Return compressed nested texts from page.
def url2content(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	texts = soup.findAll(text=True)

	def visible(element):
	    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
	        return False
	    elif re.match('<!--.*-->', element.encode('utf-8')):
	        return False
	    return True

	visible_texts = filter(visible, texts)

	# print visible_texts

	def removeSpace(string):
		return string.replace("\n", "")

	# for visible_text in map(removeSpace, visible_texts):
		# print visible_text.encode('utf-8')
	
	### From manually experiments, I find that the [0] refers to an link script tag, [1] refers to article title. [8] refers to the date, and [9] refers to the author.
	for i in range(1, 10):
		print filter(bool, map(removeSpace, visible_texts))[i].encode('utf-8')

	combined_string = ''.join(map(removeSpace, visible_texts))

	# print combined_string # it looks good!
	return combined_string.encode('utf-8')


##  Connect with ada.csv to port from url to texts
with open('ada-content.csv', 'w') as target:
    fieldnames = ['id', 'content']
    writer = csv.DictWriter(target, fieldnames=fieldnames)
    writer.writeheader()

    with open('ada.csv') as source:
	    reader = csv.DictReader(source)
	    for row in reader:
		    writer.writerow({'id': row['id'], 'content': url2content(row['url'])})
		    print 'Processing NO.' + str(row['id'])


### Connect with ada-content.csv to translate content to english version.	
with open('ada-content-en.csv', 'w') as target:
    fieldnames = ['id', 'content']
    writer = csv.DictWriter(target, fieldnames=fieldnames)
    writer.writeheader()

    with open('ada-content.csv') as source:
	    reader = csv.DictReader(source.read().splitlines())
	    for row in reader:
	    	chinese_blob = TextBlob(row['content'].decode('utf-8'))
	    	en_content = chinese_blob.translate(from_lang="zh-CN", to='en')
	    	writer.writerow({'id': row['id'], 'content': en_content})
	    	print 'Processing NO. ' + str(row['id'])














