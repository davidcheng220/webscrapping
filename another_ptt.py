from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests

service = Service("chromedriver.exe")
url = "https://www.ptt.cc/bbs/index.html"
driver = Chrome(service=service)

driver.get(url=url)

# static class = By.ByClassName
# static class = By.ByCssSelector
# static class = By.ById
# static class = By.ByLinkText
# static class = By.ByName
# static class = By.ByPartialLinkText
# static class = By.ByTagName
# static class = By.ByXPath
# static interface = By.Remotable

# xpath 的相對路徑
# copy path
# //*[@id="main-container"]/div[2]/div[2]/a
# copy full path
# /html/body/div[2]/div[2]/div[2]/a
# driver.find_element(by=By.XPATH, "/html/body/div[2]/div[2]/div[2]/a").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/a").click()
driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/button").click()

# time.sleep(10)

# get cookies and find cookies
# print(driver.get_cookies())
# cookies = {cookie_dict["name"]: cookie_dict["value"] for cookie_dict in driver.get_cookies()}
cookies = {}
for cookie_dict in driver.get_cookies():
    cookies[cookie_dict["name"]] = cookie_dict["value"]


res = requests.get(url=url, cookies=cookies)
print(res.text)
time.sleep(10)