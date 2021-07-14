import requests
HOST = "http://120.55.190.222:7080"

def login():
    url = f"{HOST}/api/mgr/loginReq"
    payload = {"username":"auto","password":"sdfsdfsdf"}
    resp = requests.post(url,data=payload)
    # print(resp.headers)
    return resp.cookies['sessionid']

def add_lesson(indata):
    url = f"{HOST}/api/mgr/sq_mgr"
    usercookies = {"sessionid":indata,"token" : "123456"}
    resp = requests.post(url,cookies= usercookies)
    print(resp.request.headers)



if __name__ == '__main__':
    res = login()
    add_lesson(res)
    print(res)


    # json 转化成字典 用loads() 函数
    # 字典转化成json  用dumps()