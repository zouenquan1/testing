import time
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "192.168.31.238:5555",
    "appPackage": "com.sanhe.clipclaps",
    "appActivity": "com.sanhe.clipclaps/.rebuild.act.MainActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True
}

# 启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.vivo.upslide:id/recents_view").click()
time.sleep(5)
# driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_top_bar_iv_user_level").click()
# time.sleep(5)

# n = int(input('请输入个数：'))
# ls = input('请输入数字：').split()
# def solution(nums,n):
#     if n==0 or n==1:
#         return None
#     elif n==2:
#         return int(nums[1])-int(nums[0])
#     else:
#         max = int(nums[1])-int(nums[0])
#         fast=2
#         low=1
#         while n>fast:
#             temp = int(nums[fast])-int(nums[low])
#             if max < temp:
#                 max = temp
#                 fast += 1
#                 low += 1
#             else:
#                 fast += 1
#                 low += 1
#                 continue
#         return max
# res=solution(ls,n)
# print(res)

# -*- coding :  utf-8 -*-
# @Time      :  2021/1/29 17:03
# @author    :  王小王
# @Software  :  PyCharm
# @File      :  柱状图-主题可选择.py
# @CSDN      :  https://blog.csdn.net/weixin_47723732
from pyecharts.charts import Bar
# from pyecharts.faker import Faker
# from pyecharts.globals import ThemeType
# from pyecharts import options as opts
# from pyecharts.charts import Bar
#
# data_0 = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# data1 = [23, 52, 108, 93, 110, 108, 48]
# data2 = [97, 81, 118, 149, 134, 47, 66]
# c = (
#     Bar({"theme": ThemeType.MACARONS})
#         .add_xaxis(data_0)
#         .add_yaxis("商家A", data1)  # gap="0%"   这个可设置柱状图之间的距离
#         .add_yaxis("商家B", data2)  # gap="0%"   这个可设置柱状图之间的距离
#         .set_global_opts(title_opts={"text": "B标题1", "subtext": "标题2"},  # 该标题的颜色跟随主题
#                          # 该标题默认为黑体显示，一般作为显示常态
#                          # title_opts=opts.TitleOpts(title="标题")
#                          xaxis_opts=opts.AxisOpts(
#                              name='星期',
#                              name_location='middle',
#                              name_gap=30,  # 标签与轴线之间的距离，默认为20，最好不要设置20
#                              name_textstyle_opts=opts.TextStyleOpts(
#                                  font_family='Times New Roman',
#                                  font_size=16  # 标签字体大小
#                              )),
#                          yaxis_opts=opts.AxisOpts(
#                              name='数量',
#                              name_location='middle',
#                              name_gap=30,
#                              name_textstyle_opts=opts.TextStyleOpts(
#                                  font_family='Times New Roman',
#                                  font_size=16
#                                  # font_weight='bolder',
#                              )),
#
#                          # datazoom_opts=opts.DataZoomOpts(type_="inside"),  #鼠标可以滑动控制
#                          # toolbox_opts=opts.ToolboxOpts()  # 工具选项
#                          # brush_opts=opts.BrushOpts()       #可以保存选择
#                          )
#
#         .render("简单柱状图.html")
# )
# print("图表已生成！请查收！")