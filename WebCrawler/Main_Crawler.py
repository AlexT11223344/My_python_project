'''
    Request: From the search page to find all subpage URL
'''
import fake_useragent
import requests
import re
import csv
from fake_useragent import UserAgent
import time
from lxml import etree
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class MainCrawler:
    def __init__(self, SleepTime=time.sleep(2), NullValue='#Null'):
        self.time_sleep = SleepTime
        self.null_value = NullValue
        self.user_agent = UserAgent()
        self.main_address = 'archive.org'

    def get_source(self, URL):
        self.url = URL
        self.user_agent_random = self.user_agent.random
        self.request_headers = {
            "user-agent": self.user_agent_random
        }
        _session = requests.Session()
        _retry = Retry(connect=5, backoff_factor=0.5)
        _adapter = HTTPAdapter(max_retries=_retry)
        _session.mount('http://', _adapter)
        _session.mount('https://', _adapter)

        _url_resp = _session.get(self.url, headers=self.request_headers)
        _url_resp.encoding = 'utf-8'
        return _url_resp

    def get_info_re(self, Main_Page, Regular_Expression):
        # Format: Regular_Expression = r'<a href="(?P<author_url>.*?)">.*?>'
        self.re = Regular_Expression
        _result = self.re.findall(Main_Page)
        return _result

    def get_info_xpath(self, Main_Page, Xpath_route):
        self.xpath_MainPage = etree.HTML(Main_Page, etree.HTMLParser())
        _result = self.xpath_MainPage.xpath(Xpath_route)
        return _result

    # def get_title_xpath(self, Main_Page, Xpath_route):
    #     self.xpath_MainPage = etree.HTML(Main_Page, etree.HTMLParser())
    #     _subpage_title = self.xpath_MainPage.xpath(Xpath_route)
    #     return _subpage_title

    def url_transform(self, main_address, list_url):
        for i in range(0, len(list_url)):
            list_url[i] = main_address + list_url[i]
        return list_url


url_1 = "https://apps.lib.ua.edu/blogs/this-goodly-land/author-list/"
crawler = MainCrawler()

'''<---------------- 写入csv文件 ---------------->'''
f = open("MainPage_info.csv", mode="w", encoding='utf-8-sig', newline='')
csv_writer = csv.writer(f)
# csv_writer.writerow(['Subpage_title', 'title_URL'])
csv_writer.writerow(['Title_URL'])

for page_num in range(1, 26):
    url = "https://archive.org/search.php?query=George+Eliot&and%5B%5D=creator%3A%22george+eliot%22&and%5B%5D=creator%3A%22eliot%2C+george%2C+1819-1880%22&and%5B%5D=creator%3A%22eliot%2C+george%2C+1819-1880.%22&pa ge=" + f"{page_num}"
    resp = crawler.get_source(url)

    # 获取div[class = 'C234'] 下的文件， 获取链接和标题
    xpath_title = '//div[@class = "C234"]/div/a/@title'
    time.sleep(1)
    xpath_url = '//div[@class = "C234"]/div/a/@href'
    time.sleep(1)

    # 相对路径,列表形式存储
    subpage_url = crawler.get_info_xpath(resp.text, xpath_url)
    # 绝对路径,列表形式存储
    subpage_url_abs = crawler.url_transform(crawler.main_address, subpage_url)
    # 标题,列表形式存储
    subpage_title = crawler.get_info_xpath(resp.text, xpath_title)
    time.sleep(1)

    # print(len(subpage_url_abs))
    # print(len(subpage_title))
    print(subpage_url_abs)
    print(subpage_title)
    for i in range(len(subpage_url_abs)):
        csv_writer.writerow([subpage_url_abs[i]])
f.close()
print('Finish')

