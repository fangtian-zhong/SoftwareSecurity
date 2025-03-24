"""
This python file is used to get the base information of articles, such as url, author, abstract and so on.
I develop four functions:
1. get_information_of_article_acm(
        url,
        title,
        title_class,
        auther,
        auther_class,
        time,
        time_class,
        abstract,
        abstract_class,
        file
                               )
2. get_information_of_article_spring(
        url,
        title,
        title_class,
        auther,
        auther_class,
        time,
        time_class,
        abstract,
        abstract_class,
        file
                               )
3. single_page_ieee(headers, ieee_keyword, url, page)
4. get_information_of_article_ieee(keyword)
As mentioned in the names of these functions, the functionalities of them can easily guess.
"""
import requests
from bs4 import BeautifulSoup
import json
import time
import re
def get_information_of_article_acm(
        url,
        title,
        title_class,
        auther,
        auther_class,
        time,
        time_class,
        abstract,
        abstract_class,
        file
                               ):
    """
    it is used to get a dictionary containing {title,url,authors,abstract,citation,year} of an article,
    which is specified by the input 'url'
    :param auther: The article's auther.
    :param auther_class: Where to find the string 'auther'. It can be changed according to the actual condition.
    :param title: The article's title.
    :param title_class: Where to find the string 'title'. It can be changed according to the actual condition.
    :param time: The article's published year.
    :param time_class: Where to find the string 'time'. It can be changed according to the actual condition.
    :param abstract: The article's abstract.
    :param abstract_class: Where to find the string 'abstract'. It can be changed according to the actual condition.
    :param url: a link of the article.
    :param file: a txt that will store the url which failed to fetch
    :return: a dictionary.
    """
    response = requests.get(url)
    if response.status_code == 200:
        csv_data = {}
        soup = BeautifulSoup(response.content, 'html.parser')

        # filter the article that pagesize lower than 7
        pages_text = soup.find("span", class_="epub-section__pagerange")
        if pages_text != None:
            pages_numbers = re.findall(r'\d+', pages_text.get_text())
            if len(pages_numbers) == 1:
                return 1
            if int(pages_numbers[1]) - int(pages_numbers[0]) + 1 < 7:
                return 1

        # get the title
        find_title = soup.find_all(title, class_=title_class)

        if find_title != None:
            title_data = ""
            for data in find_title:
                title_data += data.get_text() + "\n"
            csv_data["title"] = title_data
        else:
            csv_data["title"] = "None"

        # get the url
        csv_data["url"] = url
        # get the authors
        author_name = ""
        find_author = soup.find_all(auther, class_=auther_class)
        for a in find_author:
            author_name += a.find().get_text() + ","
        csv_data["author"] = author_name
        # get the article publish time
        find_time = soup.find(time, class_=time_class)
        if find_time != None:
            csv_data["time"] = find_time.get_text()
        else:
            csv_data["time"] = "None"
        # get the abstract
        find_abstract = soup.find_all(abstract, class_=abstract_class)
        if find_abstract != None:
            text_data = ""
            for data in find_abstract:
                text_data += data.get_text() + "\n"
            csv_data["abstract"] = text_data
        else:
            csv_data["abstract"] = "None"
        print("success to get the csv data")
        return csv_data
    else:
        print("fail to fetch", url)
        file.write(url + '\n')
        return None



def get_information_of_article_spring(
        url,
        title,
        title_class,
        auther,
        auther_class,
        time,
        time_class,
        abstract,
        abstract_class,
        file
                               ):
    """
    it is used to get a dictionary containing {title,url,authors,abstract,citation,year} of an article,
    which is specified by the input 'url'
    :param auther: The article's auther.
    :param auther_class: Where to find the string 'auther'. It can be changed according to the actual condition.
    :param title: The article's title.
    :param title_class: Where to find the string 'title'. It can be changed according to the actual condition.
    :param time: The article's published year.
    :param time_class: Where to find the string 'time'. It can be changed according to the actual condition.
    :param abstract: The article's abstract.
    :param abstract_class: Where to find the string 'abstract'. It can be changed according to the actual condition.
    :param url: a link of the article.
    :param file: a txt that will store the url which failed to fetch
    :return: a dictionary.
    """
    response = requests.get(url)
    if response.status_code == 200:
        csv_data = {}
        soup = BeautifulSoup(response.content, 'html.parser')
        # get the title
        find_title = soup.find(title, class_ = title_class)

        if find_title != None:
            csv_data["title"] = find_title.get_text()
        else:
            csv_data["title"] = "None"

        # get the url
        csv_data["url"] = url
        # get the authors
        author_name = ""
        find_author = soup.find_all(auther, class_=auther_class)
        for a in find_author:
            author_name += a.find().get_text() + ","
        csv_data["author"] = author_name
        # get the article publish time
        find_time = soup.find(time, class_=time_class)
        if find_time != None:
            csv_data["time"] = find_time.get_text()
        else:
            csv_data["time"] = "None"
        # get the abstract
        find_abstract = soup.find(abstract, class_=abstract_class)
        if find_abstract != None:
            csv_data["abstract"] = find_abstract.get_text()
        else:
            csv_data["abstract"] = "None"
        print("success to get the csv data")
        return csv_data
    else:
        print("fail to fetch", url)
        file.write(url + '\n')
        return None

def single_page_ieee(headers, ieee_keyword, url, page):
    """
    The function is used to get information of each single searched web page.
    a dictionary will be returned,
    and then this dictionary will be passed to function 'get_information_of_article_ieee' as parameter.
    :param headers: a dictionary that contains information of post header.
    :param ieee_keyword: used to search.
    :param url: url of the search page.
    :param page: page number.
    :return: a dictionary.
    """
    data = {
    "search": None,
    "doiSearch": None,
    "acronymSearch": None,
    "authorSearch": None,
    "authorAffiliationSearch": None,
    "advancedSearch": ieee_keyword,
    "publicationSearch": None,
    "beginPubDate": 2000,
    "endPubDate": 2025,
    "accessType": "all",
    "searchInner": [],
    "resultLimit": 10,
    "currentPage": str(page),
    "authors": [],
    "authorsAffiliation": [],
    "publications": [],
    "contentTypes": [],
    "sortBy": "rel",
    "includePreprints": True
}

    res = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
    time.sleep(2)
    dic_obj = res.json()
    return dic_obj


def get_information_of_article_ieee(keyword):
    """
    :param keyword: search keyword. It can be changed whatever you want.
    :return: Notice!! The return value is a list of dictionary
    """
    # pay attention to the 'Cookie' it must be changed to your 'Cookie'. It is flexible.
    headers = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '556',
        'Content-Type': 'application/json',
        'Cookie': 'acl-poly=s%3AnjVouF3Xi6xJUtBolbIXCUO4zKbBh704.FkjfreH75OjqPbIeJrVjL7fi96StwwrnVrC1z2tcbUo; feathr_session_id=65f8dbe63a8b66efe9fa2afd; _ce.s=v~cae442d99006c2a174a16a3d4032d655c88d3129~lcw~1710808116396~lva~1710808116396~vpv~0~lcw~1710808116400; __gads=ID=2bf9c0d9066295a1:T=1710808037:RT=1710813744:S=ALNI_MZqYDqnCfem8YNlslCeDCKsyZ8b6Q; __gpi=UID=00000d446bee124a:T=1710808037:RT=1710813744:S=ALNI_MZSbL1_xhU8ATshJk2-5ECmxvNWRQ; __eoi=ID=a79601fa360939a9:T=1710808037:RT=1710813744:S=AA-AfjZM76Ddpoby8glmaub0Hjxv',
        'Referer': 'https://wwwhtbprolcomputerhtbprolorg-s.evpn.library.nenu.edu.cn/csdl/search/default?queryState=',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
    }
    # the search page
    url = 'https://wwwhtbprolcomputerhtbprolorg-s.evpn.library.nenu.edu.cn/csdl/search/api/v1/search'
    # get the first page.
    single_page = single_page_ieee(headers, keyword, url, 1)
    # get the number of articles we searched.
    total_records = int(single_page["numHits"])
    # get the number of pages that we will need to travel.
    total_pages = int(total_records/single_page["resultLimit"])
    if total_records % single_page["resultLimit"] != 0:
        total_pages += 1
    print('The number of articles is', str(total_records))
    dic_list = []
    # fields = ["title", "url", "author", "time", "abstract"]
    # search each page and get the information of each article.
    for i in range(1, total_pages + 1):
        single_page = single_page_ieee(headers, keyword, url, i)
        # travel this page's article.
        for article in single_page["results"]:
            # article['doi'] stores serial number of a article.
            if article['doi'] != None:
                if 'pages' in article:
                    page_range = article['pages']
                    num_list = re.findall(r'\d+', page_range)
                    if len(num_list) == 1: # means the size of this article is just one.
                        print("the size of this article is not satisfied!url:",'https://wwwhtbprolcomputerhtbprolorg-s.evpn.library.nenu.edu.cn/csdl/' + article['doi'])
                    else:
                        if int(num_list[1]) - int(num_list[0]) + 1 >= 7:
                            # get the satisfied articles store them as a dictionary.
                            article_dic = {'title': article['title'],
                           'url': 'https://wwwhtbprolcomputerhtbprolorg-s.evpn.library.nenu.edu.cn/csdl/' + article['doi'],
                           'author': 'do not need!', 'time': article['pubYear'],
                           'abstract': article['abstract']}
                            dic_list.append(article_dic)
                        else:
                            print("the size of this article is not satisfied!url:",
                                  'https://wwwhtbprolcomputerhtbprolorg-s.evpn.library.nenu.edu.cn/csdl/' + article[
                                      'doi'])

            else:
                print(article['title'], "The doi is None!")

    return dic_list
