import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element('/html/body/form/div/div/button')

time.sleep(3)
browser.quit()