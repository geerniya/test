# -*- coding: utf-8 -*-
import datetime
import random
import string
import six
import hashlib

# 生成随机订单号 32位数字字符
def generate_out_trade_no():
    return '{0}{1}'.format(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), random.randint(100000000000, 999999999999))


# 生成验证签名和随机数
def calculate_sign(appsecret, params):
    random_string_list = [random.choice(string.digits + string.ascii_letters) for i in range(32)]
    random.shuffle(random_string_list)
    random_string = ''.join(random_string_list)

    joint_string = '&'.join(['{0}={1}'.format(k, params[k]) for k in sorted(params)]) + '&key={0}'.format(appsecret)
    if six.PY2:
        sign = hashlib.sha256(joint_string).hexdigest()
    else:
        sign = hashlib.sha256(joint_string.encode('utf-8')).hexdigest()

    return random_string, sign
