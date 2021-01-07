import unittest
import requests
class PackageListCase(unittest.TestCase):
    ''' 获取机器人流程列表 '''
    def setUp(self):
        self.base_url = "http://localhost:6001/api/Robot/packages"
    def tearDown(self):
        print(self.result)
    def test01_GetPackagesTest(self):
        """校验返回数据信息"""
        payload = {'PageIndex': 0, 'PageSize': 10}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['message'], None)

    def test02_GetPackagesTest(self):
        """校验验证码"""
        payload = {'PageIndex': 0, 'PageSize': 10}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)


if __name__ == '__main__':
    unittest.main()

