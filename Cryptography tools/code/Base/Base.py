import base64

def base64codes():
    s = input()
    b64encode = base64.b64encode(s.encode(encoding='utf-8'))
    b32encode = base64.b32encode(s.encode(encoding='utf-8'))
    b16encode = base64.b16encode(s.encode(encoding='utf-8'))
    print(b64encode.decode(encoding='utf-8'))
    print(b32encode.decode(encoding='utf-8'))
    print(b16encode.decode(encoding='utf-8'))
    print('---------------------------------')
    try:
        b64decode = base64.b64decode(s.encode(encoding='utf-8'))
        print(b64decode.decode(encoding='utf-8'))
    except Exception as e:
        print("",end="")
    try:
        b32decode = base64.b32decode(s.encode(encoding='utf-8'))
        print(b32decode.decode(encoding='utf-8'))
    except Exception as e:
        print("",end="")
    try:
        b16decode = base64.b16decode(s.encode(encoding='utf-8'))
        print(b16decode.decode(encoding='utf-8'))
    except Exception as e:
        print("",end="")

if __name__ == '__main__':

    try:
        while True:
            base64codes()
    except EOFError:
        exit()
