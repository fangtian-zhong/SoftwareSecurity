"""
Author: Zhuoyun Qian
Email: zhuoyunqian19@gmail.com
Version: 1.0
Situation:
1. Springer: download articles from Springer is easy, this project can do it successfully
2. IEEE: It has anti-crawler mechanism, the project can only get the target download url, cannot download automatically
3. Acm: It has 'IP block' mechanism! each IP can just download about 30 articles, and It is slower than doing it manually.


It is used to search articles from acm, ieee and springer libraries by keywords.
After getting the base information of each article such as url, abstract and so on, download them as pdf format.
The main.py is used for call other functions from other python file and download the target articles.

The keyword can be changed whatever you want. For example, bellow is my keywords for searching articles.
IEEE keywords:
ieee_keyword = []
ieee_keyword.append({
            "query": "vulnerability,bug",
            "junction": "and",
            "dimensions": "title"
        })
ieee_keyword.append({
            "query": "bug,vulnerability",
            "junction": "or",
            "dimensions": "pub_title"
        })
ieee_keyword.append({
            "query": "machine learning,vulnerability discovery,bug detection",
            "junction": "and",
            "dimensions": "abstract"
        })
ACM lib keywords:
    params = {
        "fillQuickSearch": "false",
        "target": "advanced",
        "title": title_keyword,
        "Abstract": abstact_keyword,
        "AfterYear": "2004",
        "BeforeYear": "2024",
        "ContentItemType": "research-article",
        "pageSize": "20",
        "startPage": "0"
    }
title_keyword = "vulnerability bug"
abstact_keyword = "vulnerability discovery,machine learning,bug detection"
Springer keywords:
keyword = 'vulnerability,bug,machine learning'

From these keywords and params, you can find that I search the articles published from 2004 to 2024,
and the number of their pages can't be lower than 7.

"""
import os
import Filter
import dealfile
acm_store_path = "path"
ieee_store_path = "path"
springer_store_path = "path"
springer_pdf_path = "path"
ieee_pdf_path = "path"
acm_pdf_path = "path"

# there you can write your code to download the article

# define the list of the keywords
keywords = ['keyword_1', 'keyword_2', 'keyword_3']

# then develop code for searching, filtering or categorizing papers.

if __name__ == '__main__':
    print("Write your code")