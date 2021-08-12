from selenium import webdriver
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://xunkao.dev.pkpm.cn:6002/c/login')

def creat_phone():  #自动生成手机号
    second = [3, 4, 5, 7, 8][random.randint(0,4)]
    third = {
        3: random.randint(0, 9),
        4:[5, 7, 9][random.randint(0,2)],
        5:[i for i in range(0,10) if i != 4][random.randint(0,8)],
        7:[6, 7, 8][random.randint(0,2)],
        8:random.randint(0,9)
    }[second]

    suffix = ''.join(random.sample('0123456789',8))
    return '1{}{}{}'.format(second,third,suffix)

phone = creat_phone()

driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div[2]/div[1]/form/div[1]/div/div[1]/input').send_keys(phone)
time.sleep(5)
driver.quit()

