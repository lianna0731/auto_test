import unittest
from common import HTMLTestRunner_cn

dirc = "D:\\pycharm_project\\web_auto\\case"
pattern = "test*.py"

discover = unittest.defaultTestLoader.discover(start_dir=dirc,pattern=pattern)
#print(discover)

reportpath = "D:\\pycharm_project\\web_auto\\report\\" + "report.html"



fp = open(reportpath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="厦门人才市场测试报告",\
                                          description="测试登录功能")
runner.run(discover)
