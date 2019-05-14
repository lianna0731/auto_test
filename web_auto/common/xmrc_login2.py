from selenium import webdriver
import time

class Xmrc_Login():

    def __init__(self,driver,username,password):
        self.driver = driver
        self.password = password
        self.usename = username

    def login(self):
        self.driver.find_element_by_xpath(".//*[@id='container']/table[1]/tbody/tr[3]/td/table/tbody/tr[1]/td[4]/a/img").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='ctl00_Body_ctl00_UsernameTextBox']").send_keys(self.usename)
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='ctl00_Body_ctl00_PasswordTextBox']").send_keys(self.password)
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='ctl00_Body_ctl00_LoginButton']").click()


    def is_login_succes(self):
        try:
            el = self.driver.find_element_by_xpath(".//*[@id='container']/table[2]/tbody/tr/td[3]/div[1]/div[2]/div[2]/span[2]").text
            return el
        except:
            return ''

if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get("https://www.xmrc.com.cn/")
    f = Xmrc_Login(driver,'lianna90','903122lan')
    f.login()