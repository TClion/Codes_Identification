#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 2.7.13
# author:TClion
# update:2017-10-17
# 简单的数字验证码识别

import Image
import pytesseract

threshold = 140     #二值化阀值
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

img = Image.open('number.jpg')
imgry = img.convert('L')    #灰度
out = imgry.point(table, '1')   #二值化
out.save('number_1.jpg')
string = pytesseract.image_to_string(out)
print string