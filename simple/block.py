#!/usr/bin/env python
# coding=utf8

import re
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class login():
    def __init__(self):
        self.login_url = "http://www.gsxt.gov.cn/index"

    def login_download_pic(self):
        self.broswer = webdriver.Firefox()
        self.broswer.get(self.login_url)
        time.sleep(3)
        self.broswer.find_element_by_xpath('//input[@id="keyword"]').send_keys(u'中国移动')
        self.broswer.find_element_by_xpath('//button[@id="btn_query"]').click()
        time.sleep(3)
        # pic_url = re.search(r'&quot;(http://static.geetest.com.+?jpg)', self.broswer.page_source).group(1)
        # return pic_url

    def merge_pic(self, pic_url):
        p = requests.get(pic_url, stream=True)
        with open('huakuai', 'wb') as f:  # 下载图片
            for chunk in p.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    def block_move(self, x=None, y=None):
        element = self.broswer.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")
        ActionChains(self.broswer).click_and_hold(on_element=element).perform()
        time.sleep(1)
        ActionChains(self.broswer).move_to_element_with_offset(to_element=element, xoffset=200, yoffset=50).perform()
        time.sleep(1)
        ActionChains(self.broswer).release(on_element=element).perform()
        time.sleep(3)


if __name__ == '__main__':
    spider = login()
    spider.login_download_pic()
    # spider.block_move()
