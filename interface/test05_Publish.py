import unittest
import requests
import warnings
import time

class ProcessCase(unittest.TestCase):
    ''' 机器人发布流程 '''
    def setUp(self):
        self.base_url = "http://localhost:6001/api/Robot/packages/publish"
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        print(self.result)

    def test01_PostRobotPublish(self):
        """数据正确直接上传"""
        files = {'file': ('bianliang', open(r'D:\Robot\bianliang.dgs', 'rb'))}
        # Version的值这个是需要唯一的，并且只能是增加的，不能减少
        f = open('D:\Robot\shuzi.txt', 'r+')    # 一定要r+模式，不然后面truncate的时候会报错
        data = f.read()
        new_data = int(data) + 1

        # print(new_data)
        # print(f"type(new_data): {type(data)}")
        f.seek(0)  # 清除内容
        f.truncate()
        f.write(str(new_data))
        Cu_Version = "1.0.{}".format(new_data)
        f.close()

        body_data = {
            "Name": "bianliang",
            "PublishUser": "luzhaoshan",
            "Description": "机票应用",
            "Version": Cu_Version
        }

        re = requests.post(url=self.base_url, data=body_data, files=files)
        self.result = re.json()
        self.assertEqual(self.result['errorCode'], 0)

    def test02_PostRobotPublish(self):
        """校验返回数据信息"""
        files = {'file': ('bianliang', open(r'D:\Robot\bianliang.dgs', 'rb'))}
        # Version的值这个是需要唯一的，并且只能是增加的，不能减少
        f = open('D:\Robot\shuzi.txt', 'r+')    # 一定要r+模式，不然后面truncate的时候会报错
        data = f.read()
        new_data = int(data) + 1
        # print(new_data)
        # print(f"type(new_data): {type(data)}")
        f.seek(0)  # 清除内容
        f.truncate()
        f.write(str(new_data))
        Cu_Version = "1.0.{}".format(new_data)
        f.close()

        body_data = {
            "Name": "bianliang",
            "PublishUser": "luzhaoshan",
            "Description": "机票应用",
            "Version": Cu_Version
        }

        re = requests.post(url=self.base_url, data=body_data, files=files)
        self.result = re.json()
        self.assertEqual(self.result['message'], None)

    def test03_PostRobotPublish(self):
        """流程包名称为空"""
        files = {'file': ('bianliang', open(r'D:\Robot\bianliang.dgs', 'rb'))}
        # Version的值这个是需要唯一的，并且只能是增加的，不能减少
        f = open('D:\Robot\shuzi.txt', 'r+')    # 一定要r+模式，不然后面truncate的时候会报错
        data = f.read()
        new_data = int(data)
        # print(new_data)
        # print(f"type(new_data): {type(data)}")
        f.seek(0)  # 清除内容
        f.truncate()
        f.write(str(new_data))
        Cu_Version = "1.0.{}".format(new_data)
        f.close()

        body_data = {
            "Name": "",
            "PublishUser": "luzhaoshan",
            "Description": "机票应用",
            "Version": Cu_Version
        }

        re = requests.post(url=self.base_url, data=body_data, files=files)
        self.result = re.json()
        self.assertIn(self.result['message'], '流程包名称不能为空')
        self.assertEqual(self.result['errorCode'], 33109)

    def test04_PostRobotPublish(self):
        """没有版本号进行上传"""
        files = {'file': ('bianliang', open(r'D:\Robot\bianliang.dgs', 'rb'))}
        # Version的值这个是需要唯一的，并且只能是增加的，不能减少
        f = open('D:\Robot\shuzi.txt', 'r+')    # 一定要r+模式，不然后面truncate的时候会报错
        data = f.read()
        new_data = int(data)
        # print(new_data)
        # print(f"type(new_data): {type(data)}")
        f.seek(0)  # 清除内容
        f.truncate()
        f.write(str(new_data))
        Cu_Version = "1.0.{}".format(new_data)
        f.close()

        body_data = {
            "Name": "bianliang",
            "PublishUser": "luzhaoshan",
            "Description": "机票应用",
            "Version": ''
        }

        re = requests.post(url=self.base_url, data=body_data, files=files)
        self.result = re.json()
        self.assertEqual(self.result['message'], '版本字符串部分太短或太长。')
        self.assertEqual(self.result['errorCode'], -1)

    def test05_PostRobotPublish(self):
        """版本号小于当前版本进行上传"""
        files = {'file': ('bianliang', open(r'D:\Robot\bianliang.dgs', 'rb'))}
        # Version的值这个是需要唯一的，并且只能是增加的，不能减少
        f = open('D:\Robot\shuzi.txt', 'r+')    # 一定要r+模式，不然后面truncate的时候会报错
        data = f.read()
        new_data = int(data)
        print(new_data)
        # print(f"type(new_data): {type(data)}")
        f.seek(0)  # 清除内容
        f.truncate()
        f.write(str(new_data))
        Cu_Version = "1.0.{}".format(new_data)
        f.close()

        body_data = {
            "Name": "bianliang",
            "PublishUser": "luzhaoshan",
            "Description": "机票应用",
            "Version": ''
        }

        re = requests.post(url=self.base_url, data=body_data, files=files)
        self.result = re.json()
        self.assertEqual(self.result['message'], '版本字符串部分太短或太长。')
        self.assertEqual(self.result['errorCode'], -1)


if __name__ == '__main__':
    unittest.main()















