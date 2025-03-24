import csv
import requests

def save_data_tocsv(data, filename, fields):
    """
    Used to store information of articles I searched into a csv file.
    :param data: a dictionary.
    :param filename: where the information to be stored
    :param fields: the key of the parameter 'data'.
    :return: None
    """
    try:
        with open(filename, mode='a', newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            value = []
            for field in fields:
                value.append(data.get(field))
            writer.writerow(value)
        print("data has been written in csv file:", filename)
    except:
        print("fail to store the article's information!")


def getinfo_txt(path_to_txt):
    '''
    It is used to convert the link in a txt file to a list.
    :param path_to_txt: path to a txt.
    :return: a list of links of articles.
    Pay attention !!! It need to be changed when used !!!!! I can not deal with all the string of links.
    '''
    link_list = []
    with open(path_to_txt, "r", encoding="utf-8") as file:
        for line in file:
            link_str = line.split(" ")[1].strip()
            second_slash_index = link_str.find("//", link_str.find("//") + 2)
            rel_link = link_str[:second_slash_index] + link_str[second_slash_index:].replace("//","/",1)
            link_list.append(rel_link)
    return link_list

def download_pdf(pdf_url, store_path, seq_num, file):
    """
    download the articles to target directory.
    :param pdf_url: url of an article pdf.
    :param store_path: where ever you want to store the articles.
    :param seq_num: how many articles have been downloaded.
    :param file: store the url of articles that fail to be downloaded
    :return: None
    """
    pdf = store_path + pdf_url.split("/")[5] + '_' + pdf_url.split("/")[6] + ".pdf"
    response = requests.get(pdf_url)
    if response.status_code == 200:
        with open(pdf, "wb") as f:
            f.write(response.content)
        print("pdf download number:", str(seq_num))
    else:
        print("number: %d fail to fetch url:" % seq_num, pdf_url)
        file.write(pdf_url + "\n")

def get_data_from_csv(path_to_csv, key):
    """
    get url from a csv file.
    :param path_to_csv: path.
    :param key: the key mapped to the url.
    :return: a list of url.
    """
    url_list = []
    try:
        with open(path_to_csv, "r", encoding="utf-8") as file:
            readline = csv.DictReader(file)

            for row in readline:
                url_list.append(row[key])
        return url_list
    except:
        print("failed to get url from csv")
        return None