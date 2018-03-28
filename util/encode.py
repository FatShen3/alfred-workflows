#!/usr/bin/python
# encoding: utf-8
from log import log
import hashlib
import base64

def md5Encode (str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def sha1 (str):
    s = hashlib.sha1()
    s.update(str)
    return s.hexdigest()

def atob (str):
    return base64.b64decode(str)

def btoa (str):
    return base64.b64encode(str)

def encode (args, wf):
    type = args[0]
    str = ' '.join(args[1:])
    log('encode type:' + type)
    if not type in ENCODE_FUNC:
        wf.add_item(title='不支持的编码格式: {0}'.format(type), valid = False)
    else:
        rst = ENCODE_FUNC[type](str)
        wf.add_item(title = '{}: {}'.format(type, str), subtitle = rst,
                        arg = rst, valid = True)

# 各种编码函数方法
ENCODE_FUNC = {
    "md5": md5Encode,
    "atob": atob,
    "btoa": btoa,
    "sha1": sha1
}