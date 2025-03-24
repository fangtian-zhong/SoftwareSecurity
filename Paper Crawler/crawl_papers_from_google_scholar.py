from re import search
from sqlite3.dbapi2 import paramstyle
from time import sleep

import requests
from bs4 import BeautifulSoup

import csv

def search_papers(base_url, keyword):
    href_list = []
    page_number = 0
    while page_number < 150:
        url = base_url + keyword + page_number.__str__()
        response = requests.get(url)
        if response.status_code != 200:
            print("Can't access the website, error code:", response.status_code)
            print(url)
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            found_list = soup.find_all("div", class_="gs_r gs_or gs_scl")

            for mem in found_list:
                pdf_link = mem.find("a").get("href")
                href_list.append(pdf_link)
            print("have obtained", href_list.__len__(), "papers")
        page_number += 1*10
    #print(href_list)
    return href_list

def store_links(store_path, url_list):
    fields = ["URL"]
    filename = store_path
    # open the csv file.
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            for url in url_list:
                writer.writerow([url])
    except Exception as e:
        print("Failed to open", store_path, "Error:", e)

# You can change the store path and keyword to what you want
store_path = "Javascript.csv"
google_scholar = "https://scholar.google.com/scholar?q=bug+detection,"
href_list = search_papers(google_scholar, "+Javascript&start=")
store_links(store_path, href_list)
