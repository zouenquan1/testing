import unittest
import selenium
import time
from appium import webdriver


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'W8LJWKJJ4P45MRN7'
        desired_caps['appPackage'] = 'com.sanhe.clipclaps'
        # desired_caps['appActivity'] = '.ui.activity.GuideActivity'
        desired_caps['appActivity'] = '.rebuild.act.MainActivity2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_something(self):
        print('test_something click ------ ')

        # 启动app
        time.sleep(10)
        # 刷新feed页
        self.driver.refresh()
        # 点击视频刷新
        self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_iv_video").click()
        time.sleep(3)
        # 切换到游戏页
        self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_game").click()
        time.sleep(3)
        # 切换到reward页
        self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_reward").click()
        time.sleep(3)
        # 切换到个人中心
        self.driver.find_element_by_id("com.sanhe.clipclaps:id/act_main_bottom_nav_dtv_me").click()
        time.sleep(3)
        # self.driver.find_element_by_id("com.sanhe.clipclaps:id/announcement_close").click()
        # time.sleep(5)
        self.assertEqual(True, 1)

    # @classmethod
    # def tearDown(self):
    #     time.sleep(5)
    #     print('tearDown ------ ')
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()

# el2 = driver.find_element_by_id("com.sanhe.clipclaps:id/mNewBootLogonSignUpBtn")
# el2.click()
# el3 = driver.find_element_by_id("com.sanhe.clipclaps:id/mRegisterPhoneNumber")
# el3.click()
# el4 = driver.find_element_by_id("com.sanhe.clipclaps:id/mRegisterPhoneNumber")
# el4.click()
# el4.send_keys("13458334283")
# el5 = driver.find_element_by_id("com.sanhe.clipclaps:id/mGoVerificationCodePage")
# el5.click()
# el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText")
# el6.send_keys("0093")
# el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.widget.EditText")
# el7.click()
# el7.send_keys("0")
# el7.click()
# el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[3]/android.widget.EditText")
# el8.click()
# el8.send_keys("9")
# el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[4]/android.widget.EditText")
# el9.send_keys("3")
# el10 = driver.find_element_by_id("com.sanhe.clipclaps:id/im_selected")
# el10.click()
# el10.click()
# el11 = driver.find_element_by_id("com.sanhe.clipclaps:id/announcement_close")
# el11.click()
