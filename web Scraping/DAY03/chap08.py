from selenium import webdriver
import time

driver = webdriver.Chrome()  # 크롭 웹 브라우저 사용
driver.get("https://www.selenium.dev/selenium/web/web-form.html") # 해당하는 사이트로 이동

print(driver.title)
print(driver.page_source)
time.sleep(2)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.pythonscraping.com/pages/warandpeace.html')
driver.implicitly_wait(5)

name = driver.find_element(By.CLASS_NAME, "green")
print(name.text)

name_list = driver.find_elements(By.CLASS_NAME, "green")
for name in name_list:
    print(name.text)

driver.quit()