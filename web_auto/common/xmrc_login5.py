from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

"""发现元素、click、send封装成方法"""

class Xmrc_Login():
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def find_elment(self,args):
            element = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x:x.find_element(*args))
            return  element

    def click(self,args):
        element = self.find_elment(args)
        element.click()

    def send_keys(self,args,x):
        element = self.find_elment(args)
        element.send_keys(x)

    # def login(self):
    #     ele1 = WebDriverWait(self.driver, self.timeout).until(lambda x:x.find_element("xpath",".//*[@id='container']/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[4]/a/img"))
    #     ele1.click()
    #
    #     ele2 = WebDriverWait(self.driver, self.timeout).until(lambda x:x.find_element("xpath","//*[@id='ctl00_Body_ctl00_UsernameTextBox']"))
    #     ele2.send_keys(self.usename)
    #
    #     ele3 = WebDriverWait(self.driver, self.timeout).until(lambda x:x.find_element("xpath","//*[@id='ctl00_Body_ctl00_PasswordTextBox']"))
    #     ele3.send_keys(self.password)
    #
    #     ele4 = WebDriverWait(self.driver, self.timeout).until(lambda x:x.find_element("xpath", ".//*[@id='ctl00_Body_ctl00_LoginButton']"))
    #     ele4.click()

    def is_login_succes(self,args):
        try:
            ele = self.find_elment(args)
            return ele.text
        except:
            return ''

    def is_elment_exisit(self,args):
        try:
            ele = self.find_elment(args)
            return True
        except:
            return False

    def is_elment_exisit(self,args):
        ele = self.find_elments(args)
        if len(ele) == 0:
            return []
        else:
            return ele


if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("https://www.xmrc.com.cn/")
    f = Xmrc_Login(driver)
    lactor1 = ("xpath",".//*[@id='container']/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[4]/a/img")
    f.click(lactor1)
    f.send_keys(("xpath","//*[@id='ctl00_Body_ctl00_UsernameTextBox']"),"lianna90")
    f.send_keys(("xpath","//*[@id='ctl00_Body_ctl00_PasswordTextBox']"),"903122lan")
    f.click(("xpath",".//*[@id='ctl00_Body_ctl00_LoginButton']"))