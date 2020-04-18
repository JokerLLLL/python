#!/usr/bin/python3


# 摄氏温度转华氏温度的公式为 celsius * 1.8 = fahrenheit - 32

celsius = input('输入摄氏温度: 单位℃：')

fahrenheit  = float(celsius) * 1.8  + 32

print("\n华氏温度是：{} \n".format(fahrenheit));
