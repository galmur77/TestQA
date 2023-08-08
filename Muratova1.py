import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html" #Открыть страницу https://suninjuly.github.io/selects1.html
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text # Найти 1 число
num1 = int(num1)

num2 = browser.find_element(By.XPATH,'//*[@id="num2"]').text # Найти 2 число
num2 = int(num2)
value = str (num1 + num2) #Посчитать сумму заданных чисел
print('num1 + num2=', value)

select = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]')) # Выбрать в выпадающем списке значение равное расчитанной сумме
select.select_by_visible_text(value)

button = browser.find_element(By.XPATH, '/html/body/div/form/button') # Находим кнопку
button.click() #Нажать кнопку "Submit"



# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()