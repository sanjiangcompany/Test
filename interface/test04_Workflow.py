import unittest
import requests
import json
class RunWorkCase(unittest.TestCase):
    ''' 机器人运行流程 '''
    def setUp(self):
        # apps走的是下面runWorkflow 运行流程，runProject这个apps这边不用
        self.base_url = "http://localhost:6001/api/Robot/runWorkflow"
    def tearDown(self):
        print(self.result)
    def test01_PostRunWork(self):
        """校验返回数据信息"""
        # '''方式一'''
        # headers = {"Content-Type": "application/json"}
        # payload = {"PackageId": "bianliang", "Version": "1.0.8", "UserName": "baiqingmei"}
        # r = requests.post(url=self.base_url, data=json.dumps(payload), headers=headers)
        json_data = {"PackageId": "bianliang", "Version": "1.0.0", "UserName": "baiqingmei"}
        r = requests.post(url=self.base_url,json=json_data)
        self.result = r.json()
        self.assertEqual(self.result['message'], None)

    def test02_PostRunWork(self):
        """校验验证码"""
        # '''方式一'''
        # headers = {"Content-Type": "application/json"}
        # payload = {"PackageId": "bianliang", "Version": "1.0.8", "UserName": "baiqingmei"}
        # r = requests.post(url=self.base_url, data=json.dumps(payload), headers=headers)
        json_data = {"PackageId": "bianliang", "Version": "1.0.0", "UserName": "baiqingmei"}
        r = requests.post(url=self.base_url,json=json_data)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)

    def test03_PostRunWork(self):
        """提交运行的流程ID为空"""
        json_data = {"PackageId": "", "Version": "1.0.0", "UserName": "baiqingmei"}
        r = requests.post(url=self.base_url,json=json_data)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 33101)

    def test04_PostRunWork(self):
        """提交运行的流程，未找到指定的流程包"""
        json_data = {"PackageId": "", "Version": "1.0.0", "UserName": "baiqingmei"}
        r = requests.post(url=self.base_url,json=json_data)
        self.result = r.json()
        self.assertEqual(self.result['message'], '未找到指定的流程包')

    def test05_PostRunWork(self):
        """提交运行的流程版本号为空"""
        json_data = {"PackageId": "bianliang", "Version": "", "UserName": "baiqingmei"}
        r = requests.post(url=self.base_url,json=json_data)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 33101)

    def test06_PostRunWork(self):
        """windows用户名称为空"""
        json_data = {"PackageId": "bianliang", "Version": "1.0.0", "UserName": ""}
        r = requests.post(url=self.base_url,json=json_data)
        self.result = r.json()
        self.assertEqual(self.result['errorCode'], 0)




if __name__ == '__main__':
    unittest.main()

