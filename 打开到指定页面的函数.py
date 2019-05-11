# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:54:11 2019

@author: Mercer
"""

from selenium import webdriver

keyWord="茉莉花"

browser = webdriver.Chrome()

browser.get("http://image.baidu.com")
#print(browser.page_source)
find_1=browser.find_element_by_id("kw")
print('----------------------------')
print(find_1)
find_1.send_keys(keyWord)

btn=browser.find_element_by_class_name("s_search")
print('----------------------------')
print(btn)
btn.click()

imgs=browser.find_elements_by_class_name("imgitem")
print('----------------------------')
print(imgs[0])
imgs[0].click()

#browser.close()