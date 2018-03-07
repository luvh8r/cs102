import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import time


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    all_tr = parser.table.findAll('table')[1].findAll('tr')[:90]
    all_list = [[all_tr[i], all_tr[i + 1]] for i in range(90) if i % 3 == 0]

    for string in all_list:
        first_string = string[0].findAll('td')[2]
        second_string = string[1].findAll('td')[1]

        commentsline = second_string.findAll('a')[-1].text
        if commentsline == 'discuss':
            comments = 0
        else:
            comments = int(commentsline[0])

        points = int(second_string.span.text[0])

        link = str(first_string.a)[27:]
        cuted = link.find('"')
        href = link[:cuted]
        if 'http' not in href:
            link = 'https://news.ycombinator.com/' + href
        else:
            link = href

        news_dict = {'author': second_string.a.text,
                     'comments': comments,
                     'points': points,
                     'title': str(first_string.a.text),
                     'url': link
                     }

        news_list.append(news_dict)

    return news_list

def extract_next_page(parser):
    """ Extract next page URL """
    news_table = parser.table.findAll('table')[1]
    final_row = news_table.findAll('tr')[91]
    link = str(final_row.findAll('td')[1].a)
    url_start = link.find('newest')
    url_end = link.find('" rel=')
    next_page_code = link[url_start:url_end]
    return next_page_code

def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        time.sleep(2)
        n_pages -= 1
    return news