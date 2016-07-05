### use selenium to simulate scrollDown event.
import time
import re
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


urls = ["http://mp.weixin.qq.com/mp/homepage?__biz=MjM5MjAyOTEzMg==&hid=1&sn=5f0278051f4e3c1d2b774abfeff832f0"]

browser = webdriver.Chrome()

browser.get("http://mp.weixin.qq.com/mp/homepage?__biz=MjM5MjAyOTEzMg==&hid=1&sn=5f0278051f4e3c1d2b774abfeff832f0")
time.sleep(1)

def scrollDownAndConcatStr(concatString):
	elem = browser.find_element_by_tag_name("body")

	no_of_pagedowns = 20

	while no_of_pagedowns:
	    elem.send_keys(Keys.PAGE_DOWN)
	    time.sleep(0.2)
	    no_of_pagedowns-=1

	concatString = concatString + browser.page_source.encode('utf-8') # indeed print out the page html code.
	return concatString

articleString = ""
tabs = []
tabs = browser.find_elements_by_class_name("item")
articleString = scrollDownAndConcatStr(articleString)

# since there are 6 element that contains item as their class, the first three are the banner, we only need the last three elements.
tabs[4].click() # will jump to the middle one.
articleString = scrollDownAndConcatStr(articleString)

tabs[5].click() # will jump to last panel.
articleString = scrollDownAndConcatStr(articleString)

print articleString

postArr = []
postArr = re.findall(r'href="(http:\/\/mp\..*?)"', articleString)
print 'Grabbing ' + str(len(postArr)) + 'urls from website...'

### Remove duplicates from python list.
postArr = list(set(postArr))
print postArr
print 'After duplicates removal, ' + str(len(postArr)) + 'urls remained...'

with open('ada.csv', 'w') as csvfile:
    fieldnames = ['id', 'url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(len(postArr)):
    	nosym_url = re.sub(r'&amp;', '&', postArr[i])
    	writer.writerow({'id': i, 'url': nosym_url})






















