# ******************发送邮件脚本**********************************
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# file_path = r"D:\AppsTest02\report\result.html" 这个本地文件的绝对路径编写如下：
BATH_PATH = os.path.dirname(
    os.path.dirname(__file__)
)
# print(BATH_PATH, 999999999)     # D:\AppsTest02 999999999

file_path = os.path.join(BATH_PATH, r'report\result.html')
# print(file_path, 333333333333)      # D:\AppsTest02\report\result.html 333333333333


# ----------1.跟发件相关的参数------
class Email:

    smtpserver = "smtp.163.com"           # 发件服务器
    port = 465                            # 端口
    sender = 'zhaoshan950602@163.com' # 读取配置文件中发件人
    sendpwd = 'JYRRLTHENMUIXTUA' # 读取配置文件中发件人密码

    # receiver = ['luzhaoshan@encootech.com', 'mahaining@encootech.com', 'zhangyunqi@encootech.com']  # 读取配置文件中收件人
    receiver = ['luzhaoshan@encootech.com',  'zhaoshan950602@163.com']  # 读取配置文件中收件人

    # ----------2.编辑邮件的内容------
    # 读文件
    import time
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    with open(file_path, "rb") as fp:
        print(file_path)
        mail_body = fp.read()

    msg = MIMEMultipart()
    msg["from"] = sender                       # 发件人
    msg["to"] = ";".join(receiver)             # 多个收件人list转str
    msg["subject"] = "Robot接口测试报告，详情可以打开附件查看具体结果信息"              # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)                      # 连服务器
        smtp.login(sender, sendpwd)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, sendpwd)                       # 登录

    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()


