import csv
import os
import PyPDF2
import string
from pdfminer.high_level import extract_text
import shutil
import re
class Springer_filter:
    """
    In this class, I define some method to filter the articles searched from Springer.
    """

    def __init__(self, article_path, article_filter_to, csv_path, wrong_folder_name):
        self.article_path = article_path
        self.article_filter_to = article_filter_to
        self.csv_path = csv_path
        self.wrong_folder = wrong_folder_name
    def convert_name(self, url_key):
        '''
        If download the article in order and name them from 1 to n, such as 1.pdf ... n.pdf
        :param url_key: url key stored in csv file
        :return: None
        '''
        url_list = []
        try:
            file = open(self.csv_path, mode='r', encoding='utf-8')
            reader = csv.DictReader(file)
            for row in reader:
                if row[url_key] != None:
                    url_list.append(row[url_key])
                else:
                    print(f"Pay attention to you key:{url_key} to url!")
        except:
            print("can not open the csv file at path:", self.csv_path)

        url_number = len(url_list)
        pdf_number = 0
        for filename in os.listdir(self.article_path):
            if os.path.isfile(os.path.join(self.article_path,filename)):
                pdf_number += 1

        if url_number != pdf_number:
            print("You have not downloaded all the articles!")
        else:
            # travel the articles from article path and change its name
            for file_name in os.listdir(self.article_path):
                file_num = int(file_name.split('.')[0])
                new_file_name = url_list[file_num-1].split('/')[4] + '_' + url_list[file_num-1].split('/')[5] + '.' +file_name.split('.')[1]
                try:
                    os.rename(os.path.join(self.article_path, file_name), os.path.join(self.article_path, new_file_name))
                    print(f"successfully change filename from {file_name} to {new_file_name}")
                except:
                    print(f"failed to change article name:{file_name}")

    def delete_size_lower(self, filter_size):
        '''
        Please pay attention to my code, I don't know why it will throw the exception when open the pdf that number of
        pages lower than 7.
        :param filter_size:
        :return:
        '''
        for file_name in os.listdir(self.article_path):
            if file_name.endswith('pdf'):
                pdf_path = os.path.join(self.article_path, file_name)
                try:
                    pdf_reader = PyPDF2.PdfReader(pdf_path)
                    if len(pdf_reader.pages) < filter_size:
                        os.remove(pdf_path)
                        print(f"the file {pdf_path} has removed")
                except:
                    print(f"fail to open the file {pdf_path}")
            else:
                print(f"the file {os.path.join(self.article_path, file_name)} is not a pdf!")

    def get_title_and_abstract(self, article_name, just_title):
        # judge if the file is a pdf or not
        if not article_name.endswith('.pdf'):
            print(f"the file {os.path.join(self.article_path, article_name)} is not a pdf file")
            return None
            # get the path of pdf
        pdf_path = os.path.join(self.article_path, article_name)
        try:
            # create a object to read text data from pdf
            file = open(pdf_path, mode='rb')
            pdf_reader = PyPDF2.PdfReader(file)
            # get the number of pages of the pdf
            num_pages = len(pdf_reader.pages)
        except:
            print(f"can not parse the file {pdf_path}")
            file.close()
            return None
        title_abstract_text = ""
        if just_title == True:
            for i in range(num_pages):
                page_text = pdf_reader.pages[i].extract_text()
                try:
                    page_text = page_text.encode('utf-8').decode('utf-8')
                except UnicodeEncodeError as e:
                    page_text = page_text.encode('ascii', 'ignore').decode('ascii')
                    print(f"the encoding of the pdf{pdf_path} is unknown, remove it to \wrong_pdf folder!")
                    file.close()
                    return None
                # turn the text of page to lower case for comparison
                page_text = page_text.lower()
                # after I check some articles I find some ones' abstract is starting with the word 'abftmct'
                index = page_text.find('abstract')
                if index == -1:
                    index = page_text.find('abftmct')
                if index != -1:
                    title_abstract_text += page_text[0:index]
                    #  delete the punctuation
                    title_abstract_text = title_abstract_text.translate(str.maketrans(" ", " ", string.punctuation))
                    # replace '\n' to ' '
                    title_abstract_text = re.sub(r'\n', ' ', title_abstract_text)
                    file.close()
                    return title_abstract_text
                # travel to the last page, but still do not get the text of title
                if i == num_pages - 1:
                    print(f"fail to get the text of title file{pdf_path}, remove it to \wrong_pdf folder!")
                    file.close()
                    return None

        else:
            for i in range(num_pages):
                # turn the text to lower
                page_text = pdf_reader.pages[i].extract_text().lower()
                index = page_text.find('introduction')
                if index == -1:
                    index = page_text.find('1 ')
                if index == -1:
                    # if travel the last page and do not find the abstract.
                    if i == num_pages - 1:
                        print(f"failed to find the text of title and abstract! file:{pdf_path}")
                        file.close()
                        return None
                    title_abstract_text += page_text
                else:
                    # get the title and abstract(we don't need but have no influence on result)
                    title_abstract_text += page_text[0:index]
                    #  delete the punctuation
                    title_abstract_text = title_abstract_text.translate(str.maketrans(" ", " ", string.punctuation))
                    # replace '\n' to ' '
                    title_abstract_text = re.sub(r'\n', ' ', title_abstract_text)
                    # turn it lower case
                    title_abstract_text = title_abstract_text.lower()
                    file.close()
                    return title_abstract_text


    def filtering_abstractAndtitle(self, keywords, target_folder, just_title):
        for file_name in os.listdir(self.article_path):
            # travel the pdf in the article's directory
            title_abstract_text = self.get_title_and_abstract(file_name, just_title)
            if title_abstract_text == None:
                # the target pdf file has something wrong and then move it to /wrong_pdf folder
                print(f"failed to get the article{file_name}'s title and abstract")
                # create /wrong_pdf folder
                if not os.path.exists(self.article_filter_to + self.wrong_folder):
                    try:
                        os.makedirs(self.article_filter_to + self.wrong_folder)
                    except:
                        print(f"failed to create a folder {self.article_filter_to + self.wrong_folder}")
                # copy the pdf file to /wrong_folder folder
                shutil.copy(self.article_path + file_name, self.article_filter_to + self.wrong_folder)
                print(
                    f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + self.wrong_folder}")
                # remove the pdf file from previous folder
                os.remove(self.article_path + file_name)
                print(f"successfully remove {self.article_path + file_name}")
                continue

            for keyword in keywords:

                # find the keyword in title or abstract
                if title_abstract_text.find(keyword) != -1:

                    # if the folder not exit then create a new folder
                    if not os.path.exists(self.article_filter_to + target_folder):
                        try:
                            os.makedirs(self.article_filter_to + target_folder)
                        except:
                            print(f"failed to create a folder {self.article_filter_to + target_folder}")

                    # copy the filtered pdf to the target folder
                    try:
                        shutil.copy(self.article_path + file_name, self.article_filter_to + target_folder)
                        print(
                            f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                        # remove the pdf file from previous folder
                        os.remove(self.article_path + file_name)
                        print(f"successfully remove {self.article_path + file_name}")
                    except:
                        print(
                            f"failed to copy the file from {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                    break

class ieee_filter:
    def __init__(self, article_path, article_filter_to, csv_path, wrong_folder_name):
        self.article_path = article_path
        self.article_filter_to = article_filter_to
        self.csv_path = csv_path
        self.wrong_folder = wrong_folder_name
    def get_title_and_abstract(self, article_name, just_title):
        '''
        Note: if return None, then remove the file to a /wrong_pdf folder
        :param article_name:
        :param just_title:
        :return:
        '''
        if not article_name.endswith('.pdf'):
            print(f"The file {os.path.join(self.article_path, article_name)} is not a pdf file!")
            return None
        # get the path of pdf
        pdf_path = os.path.join(self.article_path, article_name)
        try:
            # create a object to read text data from pdf
            file = open(pdf_path, mode='rb')
            pdf_reader = PyPDF2.PdfReader(file)
            # get the number of pages of the pdf
            num_pages = len(pdf_reader.pages)
        except:
            print(f"can not parse the file {pdf_path}")
            file.close()
            return None
        title_abstract_text = ""
        if just_title == True:
            for i in range(num_pages):
                page_text = pdf_reader.pages[i].extract_text()
                try:
                    page_text = page_text.encode('utf-8').decode('utf-8')
                except UnicodeEncodeError as e:
                    page_text = page_text.encode('ascii', 'ignore').decode('ascii')
                    print("the encoding of the pdf is unknown, remove it to \wrong_pdf folder!")
                # turn the text of page to lower case for comparison
                page_text = page_text.lower()
                # after I check some articles I find some ones' abstract is starting with the word 'abftmct'
                index = page_text.find('abstract')
                if index == -1:
                    index = page_text.find('abftmct')
                if index != -1:
                    title_abstract_text += page_text[0:index]
                    #  delete the punctuation
                    title_abstract_text = title_abstract_text.translate(str.maketrans(" ", " ", string.punctuation))
                    # replace '\n' to ' '
                    title_abstract_text = re.sub(r'\n', ' ', title_abstract_text)
                    file.close()
                    return title_abstract_text
                if i == num_pages - 1:
                    print(f"fail to get the text of title file{pdf_path}, remove it to \wrong_pdf folder!")
                    file.close()
                    return None

        else:
            for i in range(num_pages):
                # turn the text to lower
                page_text = pdf_reader.pages[i].extract_text()
                index = page_text.find('I. ')
                if index == -1:
                    index = page_text.find('1. ')
                if index == -1:
                    # if travel the last page and do not find the abstract.
                    if i == num_pages - 1:
                        print(f"failed to find the text of title and abstract! file:{pdf_path}")
                        file.close()
                        return None
                    title_abstract_text += page_text
                else:
                    # get the title and abstract(we don't need but have no influence on result)
                    title_abstract_text += page_text[0:index]
                    #  delete the punctuation
                    title_abstract_text = title_abstract_text.translate(str.maketrans(" ", " ", string.punctuation))
                    # replace '\n' to ' '
                    title_abstract_text = re.sub(r'\n', ' ', title_abstract_text)
                    # turn it lower case
                    title_abstract_text = title_abstract_text.lower()
                    file.close()
                    return title_abstract_text

    def filtering_abstractAndtitle(self, keywords, target_folder, just_title):
        for file_name in os.listdir(self.article_path):
            # travel the pdf in the article's directory
            title_abstract_text = self.get_title_and_abstract(file_name, just_title)
            if title_abstract_text == None:
                # the target pdf file has something wrong and then move it to /wrong_pdf folder
                print(f"failed to get the article{file_name}'s title and abstract")
                # create /wrong_pdf folder
                if not os.path.exists(self.article_filter_to + self.wrong_folder):
                    try:
                        os.makedirs(self.article_filter_to + self.wrong_folder)
                    except:
                        print(f"failed to create a folder {self.article_filter_to + self.wrong_folder}")
                # copy the pdf file to /wrong_folder folder
                shutil.copy(self.article_path + file_name, self.article_filter_to + self.wrong_folder)
                print(
                    f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + self.wrong_folder}")
                # remove the pdf file from previous folder
                os.remove(self.article_path + file_name)
                print(f"successfully remove {self.article_path + file_name}")
                continue

            for keyword in keywords:

                # find the keyword in title or abstract
                if title_abstract_text.find(keyword) != -1:

                    # if the folder not exit then create a new folder
                    if not os.path.exists(self.article_filter_to + target_folder):
                        try:
                            os.makedirs(self.article_filter_to + target_folder)
                        except:
                            print(f"failed to create a folder {self.article_filter_to + target_folder}")

                    # copy the filtered pdf to the target folder
                    try:
                        shutil.copy(self.article_path + file_name, self.article_filter_to + target_folder)
                        print(
                            f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                        # remove the pdf file from previous folder
                        os.remove(self.article_path + file_name)
                        print(f"successfully remove {self.article_path + file_name}")
                    except:
                        print(
                            f"failed to copy the file from {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                    break
class acm_filter:
    def __init__(self, article_path, article_filter_to, csv_path, wrong_folder_name):
        self.article_path = article_path
        self.article_filter_to = article_filter_to
        self.csv_path = csv_path
        self.wrong_folder = wrong_folder_name

    def get_title_and_abstract(self, article_name, just_title):
        # judge if the file is a pdf or not
        if not article_name.endswith('.pdf'):
            print(f"the file {os.path.join(self.article_path, article_name)} is not a pdf file")
            return None
            # get the path of pdf
        pdf_path = os.path.join(self.article_path, article_name)
        try:
            # create a object to read text data from pdf
            file = open(pdf_path, mode='rb')
            pdf_reader = PyPDF2.PdfReader(file)
            # get the number of pages of the pdf
            num_pages = len(pdf_reader.pages)
        except:
            print(f"can not parse the file {pdf_path}")
            file.close()
            return None
        title_abstract_text = ""
        if just_title == True:
            if just_title == True:
                for i in range(num_pages):
                    page_text = pdf_reader.pages[i].extract_text()
                    try:
                        page_text = page_text.encode('utf-8').decode('utf-8')
                    except UnicodeEncodeError as e:
                        page_text = page_text.encode('ascii', 'ignore').decode('ascii')
                        print(f"the encoding of the pdf{pdf_path} is unknown, remove it to \wrong_pdf folder!")
                        file.close()
                        return None
                    # turn the text of page to lower case for comparison
                    page_text = page_text.lower()
                    # after I check some articles I find some ones' abstract is starting with the word 'abftmct'
                    index = page_text.find('abstract')
                    if index == -1:
                        index = page_text.find('abftmct')
                    if index != -1:
                        title_abstract_text += page_text[0:index]
                        #  delete the punctuation
                        title_abstract_text = title_abstract_text.translate(str.maketrans(" ", " ", string.punctuation))
                        # replace '\n' to ' '
                        title_abstract_text = re.sub(r'\n', ' ', title_abstract_text)
                        file.close()
                        return title_abstract_text
                    # travel to the last page, but still do not get the text of title
                    if i == num_pages - 1:
                        print(f"fail to get the text of title file{pdf_path}, remove it to \wrong_pdf folder!")
                        file.close()
                        return None

        else:
            for i in range(num_pages):
                # turn the text to lower
                page_text = pdf_reader.pages[i].extract_text()
                index = page_text.find('I ')
                if index == -1:
                    index = page_text.find('1 ')
                if index == -1:
                    # if travel the last page and do not find the abstract.
                    if i == num_pages - 1:
                        print(f"failed to find the text of title and abstract! file:{pdf_path}")
                        file.close()
                        return None
                    title_abstract_text += page_text
                else:
                    # get the title and abstract(we don't need but have no influence on result)
                    title_abstract_text += page_text[0:index]
                    #  delete the punctuation
                    title_abstract_text = title_abstract_text.translate(str.maketrans(" ", " ", string.punctuation))
                    # replace '\n' to ' '
                    title_abstract_text = re.sub(r'\n', ' ', title_abstract_text)
                    # turn it lower case
                    title_abstract_text = title_abstract_text.lower()
                    file.close()
                    return title_abstract_text

    def filtering_abstractAndtitle(self, keywords, target_folder, just_title):
        for file_name in os.listdir(self.article_path):
            # travel the pdf in the article's directory
            title_abstract_text = self.get_title_and_abstract(file_name, just_title)
            if title_abstract_text == None:
                # the target pdf file has something wrong and then move it to /wrong_pdf folder
                print(f"failed to get the article{file_name}'s title and abstract")
                # create /wrong_pdf folder
                if not os.path.exists(self.article_filter_to + self.wrong_folder):
                    try:
                        os.makedirs(self.article_filter_to + self.wrong_folder)
                    except:
                        print(f"failed to create a folder {self.article_filter_to + self.wrong_folder}")
                # copy the pdf file to /wrong_folder folder
                shutil.copy(self.article_path + file_name, self.article_filter_to + self.wrong_folder)
                print(
                    f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + self.wrong_folder}")
                # remove the pdf file from previous folder
                os.remove(self.article_path + file_name)
                print(f"successfully remove {self.article_path + file_name}")
                continue

            for keyword in keywords:

                # find the keyword in title or abstract
                if title_abstract_text.find(keyword) != -1:

                    # if the folder not exit then create a new folder
                    if not os.path.exists(self.article_filter_to + target_folder):
                        try:
                            os.makedirs(self.article_filter_to + target_folder)
                        except:
                            print(f"failed to create a folder {self.article_filter_to + target_folder}")

                    # copy the filtered pdf to the target folder
                    try:
                        shutil.copy(self.article_path + file_name, self.article_filter_to + target_folder)
                        print(
                            f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                        # remove the pdf file from previous folder
                        os.remove(self.article_path + file_name)
                        print(f"successfully remove {self.article_path + file_name}")
                    except:
                        print(
                            f"failed to copy the file from {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                    break

    def detect_double_col(self, pdf_path, limit_lines):
        try:
            file = open(pdf_path, 'rb')
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = pdf_reader.pages
        except:
            print(f"fail to parse the file {pdf_path}")
        else:
            for page_num in range(len(num_pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                lines = text.split('\n')
                num_lines = len(lines)
                if num_lines <= limit_lines:
                    # single column
                    return 0
                else:
                    return 1
    def filter_page_size(self, double_limit_size, limit_lines, d_folder_name, s_folder_name):
        for file_name in os.listdir(self.article_path):

            if not file_name.endswith('.pdf'):
                print(f"the file {os.path.join(self.article_path, file_name)} is not a pdf")
                continue

            pdf_path = os.path.join(self.article_path, file_name)
            is_double_column = self.detect_double_col(pdf_path, limit_lines)

            try:
                file = open(pdf_path, "rb")
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
            except:
                print(f"fail to parse {pdf_path}")
                continue
            print(f"------start to filter the article {pdf_path}------")
            if not os.path.exists(self.article_filter_to + d_folder_name):
                try:
                    os.makedirs(self.article_filter_to + d_folder_name)
                except:
                    print(f"fail to create the folder {self.article_filter_to + d_folder_name}")

            if not os.path.exists(self.article_filter_to + s_folder_name):
                try:
                    os.makedirs(self.article_filter_to + s_folder_name)
                except:
                    print(f"fail to create the folder {self.article_filter_to + s_folder_name}")

            if is_double_column == 1 and num_pages >= double_limit_size:
                try:
                    shutil.copy(self.article_path + file_name, self.article_filter_to + d_folder_name)
                    print(
                        f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + d_folder_name}")
                    # remove the pdf file from previous folder
                    # os.remove(self.article_path + file_name)
                    # print(f"successfully remove {self.article_path + file_name}")
                except:
                    print(
                        f"failed to copy the file from {self.article_path + file_name} to {self.article_filter_to + d_folder_name}")
            if is_double_column == 0 and num_pages >= 2 * double_limit_size:
                try:
                    shutil.copy(self.article_path + file_name, self.article_filter_to + s_folder_name)
                    print(
                        f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + s_folder_name}")
                    # remove the pdf file from previous folder
                    # os.remove(self.article_path + file_name)
                    # print(f"successfully remove {self.article_path + file_name}")
                except:
                    print(
                        f"failed to copy the file from {self.article_path + file_name} to {self.article_filter_to + s_folder_name}")

class deal_extract_text:
    def __init__(self, article_path, article_filter_to, wrong_folder_name):
        self.article_path = article_path
        self.article_filter_to = article_filter_to
        self.wrong_folder = wrong_folder_name

    def get_extract_text(self, article_name):
        pdf_path = os.path.join(self.article_path, article_name)
        try:
            # get the extract_text of the article
            text = extract_text(pdf_path)
        except:
            print(f"fail to get the text of the article {pdf_path}")
            return None
        else:
            #  delete the punctuation
            text = text.translate(str.maketrans(" ", " ", string.punctuation))
            # replace '\n' to ' '
            text = re.sub(r'\n', ' ', text)
            # turn it lower case
            text = text.lower()
            return text

    def filter_article(self, keywords, target_folder):
        for file_name in os.listdir(self.article_path):
            text = self.get_extract_text(file_name)
            print(f"------start to parse {os.path.join(self.article_path, file_name)}------")

            if text == None:
                try:
                    # create /wrong_pdf folder
                    if not os.path.exists(self.article_filter_to + self.wrong_folder):
                        try:
                            os.makedirs(self.article_filter_to + self.wrong_folder)
                        except:
                            print(f"failed to create a folder {self.article_filter_to + self.wrong_folder}")
                    # copy the wrong file to the wrong_folder
                    shutil.copy(self.article_path + file_name, self.article_filter_to + self.wrong_folder)
                    print(
                        f"successfully move the article {self.article_path + file_name} to {self.article_filter_to + self.wrong_folder}")
                    # remove the pdf file from previous folder
                    os.remove(self.article_path + file_name)
                    print(f"successfully remove {self.article_path + file_name}")
                except:
                    print(
                        f"fail to move the article {self.article_path + file_name} to {self.article_filter_to + self.wrong_folder}")
            else:
                for keyword in keywords:
                    if text.find(keyword) != -1:
                        if not os.path.exists(self.article_filter_to + target_folder):
                            try:
                                os.makedirs(self.article_filter_to + target_folder)
                            except:
                                print(f"fail to create the folder /{target_folder}, can't filter the file {self.article_path + file_name}")
                                break
                        # copy the filtered pdf to the target folder
                        try:
                            shutil.copy(self.article_path + file_name, self.article_filter_to + target_folder)
                            print(
                                f"successfully filter the article {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                            # remove the pdf file from previous folder
                            os.remove(self.article_path + file_name)
                            print(f"successfully remove {self.article_path + file_name}")
                        except:
                            print(
                                f"failed to copy the file from {self.article_path + file_name} to {self.article_filter_to + target_folder}")
                        break

