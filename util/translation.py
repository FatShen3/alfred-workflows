#!/usr/bin/python
# encoding: utf-8

import httplib
import urllib
import random
import json
import re
from log import log
from encode import md5Encode

# some key data
KEY_DATA = {
    "fanyi_appid": "2015063000000001",
    "fanyi_secretKey": "12345678",
    "fanyi_api": "/api/trans/vip/translate",
    "fanyi_url": "fanyi-api.baidu.com",
    "fanyi_open": "http://fanyi.baidu.com/translate#{fromLang}/{toLang}/{q}"
}

# 翻译接口，目前调用百度翻译
def fanyi (q, wf):
    q = ' '.join(q)
    myurl = KEY_DATA['fanyi_api']
    appid = KEY_DATA['fanyi_appid']
    secretKey = KEY_DATA["fanyi_secretKey"]

    fromLang = 'en'
    toLang = 'zh'
    matchObj = re.match(r'((\S+)>(\S+) )?(.*)', q)
    if matchObj:
        groups = matchObj.groups()
        if groups[1] and groups[2]: # 自定义了语言来源
            fromLang, toLang = groups[1], groups[2]
        q = groups[3]
    httpClient = None
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = md5Encode(sign)
    myurl = myurl + '?appid=' + appid + '&q=' + \
        urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + \
        '&salt=' + str(salt) + '&sign=' + sign
    log('翻译请求url =%s', myurl)
    try:
        httpClient = httplib.HTTPConnection(KEY_DATA["fanyi_url"])
        httpClient.request('GET', myurl)

        response = httpClient.getresponse()
        rst = json.loads(response.read())
    except Exception, e:
        raise e
    finally:
        if httpClient:
            httpClient.close()
    #{"from":"en","to":"zh","trans_result":[{"src":"apple","dst":"\u82f9\u679c"}]}
    #{"error_code":"54001","error_msg":"Invalid Sign"}
    if rst.get('error_code'):
        return json.dumps(rst)
    else:
        for trans in rst.get('trans_result'):
            item = wf.add_item(title = trans["dst"], subtitle = trans["src"],
                        arg = KEY_DATA["fanyi_open"].format(fromLang = fromLang, toLang = toLang, q = q), valid = True)
            item.add_modifier('cmd', subtitle = u'\U0001f50a' + trans["src"])
# 另一个接口...数据全面的多
def fanyiv (q ,f):
  pass