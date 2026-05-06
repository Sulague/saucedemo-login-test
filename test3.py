from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 


# driver=webdriver.Chrome(service=Service(executable_path='./chromedriver.exe'))
def login_test(name,password,test_name,excepted_in_msg):
    # ""一个通用的登录测试函数""
    print(f"[{test_name}]测试中")

    driver=webdriver.Chrome(service=Service(executable_path='./chromedriver.exe'))
    driver.get("https://www.saucedemo.com")
    time.sleep(3)


    driver.find_element(By.ID,"user-name").send_keys(name)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()
    time.sleep(2)

    if excepted_in_msg =="Products":
        title=driver.find_element(By.CLASS_NAME,"title").text
        driver.quit()
        assert title=="Products"
        print(f"[{test_name}]通过")

    else:
        error_msg=driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
        driver.quit()
        assert excepted_in_msg in error_msg
        print(f"[{test_name}]通过，错误信息：{error_msg}")


login_test("standard_user","secret_sauce","用例1-密码正确","Products")
login_test("standard_user","Wrong_secret","用例2—错误密码","Epic sadface")
login_test("standard_user","","用例3-空密码","Epic sadface")
login_test("","secret_suace","用例4-空用户名","Epic sadface")
login_test("","","用例5-全空","Epic sadface")