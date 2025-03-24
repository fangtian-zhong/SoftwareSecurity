import articleInfo as artInfo
import dealfile
import requests
from bs4 import BeautifulSoup
import csv
import get_pages
import re
def search_acm(title, keyword, store_path):
    '''
    get information of the target article, and store them into a csv file.
    :param title: the keyword of a title.
    :param keyword: the keyword of abstract.
    :param store_path: where to store
    :return: None
    '''
    href_list = []
    base_url = "https://dl.acm.org/action/doSearch"
    params = {
        "fillQuickSearch": "false",
        "target": "advanced",
        "title": title,
        "Abstract": keyword,
        "AfterYear": "2004",
        "BeforeYear": "2024",
        "ContentItemType": "research-article",
        "pageSize": "20",
        "startPage": "0"

    }
    # get the response.
    response = requests.get(base_url, params=params)
    articles_cnt = 0
    per_page = 0
    # get the total number of articles and web pages.
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles_cnt = int(soup.find("span", class_="hitsLength").get_text().replace(",", ""))
        per_page = int(soup.find("a", class_="js--selected").text)
    else:
        print("Failed to fetch ACM search results")
    pages = articles_cnt/per_page
    if articles_cnt % per_page != 0:
        pages += 1
    print("articles in total:", articles_cnt)
    print("pages in total:", pages)

    # travel every page, and get all articles on each page.
    page_number = 0
    cnt = 0
    while pages >= page_number:
        params["startPage"] = page_number.__str__()
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            # parse the response.content for as a html.
            soup = BeautifulSoup(response.content, 'html.parser')
            # get url of all the articles.
            for link in soup.find_all("span", class_="hlFld-Title"):
                # get the link.
                href_a = link.find("a")
                href = href_a.get('href')
                if href:
                    # store the url into a list
                    href_list.append("https://dl.acm.org" + href)
                    print("number:%d" % cnt, "https://dl.acm.org" + href)
                    cnt += 1
                else:
                    print("href number:%d", cnt, "is null")
                    cnt += 1
        else:
            print("fail to fetch the url:%s at page", base_url, page_number)
            exit(1)
        page_number += 1

    fields = ["title", "url", "author", "time", "abstract"]
    filename = store_path + "article" + ".csv"
    # open the csv file.
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(fields)
    index = 1
    # travel the href_list and store the information of each article into the csv file.
    for href in href_list:
        text = artInfo.get_information_of_article_acm(href, None, "citation__title", None, "loa__author-name", None,
                                                  "CitationCoverData", None, "abstractSection abstractInFull")
        if text != None:
            dealfile.save_data_tocsv(text, filename, fields)
            print("article download %d" % index)
            index = index + 1

    print("ACM search results for keyword:", keyword)

def convert_acm_txt_to_csv(path_to_txt, store_path, from_, list_size):
    """
    It can be deprecated! I accidentally store the article url into txt,
    so I develop this for restore them into a csv file.
    :param path_to_txt:
    :param store_path:
    :param from_:
    :param list_size:
    :return:
    """
    href_list = dealfile.getinfo_txt(path_to_txt)

    fields = ["title", "url", "author", "time", "abstract"]
    filename = store_path + "article" + ".csv"
    if from_ == 0:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(fields)
    index = from_
    while index < list_size:
        text = artInfo.get_information_of_article_acm(href_list[index], None, "citation__title", None, "loa__author-name", None,
                                                      "CitationCoverData", None, "abstractSection abstractInFull")
        if text != None and text != 1:
            dealfile.save_data_tocsv(text, filename, fields)
            print("article download %d" % index)
        if text == None:
            print("fail to fetch at index:", index)
            return index
        if text == 1:
            print("the size of article is not satisfied at index:", index)
        index = index + 1

def search_springer(keyword, store_path, file):
    '''
    save the information of each article searched from Springer into a csv file.
    :param keyword: keyword.
    :param store_path: the path where to store.
    :param file: where to store the url which fail to fetch
    :return:
    '''
    base_url = "https://link.springer.com/search"
    href_list = []
    # the 'dataFrom' ,'dataTo' and 'keyword' can be changed to what you want.
    params = {
        "new-search": "true",
        "query": keyword,
        "content-type": "article",
        "dataFrom": 2004,
        "dataTo": 2024,
        "sortBy": "relevance",
        "date": "custom",
        "page": "1"
    }
    headers = {
        "Service-Worker-Allowed": "true"
    }
    # the parameter 'name' and 'class_' need to change by manually debugging the web (F12)
    # get the number of the pages.
    pages_cnt = get_pages.pages_cnt(base_url, keyword, params, headers, "li", "eds-c-pagination__item")
    # travel each page to get each articles' link
    page = 1
    while page <= pages_cnt:
        params["page"] = page.__str__()
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith("/article/"):
                    href_list.append("https://link.springer.com" + href)
        page += 1

    # the fields is a list of keys of the dictionary.
    fields = ["title", "url", "author", "time", "abstract"]
    filename = store_path + "springerarticle" + ".csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(fields)

    # travel the href_list, each href is a url of article.
    index = 1
    print(len(href_list))
    for href in href_list:
        response = requests.get(href)
        if response.status_code == 200:
            text = artInfo.get_information_of_article_spring(
                href,
                title="h1",
                title_class="c-article-title",
                time="time",
                time_class=None,
                auther="li",
                auther_class="c-article-author-list__item",
                abstract="div",
                abstract_class="c-article-section__content"
            )
            if text != None:
                dealfile.save_data_tocsv(text, filename, fields)
                print("article download %d" % index)
                index = index + 1
        else:
            print("failed to fetch :", href)
            file.write(href + '\n')

def search_ieee(keyword, store_path):
    """
    used to search articles from ieee, and store some information of them into a csv.
    :param keyword: keyword. You can change to whatever you want.
    :param store_path: where to store.
    :return: None
    """
    fields = ["title", "url", "author", "time", "abstract"]
    filename = store_path + "articleieee" + ".csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(fields)
    dic_list = artInfo.get_information_of_article_ieee(keyword)
    print("articles in total:", len(dic_list))
    index = 1
    for article in dic_list:
        if article['url'] != None:
            dealfile.save_data_tocsv(article, filename, fields)
            print("article download %d" % index)
            index = index + 1

def get_springer_pdf_url(article_url, file):
    """
    get the pdf url of the target article from Springer.
    :param article_url: the article need to be downloaded.
    :param file: where to store the article's url which failed to fetch, or I don't have access to download.
    :return: pdf url if find, None if not.
    """
    response = requests.get(article_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # find where stores the pdf url
        get_mod = soup.find("div", class_="c-pdf-download u-clear-both u-mb-16")
        if get_mod == None: # don't have access to pdf download
            print("url：%s can not download!" % article_url)
            file.write("noaccess: " +  article_url + '\n')
            return None
        pdf_url = "https://link.springer.com/" + get_mod.find('a').get('href')
        if get_mod.find('a').get('href') != None:
            return pdf_url
        else: # can not get the pdf download url
            print("the article doesn't have pdf url, article url:", article_url)
            file.write("nopdfurl: " + article_url + '\n')
            return None

    else: # fail to fetch article's url
        print("fail to fetch:", article_url)
        file.write("failfetch: " + article_url + '\n')
        return None

def get_acm_pdf_url(article_url, file):
    """
    get the pdf url of target article for downloading.
    :param article_url: url of target article.
    :param file: where to store the pdf_url that can not to be downloaded.
    :return: None if can not be downloaded, pdf_url if can download.
    """
    response = requests.get(article_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # get the pdf download url.
        get_link = soup.find("li", class_="pdf-file")
        if get_link == None: # don't have access to this article
            pdf_url = "https://dl.acm.org/doi/pdf/" + article_url.split("/")[4] + '/' + article_url.split("/")[5]
            # store it as pdf url into a file '.txt' or '.csv'
            file.write(pdf_url + "\n")
            return None
        else:# the pdf can be downloaded.
            pdf_url = "https://dl.acm.org" +  get_link.find("a").get("href")
            return pdf_url
    else:
        print("article url can not request!", article_url)
        pdf_url = "https://dl.acm.org/doi/pdf/" + article_url.split("/")[4] + '/' + article_url.split("/")[5]
        # store it as pdf url into a file '.txt' or '.csv'
        file.write(pdf_url + "\n")
        return None

def download_pdf_acm(url_list, from_, store_to_path, file):
    """
    Download the articles.
    :param url_list: a list of the articles' url.
    :param from_: starting index in the list.
    :param store_to_path: where to store the pdf of articles.
    :return:
    """
    len_url_list = len(url_list)
    print("need to be download in total:", len_url_list)
    for i in range(from_, len_url_list):
        # get the url of a pdf
        pdf_url = get_acm_pdf_url(url_list[i], file)
        if pdf_url != None:
            dealfile.download_pdf(pdf_url, store_to_path, i+1, file)
        else:
            pdf_url = "https://dl.acm.org/doi/pdf/" + url_list[i].split("/")[5] + '/' + url_list[i].split("/")[6]
            print("number %d the article can not be downloaded!url:" % (i+1), pdf_url)


