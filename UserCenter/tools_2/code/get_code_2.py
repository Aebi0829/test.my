from tools_2.code import get_code_1
import requests
import base64

def code():
    # 获取未解码的basecode,scode
    word = get_code_1.scode()
    # print(word)
    url = 'https://testapialp.hemeifinance.com/Home/setslidercode'
    params = {
        'scode': word
    }
    header ={
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = requests.post(url, headers=header,data=params)
    list = res.json()
    # print(list)
    list = list['data']['basecode']
    scode = word
    basecode = base64.b64decode(list[16:-16])
    basecode = str(basecode,'utf-8')
    # print(scode,basecode)
    return scode,basecode

