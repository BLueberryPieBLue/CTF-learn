from PIL import Image
import numpy as np
img = Image.open("0.png")
img_array = np.array(img)
arr1 = img_array[:]
print(arr1.shape)

f=open("./code.txt",'w+')

for x in range(1,arr1.shape[0]):
    for y in range(1,arr1.shape[1]):
        a = img_array[x,y][0]
        b = img_array[x,y][1]
        c = img_array[x,y][2]
        d = img_array[x,y][3]
        s="("+str(a)+","+str(b)+","+str(c)+","+str(d)+")\n"
        #print(s)
        f.write(s)

f.close()




