"""
Author: Zhuoyun Qian
Email: qianzhuoyun@nenu.edu.cn
Version: 1.0
Situation:
1. Springer: download articles from Springer is easy, this project can do it successfully
2. IEEE: It has anti-crawler machanism, the project can only get the target download url, cannot dowload automatically
3. Acm: It has 'IP block' machanism! each IP can just download about 30 articles, and It is slower than do it manually.
4. Sci-Hub: articles in this library can be downloaded for free, but this database incomplete.
What I am doing:
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
and the number of their pages can't lower than 7.

"""
import os
import Filter
import dealfile
acm_store_path = "D:\\gitspace\\mysurvey\\articles\\"
ieee_store_path = "D:\\gitspace\\mysurvey\\articles\\"
springer_store_path = "D:\\gitspace\\mysurvey\\articles\\"
springer_pdf_path = "D:\\gitspace\\mysurvey\\pdf\\springer\\"
ieee_pdf_path = 'D:\\gitspace\\mysurvey\\pdf\\Ieee\\'
acm_pdf_path = "D:\\gitspace\\mysurvey\\pdf\\acm\\"
keyword = "vulnerability,bug,machine learning"

# there you can write your code to download the article

keywords_IR = [' p code', 'assembly','microsoft intermediate language', 'msil', 'llvm', 'gimple', 'jimple', 'smali', ' spir-v', 'mlir' ]
keywords_IR_new = ['smali file', 'smali code', 'vliw architecture', 'intermediate representation', 'microsoft intermediate language']
keywords_bytecode = ['bytecode', 'byte code']
keywords_binary = ['binary']
keywords_network = ['network']
filtering = Filter.deal_extract_text(
                article_path="D:\\gitspace\mysurvey\\filterarticles\\source_code\\Others\\",
                article_filter_to="D:\\gitspace\mysurvey\\filterarticles\\source_code\\Others\\",
                wrong_folder_name="wrong_pdf"
)


filtering.filter_article(keywords_IR_new,'IR')