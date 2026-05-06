from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(executable_path='./chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com")
time.sleep(3)

#======用例1:正确密码=======
print("用例1：正确密码")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

title=driver.find_element(By.CLASS_NAME,"title").text
assert title=="Products"
print("用例1通过：正确密码登录成功")

driver.quit()

#=====用例2：错误密码登录=====
print("用例2：测试密码错误")

#重新打开网页
service=Service(executable_path='./chromedriver.exe')
driver=webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com")
time.sleep(3)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce1")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

#获取错误提示
msg=driver.find_element(By.CSS_SELECTOR,"[data-test=error]").text
print("错误提示："+msg)

assert "Epic sadface"in msg 
print("用例2通过：错误密码登录被正确拦截！")

input()
driver.quit()