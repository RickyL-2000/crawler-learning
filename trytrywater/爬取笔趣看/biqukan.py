# %%

"""
这个算法貌似有问题...爬出来是一个乱码，作为小白我暂时无可奈何
"""

# from bs4 import BeautifulSoup
# import requests
#
# if __name__ == "__main__":
#     url = "https://www.biqukan.com/1_1094/5403177.html"
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#     req = requests.get(url, headers=headers)
#     html = req.text
#     bf = BeautifulSoup(html, 'html.parser')
#     texts = bf.find_all('div', class_="showtxt")
#     print(texts[0].text.replace('\xa0'*8, '\n\n'))

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    texts = bf.find_all('div', id='content', class_='showtxt')
    print(texts[0].get_text())
