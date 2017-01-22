import uestc_query,os;

def test_uestc_score_query():
  username = os.getenv("TUSERNAME");
  password = os.getenv("TPASSWORD");
  res = uestc_query.query(username,password);
  assert res != None
  assert len(res) > 0