from bs4 import BeautifulSoup
import requests, os, itertools, re

print("Enter URL: ")
url = input()

def search_webpage(url, searched_word):
    # get request is made to the website
    html_text = requests.get(url).text
    # set the parser and the text to be parsed
    soup = BeautifulSoup(html_text, 'lxml')
    results = soup.body.find_all(string=re.compile(
        '.*{0}.*'.format(searched_word), re.IGNORECASE), recursive=True)
    return results

def get_sop():
    return search_webpage(url, "personal statement")

def get_fee():
    return search_webpage(url, "fee")

def get_letter():
    return search_webpage(url, "letter")

def get_toefl():
    return search_webpage(url, "TOEFL")

def get_gre():
    return search_webpage(url, "GRE")

def get_app_link():
    return search_webpage(url, "apply")

def get_deadline():
    return search_webpage(url, "deadline")

def get_faq():
    return search_webpage(url, "frequently")


# print(get_sop())
# print(get_fee())
# print(get_letter())
# print(get_toefl())
# print(get_gre())
# print(get_app_link())
# print(get_deadline())
# print(get_faq())