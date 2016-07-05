import urllib
from bs4 import BeautifulSoup
import re

html = urllib.urlopen('http://mp.weixin.qq.com/s?__biz=MjM5MjAyOTEzMg==&mid=2650157004&idx=1&sn=3a85bd6c678f00b2cdbe73b80e964d60&scene=19#wechat_redirect').read()
soup = BeautifulSoup(html, 'html.parser')
texts = soup.findAll(text=True)

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', element.encode('utf-8')):
        return False
    return True

visible_texts = filter(visible, texts)

# for visible_text in visible_texts:
# 	print visible_text.encode('utf-8')

def removeSpace(string):
	return string.replace("\n", "")

combined_string = ''.join(map(removeSpace, visible_texts))

print combined_string


















