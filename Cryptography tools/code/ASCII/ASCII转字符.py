def ASCIItostr():
    try:
        s = input()
        s=s.split()
        for i in s:
            print(chr(int(i)),end="")
        print()
    except Exception as e:
        print("",end="")


if __name__ == '__main__':

    try:
        while True:
            ASCIItostr()
    except EOFError:
        exit()




