#!/usr/bin/python3

'''
numb1 = int(input("第一个数字:"));
numb2 = int(input("第二个数字:"));
i = numb1;
while i >= 1:
    if numb1 % i == 0 and numb2 % i == 0:
        break;
    i -= 1;
print("最大公约数:", i);
'''


numb1 = int(input("第一个数字:"));
numb2 = int(input("第二个数字:"));
i = numb1;
while True:
    if i % numb1 == 0 and i% numb2 == 0:
        break;
    i += 1;
print("最小公倍数:", i);

