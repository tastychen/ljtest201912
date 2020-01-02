import unittest
import requests
from utils.tools import Db
from config import host,dbinfo

dbhost = dbinfo["host"]
user = dbinfo["user"]
password = dbinfo["password"]
dbname = dbinfo["dbname"]
db = Db(dbhost,user,password,dbname)


class TestInspirer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.requests = requests.Session()
        url = host + "/login"
        headers = {"Content-Type":"application/json"}
        data = {"username":"langjin","password":"lj123456"}
        res = cls.requests.post(url,headers=headers,json=data)
        cls.token = res.json()["data"]["token"]
    
    
    @classmethod
    def tearDownClass(cls):
        db.commit("delete from t_inspirer where uid = 251;")


    def test_01_inspirernew(self):
        """测试发表灵感接口"""
        url = host+"/inspirer/new"
        headers = {"Content-Type":"application/json"}
        headers.update(token=self.token)
        data = {"content":"测试自动化发表灵感"}
        res = self.requests.post(url,headers=headers,json=data)
        global iid
        iid = db.query("SELECT id from t_inspirer where uid = 251 ORDER BY createtime desc limit 1;")[0][0]
        self.assertEqual(200,res.json()["status"])

    def test_02_inspirerupdate(self):
        """测试修改灵感接口"""
        url = host+"/inspirer/update"
        headers = {"Content-Type":"application/json"}
        headers.update(token=self.token)
        data = {"content":"修改测试自动化发表灵感","iid":iid}
        res = self.requests.post(url,headers=headers,json=data)
        self.assertEqual(200,res.json()["status"])

    def test_03_inspirerdelete(self):
        """测试删除灵感接口"""
        url = host+"/inspirer/delete"
        headers = {"Content-Type":"application/json"}
        headers.update(token=self.token)
        data = {"iid":iid}
        res = self.requests.post(url,headers=headers,json=data)
        self.assertEqual(200,res.json()["status"])



