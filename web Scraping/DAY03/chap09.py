from selenium import webdriver
from selenium.webdriver.common.by import By
import time

agent_option = webdriver.ChromeOptions()
user_agent_string = "Mozilla/5.0"
agent_option.add_argument("user-agent="+user_agent_string)

driver = webdriver.Chrome(options=agent_option)
driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element(By.NAME, "id").send_keys("아이디")
driver.find_element(By.NAME, "pw").send_keys("패스워드")

driver.find_element(By.ID, "log.login").click()
time.sleep(3)
driver.quit()

# selenium API : 구글 검색어 입력
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=" + "Python")

driver.implicitly_wait(3)

search_results = driver.find_elements(By.CSS_SELECTOR, "div.yuRUdf")
print(len(search_results))

for result in search_results :
    title_element = result.find_element(By.CSS_SELECTOR, "h3")
    title = title_element.text.strip()
    print(f"{title}")

driver.quit()

from bs4 import BeautifulSoup

DRIVER = webdriver.Chrome()
driver.get('https://blog.naver.com/swf1004/221631056531')

driver.switch_to.frame("mainFrame")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

results = soup.find_all("div", {"class":"se-module"})

result1 = []
for result in results :
    remove_carriage_str = result.text.replace("\n", "")
    print(remove_carriage_str)
    result1.append(remove_carriage_str)