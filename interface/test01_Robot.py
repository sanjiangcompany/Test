import unittest
import requests
class GetNameCase(unittest.TestCase):
    ''' 获取机器人基础信息 '''
    def setUp(self):
        self.base_url = "http://localhost:6001/api/v2/robot"
    def tearDown(self):
        print(self.result)
    def test01_GetNameTest(self):
        """校验验证码"""
        r = requests.get(self.base_url)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)

    def test02_GetNameTest(self):
        """校验返回数据信息"""
        r = requests.get(self.base_url)
        self.result = r.json()
        self.assertEqual(self.result['message'], None)

if __name__ == '__main__':
    unittest.main()












