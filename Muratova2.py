import math
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB#top"  # Открыть страницу
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, '//*[@id="input_11_1"]') #Заполнить текстовые поля: имя
input1.send_keys('Ivan')

input2 = browser.find_element(By.XPATH, '//*[@id="input_11_2"]') # Заполнить текстовые поля: фамилия
input2.send_keys('Petrov')

input3 = browser.find_element(By.XPATH, '//*[@id="input_11_4"]') # Заполнить текстовые поля: фамилия
input3.send_keys('MMM')

input4 = browser.find_element(By.XPATH, '//*[@id="input_11_22"]') # Заполнить текстовые поля: фамилия
input4.send_keys('director')

input5 = browser.find_element(By.XPATH, '//*[@id="input_11_5"]') #Заполнить текстовые поля: email
input5.send_keys('123@mail.ru')

input6 = browser.find_element(By.XPATH, '//*[@id="input_11_5"]') #Заполнить текстовые поля: email
input6.send_keys('+79131234565')
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
input4.send_keys(file_path)

button = browser.find_element(By.XPATH, '/html/body/div[1]/form/button') # Нажать кнопку "Submit"
button.click()

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()



time.sleep(10)
browser.quit()
