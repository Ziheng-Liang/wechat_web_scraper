### use selenium to simulate scrollDown event.
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("http://mp.weixin.qq.com/mp/homepage?__biz=MjM5MjAyOTEzMg==&hid=1&sn=5f0278051f4e3c1d2b774abfeff832f0")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

print browser.page_source.encode('utf-8')
post_elems = browser.find_elements_by_class_name("list-item")

for post in post_elems:
    print post.text























