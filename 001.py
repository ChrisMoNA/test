from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
import xlsxwriter


url = 'https://www.baidu.com/'
login_name = 'qzko3'
login_pwd = 'qzko123'
'''
woshishabi
'''

# time.sleep(5)
def openChromeModel(driver,url):
    '''
    打开浏览器和测试网页
    url:测试网页网址
    '''
    driver.get(url)


def loginModel(driver,login_name,login_pwd):
    '''
    登录模块
    '''
    firstEle = driver.find_element_by_id('//*[@id="u1"]/a[2]').click()
    time.sleep(3)
    try:
        driver.find_element_by_class_name('tang-pass-footerBarULogin').click()
    except:
        pass

    nameEle = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]')
    pwdEle = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]')
    nameEle.send_keys('')
    nameEle.clear()
    nameEle.send_keys(login_name)
    pwdEle.send_keys('')
    pwdEle.clear()
    pwdEle.send_keys(login_pwd)
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()



driver = webdriver.Chrome()
driver.maximize_window()

#调用函数打开网页
openChromeModel(driver,url)

# 登录网页
loginModel(driver,login_name,login_pwd)





# driver.get('https://tool.chinaz.com/webdetect/')
# driver.maximize_window()
# ele = driver.find_element_by_link_text('首页')
# ActionChains(driver).move_to_element(ele).perform()
# sub_ele = driver.find_element_by_xpath('//*[@id="Navbar"]/ul[1]/li[2]/a[1]')
# sub_ele.click()