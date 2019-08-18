import base64

def base64codes(s):
    b64encode = base64.b64encode(s.encode(encoding='utf-8'))
    b32encode = base64.b32encode(s.encode(encoding='utf-8'))
    b16encode = base64.b16encode(s.encode(encoding='utf-8'))
    #print(b64encode.decode(encoding='utf-8'))
    #print(b32encode.decode(encoding='utf-8'))
    #print(b16encode.decode(encoding='utf-8'))
    #print('---------------------------------')
    b64decode = base64.b64decode(s.encode(encoding='utf-8'))
    #print(b64decode.decode(encoding='utf-8'))
    p.write(b64decode.decode(encoding='utf-8'))
    


blocksize=200
p=open('18.txt','w+')
f=open('17.txt','r')

try:
    while True:
        a=f.read(blocksize)
        if a:
            base64codes(a)
        else:
            print("OK")
except EOFError:
    exit()



f.close()
p.close()


   
