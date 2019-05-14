from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

"""使用driver.find_element方法"""

class Xmrc_Login():

    def __init__(self,driver,username,password):
        self.driver = driver
        self.password = password
        self.usename = username

    def login(self):
        ele1 = WebDriverWait(self.driver, 10).until(lambda x:x.find_element("xpath",".//*[@id='container']/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[4]/a/img"))
        ele1.click()

        ele2 = WebDriverWait(self.driver, 10).until(lambda x:x.find_element("xpath","//*[@id='ctl00_Body_ctl00_UsernameTextBox']"))
        ele2.send_keys(self.usename)

        ele3 = WebDriverWait(self.driver, 10).until(lambda x:x.find_element("xpath","//*[@id='ctl00_Body_ctl00_PasswordTextBox']"))
        ele3.send_keys(self.password)

        ele4 = WebDriverWait(self.driver, 10).until(lambda x:x.find_element("xpath", ".//*[@id='ctl00_Body_ctl00_LoginButton']"))
        ele4.click()


    def is_login_succes(self):
        try:
            ele = WebDriverWait(self.driver, 10).until(lambda x:x.find_element("xpath", ".//*[@id='container']/table[2]/tbody/tr/td[3]/div[1]/div[2]/div[2]/span[2]"))
            return ele .text
        except:
            return ''

if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("https://www.xmrc.com.cn/")
    f = Xmrc_Login(driver,'lianna90','903122lan')
    f.login()