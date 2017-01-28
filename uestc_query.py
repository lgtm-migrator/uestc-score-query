# -*- coding: utf-8 -*-
import requests
from pprint import pprint as pr
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup


class Session(object):

    def __init__(self):
        self.conn = requests.session()

    def login(self, username, password):
        session = self.conn
        r = session.get(
            "https://idas.uestc.edu.cn/authserver/login")
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
        r = session.post(
            "https://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal", data=data)
        return self.is_login()

    def is_login(self, username: str=None):
        r = self.conn.get("https://idas.uestc.edu.cn/authserver/index.do")
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            login_id = soup.select(
                "#auth_siderbar > div.auth_username > span > span")[0].text.strip()
            if username != None and username == login_id:
                return True
            elif login_id:
                return True
        except Exception as err:
            raise err
            return False

def query(username, password):
    session = requests.session()
    r = session.get(
        "http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F")
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
    r = session.post(
        "http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal", data=data)
    r = session.get(
        "http://eams.uestc.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR")
    table = []
    d = pq(r.text)
    h = d(".gridtable:last thead tr th")
    c = d(".gridtable:last tbody tr")

    for tr in c:
        line = {}
        for td, i in zip(tr.getchildren(), h):
            line[i.text] = td.text and td.text.strip()
        table.append(line)
    return table
