import requests
from tools_2.code import get_code_2, get_code_1

def yzm():
    # 获取scode,basecode
    phone = get_code_1.phone()[0]
    password = get_code_1.phone()[1]
    code = get_code_2.code()
    scode = str(code[0])
    basecode = code[1]
    # 请求头&请求参数
    url = "https://testapialp.hemeifinance.com/home/check"
    params = {
        'user_cell_zd':'86',
        'user_cell':phone,
        'scode':scode,
        'basecode':basecode
    }
    # print(params)

    res = requests.post(url,data=params)
    list = res.json()
    list = list['data']
    # print(list)
    return list,phone,password
