import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://yohoho.cc/"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, '//*[@id="search-title"]')
input1.send_keys('123')

input2 = browser.find_element(By.XPATH,'//*[@id="search"]')
input2.click()

h1 = browser.find_element(By.XPATH, '/html/body/nav/div/div[1]/a')
h1 = h1.text

assert 'Yohoho' == h1



# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()