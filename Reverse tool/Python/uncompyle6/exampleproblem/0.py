# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 |Anaconda, Inc.| (default, Nov 13 2018, 17:33:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: /root/Desktop/123/Crackme.py
# Compiled at: 2018-10-20 10:01:07


def encrypt(key, seed, string):
    rst = []
    for v in string:
        rst.append((ord(v) + seed ^ ord(key[seed])) % 255)
        seed = (seed + 1) % len(key)

    return rst


if __name__ == '__main__':
    flag = ''
    KEY1 = 'SDUT Network and information security laboratory'
    KEY2 = [54, 14, 30, 3, 5, 30, 43, 28, 37, 231, 28, 79, 52, 44, 15, 40, 6, 17, 2, 56, 233, 22, 35, 170, 18, 24, 12,
     236, 42, 227, 39, 235, 164, 4, 193, 229, 5, 238, 239, 224, 253, 210, 222, 46]
    en_out = encrypt(KEY1, 5, flag)
    if KEY2 == en_out:
        print ('FLAG IS flag{%s}' % flag)
    else:
        print ('No')
# okay decompiling Crackme.pyc
