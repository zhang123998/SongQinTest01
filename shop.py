
import requests
from configs.config import HOST
class Shop:
    def __init__(self,intoken):
        self.header = {"Authorization":intoken}

    def shop_list(self,inData):
        url = f"{HOST}/shopping/myShop"
        payload = inData
        resp = requests.get(url,params=payload,headers=self.header)
        return resp.json()
from login import Login
import pprint
if __name__ == '__main__':
    token = Login().login({"username":"th0330","password":"34331"},gettoken=True)
    res = Shop(token).shop_list({"page": 1,"limit" : 20})
    print(res)
    pprint.pprint(res)

