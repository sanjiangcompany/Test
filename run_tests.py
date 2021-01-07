import sys
sys.path.append('./interface')
from util.HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from util import Email_Project

# 指定接口测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, pattern='test*.py')


if __name__ == "__main__":
    # 执行发送邮件功能
    Email_Project.Email()
    # 执行脚本文件入口
    filename = './report/' + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Robot接口自动化测试',
                            description='运行环境：Python3.6, Requests, unittest ')
    runner.run(testsuit, rerun=0, save_last_run=False)
    fp.close()




















