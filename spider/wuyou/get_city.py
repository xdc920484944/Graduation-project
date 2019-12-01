import requests
import re

import urllib3


def Get_city():
    url = 'https://js.51jobcdn.com/in/resource/js/2019/search/common.7331dab4.js'
    urllib3.disable_warnings()
    res = requests.get(url)
    result = re.findall('use strict";window.area={([^}]*)', res.text)
    lists = result[0].split(',')
    city = {}
    for _list in lists:
        _list = _list.replace('"', '').split(':')
        city[_list[1]] = _list[0]
    return city
