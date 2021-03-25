# python

import random
import time
import requests
from hashlib import md5

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"


appVersion = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"

#有道内部函数
'''
 var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()请输入您想要翻译的内容:hao do you do
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "]BjuETDhU)zqSxf-=B#7m")
        }
    };
'''

def r(e):
    # 对应 bv 参数（浏览器版本的加密数据）
    t = md5(appVersion.encode()).hexdigest()
    # 对应时间戳
    r = str(int(time.time()*1000))
    #对应时间戳加随机数
    i = r + str(random.randint(0,9))
    return {
        'ts': r,
        'bv': t,
        'salt': i,
        'sign': md5(("fanyideskweb" + e + i + "]BjuETDhU)zqSxf-=B#7m").encode()).hexdigest()
    }


#请求头参数
headers = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Content-Length":"260",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"OUTFOX_SEARCH_USER_ID=-256887737@10.108.160.18; OUTFOX_SEARCH_USER_ID_NCOO=99154088.10431568; _ntes_nnid=3136984530f893bc43dc18629e8fbb73,1597886032693; JSESSIONID=aaa2-XqkusIrA8eKfgpqx; ___rl__test__cookies=1597987562877",
    "Host":"fanyi.youdao.com",
    "Origin":"http://fanyi.youdao.com",
    "Pragma":"no-cache",
    "Referer":"http://fanyi.youdao.com/",
    "User-Agent":appVersion,
    "X-Requested-With":"XMLHttpRequest"
}

def tran(word):
    #获取相关参数
    data = r(word)
    #构建请求参数
    params = {
        "i":word,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":data['salt'],
        "sign":data['sign'],
        "lts":data['ts'],
        "bv":data['bv'],
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"
    }

    res = requests.post(url, headers=headers, data=params)
    return res.json()


# print(r("what do you want to get?"))

if __name__ == '__main__':
    while True:
    #手动输入翻译
        word = input('请输入您想要翻译的内容:')
        result = tran(word)
        r = result['translateResult'][0]
        print(r[0]['src'])
        print(r[0]['tgt'])

    # #翻译到txt文本
    # with open('english.txt',mode='r',encoding='utf-8') as f:
    #     text = f.read()
    # result = tran(text)
    # r_s = result['translateResult'][0]
    # with open('c&e.txt',mode='w',encoding='utf-8') as f:
    #     for r in r_s:
    #         f.write(r['src'])
    #         f.write('\n')
    #         f.write(r['tgt'])
    #         f.write('\n')
    #         f.write('\n')
    #         print(r['src'])
    #         print(r['tgt'])