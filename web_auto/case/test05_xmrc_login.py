from selenium import webdriver
import time
import unittest
from common.xmrc_login5 import Xmrc_Login

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
        xmrc = Xmrc_Login(self.driver)
        lactor1 = ("xpath", ".//*[@id='container']/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[4]/a/img")
        lactor2 = ("xpath", "//*[@id='ctl00_Body_ctl00_UsernameTextBox']")
        lactor3 = ("xpath", "//*[@id='ctl00_Body_ctl00_PasswordTextBox']")
        lactor4 = ("xpath", ".//*[@id='ctl00_Body_ctl00_LoginButton']")
        lactor5 = ("xpath", ".//*[@id='container']/table[2]/tbody/tr/td[3]/div[1]/div[2]/div[2]/span[2]")

        xmrc.click(lactor1)
        xmrc.send_keys(lactor2, "lianna90")
        xmrc.send_keys(lactor3, "903122lan")
        xmrc.click(lactor4)

        t = xmrc.is_login_succes(lactor5)
        self.assertTrue(t == '李安娜')

    def test_2(self):
        xmrc = Xmrc_Login(self.driver)
        lactor1 = ("xpath", ".//*[@id='container']/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[4]/a/img")
        lactor2 = ("xpath", "//*[@id='ctl00_Body_ctl00_UsernameTextBox']")
        lactor3 = ("xpath", "//*[@id='ctl00_Body_ctl00_PasswordTextBox']")
        lactor4 = ("xpath", ".//*[@id='ctl00_Body_ctl00_LoginButton']")
        lactor5 = ("xpath", ".//*[@id='container']/table[2]/tbody/tr/td[3]/div[1]/div[2]/div[2]/span[2]")
        xmrc.click(lactor1)
        xmrc.send_keys(lactor2, "lianna90")
        xmrc.send_keys(lactor3, "903122")
        xmrc.click(lactor4)
        t = xmrc.is_login_succes(lactor5)
        self.assertTrue(t == "")



