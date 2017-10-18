#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 2.7.13
# author:TClion
# update:2017-10-17
# 豆瓣英文单词验证码识别

import Image
import pytesseract
import ImageFilter

threshold = 15    #二值化阀值，重要！
table = [0 if i < threshold else 1 for i in xrange(256)]

def string_idt():
    img = Image.open('douban.jpg')
    imgry = img.convert('L')    #灰度
    pic = imgry.point(table, '1')   #二值化
    new_pic = pic.filter(ImageFilter.MedianFilter(3))   #中值过滤，重要！
    new_pic.save('douban_1.jpg')
    return new_pic


if __name__ == '__main__':
    img = string_idt()
    string = pytesseract.image_to_string(img)
    print string