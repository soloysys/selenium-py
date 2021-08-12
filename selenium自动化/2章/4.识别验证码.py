from selenium import webdriver
import time
from PIL import Image  # 用于打开图片和对图片处理
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://xunkao.dev.pkpm.cn:9033')
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/header/div/div[3]/div/span').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[2]/div/form/div[1]/div/div/input').send_keys('515648846@qq.com')
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[2]/div/form/div[2]/div/div/input').send_keys('ys475688')

def get_picture():
    driver.save_screenshot('E:/code.png')
    code_element = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[2]/div/form/div[3]/div/img')
    left = code_element.location['x']  # 获取图片坐标
    top = code_element.location['y']
    right = code_element.size['width'] + left
    bot = code_element.size['height'] + top
    im = Image.open('E:/code.png')
    img = im.crop((left,top,right,bot))
    img.save('E:/code1.png')

code_image = get_picture()



# driver.quit()
