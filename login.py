import requests
import pytest
import hashlib

HOST = "http://121.41.14.39:8082"


#
def get_md5(psw):
    md5 = hashlib.md5()  # 实例化一个MD5加密对象

    md5.update(psw.encode("UTF-8"))  # 调用加密方法

    return md5.hexdigest()  # 返回16进制的结果


class Login:

    # 构建接口请求
    def login(self, inData, gettoken=False):
        url = f"{HOST}/account/sLogin"  # URL
        # payload = {"username": "th0330", "password": "9abbbda872050c52f250190578b0c178"}  # 参数

        inData["password"] = get_md5(inData["password"])
        payload = inData
        resp = requests.post(url, data=payload)  # 发请求
        # print("登录接口的请求体  >>>",resp.request.body)
        # print("登录的请求头  >>>",resp.request.headers)
        """
        data:默认是表单格式
        json:默认是json格式
        params  参数放到url后面 ?  后面的
        files 文件上传接口
        """
        # 在pycharm的控制台输出的时候 ：字典一定是 单引号  json：是双引号
        # print(resp.text)    #查看响应结果，返回的是json格式 ，是字符串
        if gettoken:
            return resp.json()  # ['data']['token']
        else:
            return resp.json()  # 返回的是字典


# th0330 34331
if __name__ == '__main__':
    res = Login().login({"username": "t323230330", "password": "34331"}, gettoken=True)
    print(res)
