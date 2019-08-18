def strtoASCII():
    try:
        s = input()
        for i in s:
            print(ord(str(i)),end=" ")
        print()
    except Exception as e:
        print("",end="")


if __name__ == '__main__':

    try:
        while True:
            strtoASCII()
    except EOFError:
        exit()


