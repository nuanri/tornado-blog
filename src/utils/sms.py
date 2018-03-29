import requests
import json
# import urllib

import settings


def sms(email, data={}):
    url = "http://api.sendcloud.net/apiv2/mail/sendtemplate"

    # xsmtpapi = {
    #     'to': ['test1@ifaxin.com', 'test2@ifaxin.com'],
    #     'sub': {
    #         '%name%': ['user1', 'user2'],
    #         '%money%': ['1000', '2000'],
    #     }
    # }


    xsmtpapi = {
        'to': [email],
        'sub': {
            '%name%': [data["name"]],
            '%authcode%': [data["code"]],
        }
    }

    params = {
        "apiUser": settings.API_USER,    # 使用apiUser和apiKey进行验证
        "apiKey": settings.API_KEY,
        "templateInvokeName": "nuanri_authcode",
        "xsmtpapi": json.dumps(xsmtpapi),
        "from": "jy_shi@163.com",    # 发信人, 用正确邮件地址替代
        "fromName": "暖日",
        "subject": "暖日帐号--邮箱身份验证"
    }

    # filename = "./test.txt"
    # display_filename = "filename"
    #
    # files = {"attachments": (urllib.quote(display_filename), open(filename, "rb"))}
    # r = requests.post(url, files=files, data=params)

    res = requests.post(url, data=params)
    res = json.loads((res.content).decode('utf8'))

    return res
