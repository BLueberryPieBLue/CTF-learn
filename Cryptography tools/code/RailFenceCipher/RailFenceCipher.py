#coding=utf-8
def railFenceCipher():
    e = input()
    elen = len(e)
    field=[]
    for i in range(2,elen):
        if(elen%i==0):
            field.append(i)

    for f in field:
        b = int(elen / f)
        result = {x:'' for x in range(b)}
        for i in range(elen):
            a = i % b;
            result.update({a:result[a] + e[i]})
        d = ''
        for i in range(b):
            d = d + result[i]
        print (d.lower())


if __name__ == '__main__':

    try:
        while True:
            railFenceCipher()
    except EOFError:
        exit()
     
