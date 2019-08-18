#!/usr/bin/python
# -*- coding:utf8 -
#py27
import binascii
import string
dic=range(0,9)
crc = 0x69C821E0   # 记得要以0x开头
for i in dic :
    for j in dic:
        for p in dic:
            for q in dic:
                for a in dic:
                    for b in dic:
                        s=(str(i)+str(j)+str(p)+str(q) +str(a)+str(b)).encode()
                        if crc == (binascii.crc32(s) & 0xffffffff):
                            print(s)
