def decrypt(key1,seed,key2):
    str = ''
    for i in key2:
        v = (i^ord(key1[seed]))-seed
        seed = (seed+1)%255
        str += chr(v)
        print(str)
    return str

if __name__ == '__main__':
    KEY1 = 'SDUT Network and information security laboratory'
    KEY2 = [54, 14, 30, 3, 5, 30, 43, 28, 37, 231, 28, 79, 52, 44, 15, 40, 6, 17, 2, 56, 233, 22, 35, 170, 18, 24, 12,
     236, 42, 227, 39, 235, 164, 4, 193, 229, 5, 238, 239, 224, 253, 210, 222, 46]
    print (decrypt(KEY1,5,KEY2))
