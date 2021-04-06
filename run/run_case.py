import datetime
import os
import unittest

from BeautifulReport import BeautifulReport as bf

test_dir = os.path.join(r"E:\testing\case")
report_dir = os.path.join(r"E:\testing\report")
discover = unittest.defaultTestLoader.discover(test_dir, 'login.py', None)
now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(now)
bf(discover).report(description='测试', filename=filename, report_dir="../report")

if __name__ == '__main__':
    unittest.main()
