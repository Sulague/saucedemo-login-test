from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(executable_path='./chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com")

time.sleep(3)
#登录
# username_box=driver.find_element(By.ID,"user-name")
# username_box.send_keys("standard_user")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
# password_box=driver.find_element(By.ID,"password")
# password_box.send_keys("secret_sauce")
# print("输入了密码" )
driver.find_element(By.ID,"password").send_keys("secret_sauce")
# login_bottom=driver.find_element(By.ID,"login-button")
# login_bottom.click()
# print("点击登录按钮")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

#获取页面文字(一次获取多个，CLASS_NAME相同)
items=driver.find_elements(By.CLASS_NAME,"inventory_item_name")
for i in items:
    print(i.text)

#获取页面标题
title=driver.find_element(By.CLASS_NAME,"title").text
#assert 自动判断，预期==结果
assert title == "Products"
print("测试通过，登录成功，页面标题正确")
# print("标题是："+title)
input()
driver.quit()