#coding:utf-8

p=473398607161
q=4511491
e=17

def egcd(a, b):
    #扩展欧几里德算法
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    #d=modinv(e,(p-1)*(q-1))
    g, x, y = egcd(a, m)
    if g != 1:
       raise Exception('modular inverse does not exist')
    else:
       return x % m
	   
d = modinv(e,(p-1)*(q-1))
print("d=\n%s"%d)