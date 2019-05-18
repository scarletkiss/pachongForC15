# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:09:46 2019

@author: dell
"""

import tkinter as tk
import tkinter.messagebox
import requests
import os
import traceback
from selenium import webdriver
import time
from tkinter import ttk

win = tk.Tk()
win.title("图片搜索下载")    # 添加标题

ttk.Label(text='').grid(row=0,padx=10)
ttk.Label(text='').grid(row=1,padx=60)
ttk.Label(text='').grid(row=2,padx=60)
ttk.Label(text='').grid(row=3,padx=60)
ttk.Label(text='').grid(row=4,padx=60)
ttk.Label(text='').grid(row=5,padx=60)
ttk.Label(text='').grid(row=6,padx=60)
ttk.Label(text='').grid(row=7,padx=60)
ttk.Label(text='').grid(row=9,padx=60)
ttk.Label(text='').grid(row=11,padx=60)
ttk.Label(text='').grid(row=13,padx=60)

ttk.Label(text='').grid(column=6,padx=35)
ttk.Label(text='').grid(column=7,padx=35)
'''
ttk.Label(text='').grid(column=8,padx=20)
ttk.Label(text='').grid(column=4,padx=20)
'''
ttk.Label(win, text="关键字：").grid(column=3, row=8)    # 添加一个标签，并将其列设置为3，行设置为8
ttk.Label(win, text="下载页数：").grid(column=3, row=10)      # 设置其在界面中出现的位置  column代表列   row 代表行
ttk.Label(win, text="文件名").grid(column=3, row=12)


# ！！！程序设计：需要import Tkinter来进行网格布局
# ！！！程序设计：

# 定义下载函数
def download(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)
def pa():
    # 创建下载目录，可以修改Imgs4成其它的，也可以下载到现有目录
    # ！！！程序设计：此处应使得下载目录可以自定义，在可视化界面下选择目录和新建目录
    if os.path.exists(name.get()) is False:
        os.makedirs(name.get())
    
    # 打开谷歌浏览器Chrome

    
    browser = webdriver.Chrome()
    
    browser.get("http://image.baidu.com")
    #print(browser.page_source)
    find_1=browser.find_element_by_id("kw")
    print('----------------------------')
    print(find_1)
    find_1.send_keys(keyWord.get())
    
    btn=browser.find_element_by_class_name("s_search")
    print('----------------------------')
    print(btn)
    btn.click()
#    
#    imgs=browser.find_elements_by_class_name("imgitem")
#    print('----------------------------')
#    print(imgs[0])
#    imgs[0].click()
#    print('----------------------------')
#    
    url=browser.find_element_by_name("pn0").get_attribute('href')
    browser.get(url)
    
    

    
    #browser.close()
    # 进入百度图片详细查看页
    # ！！！程序设计：此处链接可以直接通过粘贴变换，因此可以使用字符串变量来规定多个链接，
    # ！！！程序设计：或者通过对键入量的搜索出来的链接提取来设置此处的变量。
    # ！！！程序设计：此处链接应可以更改
    #url = 'http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%89%A1%E4%B8%B9%E8%8A%B1&step_word=&hs=0&pn=1&spn=0&di=151496180660&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=172389972%2C1050738793&os=2105520008%2C2184118427&simid=0%2C0&adpicid=0&lpn=0&ln=1919&fr=&fmq=1556352299254_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fpic152.nipic.com%2Ffile%2F20180114%2F4801598_221007284000_2.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bgtrtv_z%26e3Bv54AzdH3Ffi5oAzdH3F8lac0ba0_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'
    #browser.get(url)
    
    # 设置下载的图片数量及进行下载
    # ！！！程序设计：此处应用变量来控制开始和结束，决定爬取图片的数量
    start = 1
    end = int(name1.get())
    
    
    for i in range(start,end + 1):
    #     # 获取图片位置
        img = browser.find_elements_by_xpath("//img[@class='currentImg']")
        for ele in img:
            #   获取图片链接
            target_url = ele.get_attribute("src")
            #   设置图片名称。以图片链接中的名字为基础选取最后25个字节为图片名称。
            img_name = target_url.split('/')[-1]
            filename = os.path.join(name.get(), "3_"+str(i)+".jpeg")
            download(target_url, filename)
    #     # 下一页
        next_page = browser.find_element_by_class_name("img-next")
        next_page.click()
        time.sleep(3)
    #     # 显示进度
        print('%d / %d' % (i, end))
    
    # 关闭浏览器
    # ！！！程序设计：应该可以用别的方法来终止，关闭程序
    browser.quit()

# 按钮
action = ttk.Button(win, text="点击搜索", command=pa)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=5, row=14)    # 设置其在界面中出现的位置  column代表列   row 代表行

# 爬取关键词
keyWord = tk.StringVar()
keyWordEntered = ttk.Entry(win, width=22, textvariable=keyWord)
keyWordEntered.grid(column=5, row=8)      # 设置其在界面中出现的位置  column代表列   row 代表行
keyWordEntered.focus()     # 当程序运行时,光标默认会出现在该文本框中

# 下载数量
name1 = tk.StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
name1Entered = ttk.Entry(win, width=22, textvariable=name1)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
name1Entered.grid(column=5, row=10)       # 设置其在界面中出现的位置  column代表列   row 代表行

#目标文件夹名
name = tk.StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = ttk.Entry(win, width=22, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.grid(column=5, row=12)       # 设置其在界面中出现的位置  column代表列   row 代表行


win.mainloop()      # 当调用mainloop()时,窗口才会显示出来