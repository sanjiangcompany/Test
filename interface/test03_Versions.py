import unittest
import requests
class VersionCase(unittest.TestCase):
    ''' 获取机器人版本信息 '''
    def setUp(self):
        self.base_url = "http://localhost:6001/api/Robot/packageVersions"
    def tearDown(self):
        print(self.result)

    def test01_GetPackagesTest(self):
        """校验返回数据信息"""
        payload = {'PackageId': 'bianliang', 'PageIndex': 1, 'PageSize': 10}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['message'], None)

    def test02_GetPackagesTest(self):
        """校验验证码"""
        payload = {'PackageId': 'bianliang', 'PageIndex': 1, 'PageSize': 10}
        r = requests.get(self.base_url, params=payload)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)

if __name__ == '__main__':
    unittest.main()






