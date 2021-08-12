from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 浏览器初始化
def driver_init():
    driver.get('https://xunkao.dev.pkpm.cn:9033')
    driver.maximize_window()
    time.sleep(2)

# 获取element信息
def get_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element
# 运行主程序
def run_main():
    driver_init()
    get_element('/html/body/div/div/div[1]/div/header/div/div[3]/div/span').click()
    get_element('/html/body/div[1]/div/div[4]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys('515648846@qq.com')
    get_element('/html/body/div[1]/div/div[4]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys('ys475688')
    get_element('/html/body/div[1]/div/div[4]/div/div/div[2]/div/form/div[3]/div/div/input').send_keys('111')
    get_element('/html/body/div[1]/div/div[4]/div/div/div[2]/div/form/div[5]/div/button').click()
    time.sleep(5)
    driver.quit()

run_main()

