from lxml import html
import requests

page = requests.get('http://mp.weixin.qq.com/mp/homepage?__biz=MjM5MjAyOTEzMg==&hid=1&sn=5f0278051f4e3c1d2b774abfeff832f0')
tree = html.fromstring(page.content)
print page.content