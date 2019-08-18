import re
def mqst(s):  # 只能算曼切斯特编码,无法算差分
    mdict = {'5': '00', '6': '01', '9': '10', 'A': '11'}
    a1 = ''.join(mdict[i] for i in s)
    a2 = ''.join(mdict[i][::-1] for i in s)
    print ('曼切斯特解码:   ', a1)
    print ('曼切斯特解码2:  ', a2)
mqst("AAAAA56A69AA55A95995A569AA95565556")
mqst("AAAAA56A69AA556A965A5999596AA95656")



