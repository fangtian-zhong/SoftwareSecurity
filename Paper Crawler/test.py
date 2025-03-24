# The python is just used to test my code.


import os
import re
import string
from pdfminer.high_level import extract_text
import PyPDF2
import  shutil
import requests
import  Filter
import bs4
acm_store_path = "D:\\gitspace\\mysurvey\\articles\\"
ieee_store_path = "D:\\gitspace\\mysurvey\\articles\\"
springer_store_path = "D:\\gitspace\\mysurvey\\articles\\"
springer_pdf_path = "D:\\gitspace\\mysurvey\\pdf\\springer\\"
ieee_pdf_path = 'D:\\gitspace\\mysurvey\\pdf\\Ieee\\'
acm_pdf_path = "D:\\gitspace\\mysurvey\\pdf\\acm\\"
keyword = "vulnerability,bug,machine learning"
pdf_double_col_path = "D:\\gitspace\mysurvey\\filterarticles\\source_code\\source_code_android\\10.1145_3395363.3397356.pdf"
pdf_single_col_path = "D:\\gitspace\mysurvey\\filterarticles\\source_code\\source_code_android\\10.1007_s10664-022-10119-4.pdf"
def detect_double_column(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = pdf_reader.pages
        for page_num in range(len(num_pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            lines = text.split('\n')
            left_aligned = 0
            right_aligned = 0
            for line in lines:
                if line.strip():
                    if line[0].isdigit():  # Assuming numbers indicate left alignment
                        left_aligned += 1
                    elif line[-1].isdigit():  # Assuming numbers indicate right alignment
                        right_aligned += 1
            if left_aligned > right_aligned:
                return 1
            elif right_aligned > left_aligned:
                return 0
            else:
                #print(f"Page {page_num + 1}: Uncertain Layout")
                return 2

def detect_double_col(pdf_path, limit_lines):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = pdf_reader.pages
        for page_num in range(len(num_pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            lines = text.split('\n')
            num_lines = len(lines)
            if num_lines <= limit_lines:
                print(f"num_lines: {num_lines}, single: {pdf_path}")
                # single column
                return num_lines
            else:
                print(f"num_lines: {num_lines}, double: {pdf_path}")
                return num_lines

# print(detect_double_col("D:\\gitspace\\mysurvey\\filterarticles\\source_code\\source_code_android\\3571848.pdf", 45))
# print(detect_double_col(pdf_double_col_path, 45))
number_list = []
for file in os.listdir("D:\\gitspace\\mysurvey\\filterarticles\\source_code\\source_code_win\\"):

    pdf_path = os.path.join("D:\\gitspace\\mysurvey\\filterarticles\\source_code\\source_code_win\\", file)
    number_list.append(detect_double_col(pdf_path, 48))

sort_list = sorted(number_list)
print(sort_list)