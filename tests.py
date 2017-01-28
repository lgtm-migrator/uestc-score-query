import uestc_query
import os

username = os.getenv("TUSERNAME")
password = os.getenv("TPASSWORD")

def test_uestc_score_query():
    res = uestc_query.query(username, password)
    assert res != None
    assert len(res) > 0


def test_uestc_score_login():
    s = uestc_query.Session()
    assert s.login(username, password) == True
