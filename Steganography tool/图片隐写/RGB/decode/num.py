#!/usr/bin/python
num = int(input())
def output(num):
    num=int(num)
    for i in range(2,num):
        if num % i == 0 : 
          print (i),
          output(num/i)
          return
    print (num)
    return 

output(num)
