# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author  :   {Richard Li}
@License :   (C) Copyright 2013-2017, {BUPT}
@Contact :   {543306408@qq.com}
@Software:   PyCharm
@File    :   python].py
@Time    :   2019/3/29 23:58
@Desc    :
"""
import requests
import os
import traceback
from selenium import webdriver
import time
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

# 创建下载目录，可以修改Imgs4成其它的，也可以下载到现有目录
# ！！！程序设计：此处应使得下载目录可以自定义，在可视化界面下选择目录和新建目录
if os.path.exists('imgsP') is False:
    os.makedirs('imgsP')

# 打开谷歌浏览器Chrome
browser = webdriver.Chrome()

# 进入百度图片详细查看页
# ！！！程序设计：此处链接可以直接通过粘贴变换，因此可以使用字符串变量来规定多个链接，
# ！！！程序设计：或者通过对键入量的搜索出来的链接提取来设置此处的变量。
# ！！！程序设计：此处链接应可以更改
url = 'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E9%A6%99%E6%B0%B4&step_word=&hs=0&pn=1&spn=0&di=178779556230&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2352711305%2C2868017379&os=2386432233%2C3137367204&simid=3292106744%2C195904505&adpicid=0&lpn=0&ln=1631&fr=&fmq=1555746432795_R&fm=detail&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201404%2F20%2F20140420074812_crunX.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B17tpwg2_z%26e3Bv54AzdH3Fks52AzdH3F%3Ft1%3Dc0a09lcd0&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'
browser.get(url)

# 设置下载的图片数量及进行下载
# ！！！程序设计：此处应用变量来控制开始和结束，决定爬取图片的数量
start = 1
end = 400


for i in range(start,end + 1):
#     # 获取图片位置
    img = browser.find_elements_by_xpath("//img[@class='currentImg']")
    for ele in img:
        #   获取图片链接
        target_url = ele.get_attribute("src")
        #   设置图片名称。以图片链接中的名字为基础选取最后25个字节为图片名称。
        img_name = target_url.split('/')[-1]
        filename = os.path.join('imgsP', "3_"+str(i)+".jpeg")
        download(target_url, filename)
#     # 下一页
    next_page = browser.find_element_by_class_name("img-next").click()
    time.sleep(3)
#     # 显示进度
    print('%d / %d' % (i, end))

# 关闭浏览器
# ！！！程序设计：应该可以用别的方法来终止，关闭程序
browser.quit()
