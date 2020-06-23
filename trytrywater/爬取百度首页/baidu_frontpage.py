# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
# urlretrieve 用于下载图片
from urllib.request import urlretrieve

# %%
# 读取首页html
html = urlopen("http://www.baidu.com/")

html_text = bytes.decode(html.read())

print(html_text)

# %%
html = urlopen("http://www.baidu.com/")     # FIXME: 为什么这里要重新读取一遍？

obj = bf(html.read(), 'html.parser')

title = obj.head.title

print(title)

# %%
# 打印所有图片的信息

pic_info = obj.find_all('img')

for i in pic_info:
    print(i)

# %%
# 只提取logo图片的信息

logo_pic_info = obj.find_all('img', class_="index-logo-src") # FIXME: 如果是find()会如何？

logo_url = "https:" + logo_pic_info[0]['src']
# 打印链接
print(logo_url)

# %%
# 下载图片
urlretrieve(logo_url, 'logo.png')
