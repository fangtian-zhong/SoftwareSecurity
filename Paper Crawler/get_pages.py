from bs4 import BeautifulSoup
import requests
import json
def pages_cnt(url, keyword, params, header, name, class_):
    """
    It is just used for deal with the ieee page,
    so I will not show its details.
    """
    response = requests.get(url, params=params, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        find_data_page = soup.find_all(name, class_=class_)
        if len(find_data_page) == 1:
            return 1
        else:
            return len(find_data_page) - 1
    else:
        print("failed to fetch the url", url)

def single_page(url, headers, keyword, page):
    """
    It is deprecated!
    """
    data = {
        "newsearch": 'true',
        "queryText": keyword,
        "pageNumber": str(page),
    }
    response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
    print(response)
    page_dic = response.json()
    return page_dic