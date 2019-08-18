#coding:utf-8

import binascii
import string 
import zipfile
# def tansnum(s):
#     return int(s, 16)  转十六进制


dic=string.printable

def CrackCrc(crc):
    for i in dic :
        for j in dic:
            for p in dic:
                for q in dic:
                    s=i+j+p+q
                    if crc == (binascii.crc32(s) & 0xffffffff):
                        print (s)
                        #return 


def getcrc32():
    l=[]
    for b in range(68):
        file = 'out' + str(b) + '.zip'
        f = zipfile.ZipFile(file,'r')
        GetCrc = f.getinfo('data.txt')
        crc = GetCrc.CRC
        l.append(hex(crc))
    return l



if __name__  == "__main__":
    #c = open('out.txt', 'w')
    l = getcrc32()
    for i in l:
       CrackCrc(i)
    #c.close()
