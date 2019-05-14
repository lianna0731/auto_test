from selenium import webdriver
import time
import unittest
from common.xmrc_login4 import Xmrc_Login

class Login_xmrc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        time.sleep(3)
        self.driver.maximize_window()
        self.driver.get("https://www.xmrc.com.cn/")

    def tearDown(self):
        time.sleep(3)
        self.driver.delete_all_cookies()  # 清空cookies，退出登录
        time.sleep(3)
        self.driver.close()


    def test_1(self):
        xmrc = Xmrc_Login(self.driver,'lianna90','903122lan')
        xmrc.login()
        t = xmrc.is_login_succes()
        self.assertTrue(t == '李安娜')

    def test_2(self):
        #time.sleep(3)
        #self.driver.find_element_by_xpath(".//*[@id='ctl00_ctl00_Body_FaceControl_LogoutLink']").click()
        # time.sleep(3)
        # windows_handlet = self.driver.window_handles
        # self.driver.switch_to.window(windows_handlet[1])
        xmrc = xmrc = Xmrc_Login(self.driver,'lianna90','123456')
        t = xmrc.is_login_succes()
        self.assertTrue(t == "")



