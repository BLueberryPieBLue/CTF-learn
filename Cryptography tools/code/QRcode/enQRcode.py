import qrcode
import os
import sys
import time
#pip install zxing解析库，还需要安装PIL，pillow和qrCode库
QRImagePath = os.getcwd() + '/qrcode.png'   #临时存储位置
qr = qrcode.QRCode(     
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)   #设置图片格式
print("input:QRcode image:")
data = input()  #运行时输入数据
qr.add_data(data)
qr.make(fit=True)
 
img = qr.make_image()
img.save('qrcode.png')  #生成图片
 
if sys.platform.find('darwin') >= 0:
    os.system('open %s' % QRImagePath)
    
elif sys.platform.find('linux') >= 0:
    os.system('xdg-open %s' % QRImagePath)
else:
    os.system('call %s' % QRImagePath)
    
time.sleep(5)   #间隔5个单位
#os.remove(QRImagePath)  #删除图片
