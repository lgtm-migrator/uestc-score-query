# -*- coding: utf-8 -*-
import requests
from pprint import pprint as pr
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

ALL_GRADES_URL = "http://eams.uestc.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"

AUTH_SERVER_URL = "https://idas.uestc.edu.cn/authserver/login"

AUTH_SERVER_INDEX = "https://idas.uestc.edu.cn/authserver/index.do"


def parse_all_grades_page(page: str):
    soup = BeautifulSoup(page, "lxml")
    grades_list = soup.select('.grid > table > tbody > tr')
    heads = list(map(lambda td: td.text.strip(), soup.select(
        '.grid > table > thead > tr > th')))
    table = []
    for grade in grades_list:
        line = {}
        tds = grade.find_all('td')
        for i in range(0, len(tds)):
            line[heads[i]] = tds[i].text.strip()
        table.append(line)
    return table


def get_authorized_session(username, password):
    session = requests.session()
    r = session.get(ALL_GRADES_URL)
    d = pq(r.text)
    # 从网页中获取动态生成的字段
    lt = d('#casLoginForm > input[type="hidden"]:nth-child(5)').attr.value
    execution = d(
        '#casLoginForm > input[type="hidden"]:nth-child(7)').attr.value
    data = {
        "username": username,
        "password": password,
        "lt": lt,
        "execution": execution,
        "rmShown": 1,
        "dllt": "userNamePasswordLogin",
        "_eventId": "submit"
    }
    # login
    session.post(AUTH_SERVER_URL, data=data)
    return session


def get_authorized_session_cookie(username, password):
    session = get_authorized_session(username, password)
    return session.cookies


def query(username, password):
    session = get_authorized_session(username, password)
    page = session.get(ALL_GRADES_URL).text
    return parse_all_grades_page(page)
