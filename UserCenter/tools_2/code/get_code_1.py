import time
import random



def scode():
    # 获取scode
    m = int(time.time() * 1000)
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    code = str(m) + str(a) + str(b) + str(c) + str(d)
    scode = int(code)
    return scode

def phone():
    res = 140
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    e = random.randint(0, 9)
    f = random.randint(0, 9)
    g = random.randint(0, 9)
    h = random.randint(0, 9)
    phone = str(res)+str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)
    phone = int(phone)
    # print(phone)
    password = 'qwer1234'
    return phone,password

def account():
    account = phone()

def ID_number():
    m = int(time.time()*10000)
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    ID = str(m) + str(a) + str(b) + str(c) + str(d)
    ID = int(ID)
    # print(ID)
    return ID


