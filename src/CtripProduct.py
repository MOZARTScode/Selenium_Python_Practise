from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Firefox()
try:
  browser.get('http://vacations.ctrip.com/tour/detail/p17699935s1.html?kwd=%e4%b8%89%e4%ba%9a')
  wait = WebDriverWait(browser, 20)
  score = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="score_s"]')))
  print(score.text)
  browser.
except TimeoutException:
  print("time out!")
browser.close()

# quote用于转码，给中文、特殊字符转码，ex:quote('手机') 结果为：'%E6%89%8B%E6%9C%BA'
# r2 = requests.post('http://vacations.ctrip.com/tour/restapi/gateway/10124/GetUserInfo.json', headers=headers)