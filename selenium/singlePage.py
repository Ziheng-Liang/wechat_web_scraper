from lxml import html
import requests


page = requests.get('http://mp.weixin.qq.com/s?__biz=MjM5MjAyOTEzMg==&mid=2650157004&idx=1&sn=3a85bd6c678f00b2cdbe73b80e964d60&scene=19#wechat_redirect')
tree = html.fromstring(page.content)

print page.content