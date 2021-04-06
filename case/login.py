import datetime
import os
import unittest

import appium
import selenium
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from BeautifulReport import BeautifulReport as bf


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        # desired_caps['deviceName'] = '192.168.31.238:5555'
        # desired_caps['deviceName'] = '192.168.31.85:5555'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.sanhe.clipclaps'
        desired_caps['appActivity'] = '.ui.activity.GuideActivity'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(30)
        self.wdw = WebDriverWait(self.driver, 10, 1)

    def test_1(self):
        """
        浏览app各分页
        """
        www = self.driver.is_app_installed("com.sanhe.clipclaps")
        if www:
            print("app已安装，可以进行操作！")
            # time.sleep(10)
            try:
                # 不选择分类
                self.wdw.until(lambda x: x.find_element_by_id("com.sanhe.clipclaps:id/mBack")).click()

                # self.driver.find_element_by_id("com.sanhe.clipclaps:id/mBack").click()
                # 稍后选择分类
                # time.sleep(5)

                # self.driver.find_element_by_id("com.sanhe.clipclaps:id/common_dialog_confirmation_tv_later").click()
                self.wdw.until(
                    lambda x: x.find_element_by_id(
                        "com.sanhe.clipclaps:id/common_dialog_confirmation_tv_later")).click()
                # 点击 X 关闭提示框
                # time.sleep(5)
                # self.driver.find_element_by_id("com.sanhe.clipclaps:id/announcement_close").click()
                # try:
                #     self.wdw.until(lambda x: x.find_element_by_id("com.sanhe.clipclaps:id/announcement_close")).click()
                # except Exception as e:
                #     print(e)
            except Exception as e:
                print(e, "已经选择分类了！")

            # 点击视频刷新
            # self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_iv_video").click()
            self.wdw.until(
                lambda x: x.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_iv_video")).click()
            # time.sleep(5)
            # 切换到游戏页
            # self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_game").click()
            self.wdw.until(
                lambda x: x.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_game")).click()
            # time.sleep(5)
            # 切换到reward页
            # self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_reward").click()
            self.wdw.until(
                lambda x: x.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_reward")).click()
            # time.sleep(5)
            # 切换到个人中心
            # self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_me").click()
            self.wdw.until(lambda x: x.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_me")).click()
            time.sleep(2)
            self.assertEqual(True, 1)
        else:
            print("请先安装app再进行相关操作！！")


    def test_2(self):
        """
        对app的一些操作以及截图
        """
        www = self.driver.is_app_installed("com.sanhe.clipclaps")
        if www:
            # 打开通知栏
            # self.driver.open_notifications()
            # 获取手机分辨率
            print(self.driver.get_window_size())
            # 获取手机时间
            print(self.driver.device_time)
            # 截图按时间段并保存
            path = os.path.join(r"E:\testing\photo")
            print(path)
            # 格式化输出时间
            times = time.strftime("%Y-%m-%d %H:%M:%S")
            print(times)
            timess = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            # self.driver.get_screenshot_as_file(path + "/%s.png" % times)
            self.driver.get_screenshot_as_file(path + "/%s.png" % timess)

            # 关闭app
            self.driver.close_app()
            print("成功关闭app")
            # 断言成功
            self.assertEqual(True, 1, "用例成功")
        else:
            print("未检测到app")


    @unittest.skip("跳过测试")
    def test_3(self):
        """
        跳过测试
        :return:
        """
        print("这是第三条测试用例！")


    @unittest.skipUnless(1 > 2, "能成功吗？让我们拭目以待哦！")
    def test_4(self):
        """
        跳过测试
        :return:
        """
        self.assertEqual(1, 2)


    @classmethod
    def tearDown(self):
        time.sleep(5)
        print('tearDown ------ ')
        self.driver.quit()


# suite = unittest.TestSuite()  # 定义一个测试集合
# suite.addTest(unittest.makeSuite(MyTestCase))  # 把写的用例加进来（将TestCalc类）加进来
# run = bf(suite)  # 实例化BeautifulReport模块
# run.report(filename='test', description='执行用例')


if __name__ == '__main__':
    unittest.main()
