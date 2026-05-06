# SauceDemo 登录功能自动化测试

## 项目简介
使用 Python + Selenium 完成 SauceDemo 网站的登录功能自动化测试。

## 测试用例（共5条）
| 用例 | 用户名 | 密码 | 预期结果 |
|------|--------|------|----------|
| 用例1 | standard_user | secret_sauce | 登录成功 |
| 用例2 | standard_user | wrong_password | 登录失败 |
| 用例3 | standard_user | （空） | 登录失败 |
| 用例4 | （空） | secret_sauce | 登录失败 |
| 用例5 | （空） | （空） | 登录失败 |

## 技术栈
- Python 3
- Selenium WebDriver
- ChromeDriver

## 运行方式
1. 安装 Python 3
2. 安装 Selenium：pip install selenium
3. 下载对应版本的 ChromeDriver
4. 运行：python test3.py

## 作者
Sulague
