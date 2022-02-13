from genericpath import exists
import os
import requests
from lxml import etree

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(CURRENT_DIR, "downloads")

def SaveLltReport(url, fname=None):
    res = requests.get(url)
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    if not fname:
        _, fname = os.path.split(url)
    fname = os.path.join(TARGET_DIR, fname)
    with open(fname, 'wb') as file:
        file.write(res.content)

def GetPage(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    html = res.text.encode("utf-8")
    obj = etree.HTML(html)
    return obj

def DownloadPage(url):
    obj = GetPage(url)
    llt_url = obj.xpath("//*[@id='s_top_wrap']/div")
    print(llt_url)
    SaveLltReport(url)
    return next_url


DownloadPage("https://www.baidu.com/")
