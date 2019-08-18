import hashlib
class MD5:
    def str():
        str=input("字符串:\n")
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        print (m.hexdigest())
        
    def filebin():
        src=input("文件路径:\n")
        f = open(src, 'rb')
        f_md5 = hashlib.md5()
        f_md5.update(f.read())
        print (f_md5.hexdigest())
        
    def file():
        src=input()
        f = open(src, 'r')
        f_md5 = hashlib.md5()
        f_md5.update(f.read().encode('utf-8'))
        print (f_md5.hexdigest())

    


if __name__=='__main__':

    try:
        while True:
            MD5.filebin()
    except EOFError:
            exit()
