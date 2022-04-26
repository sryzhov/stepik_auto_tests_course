from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_xpath("//*[@id='num1']")
    x_value = int(x.text)
    print(x_value)
    y = browser.find_element_by_xpath("//*[@id='num2']")
    y_value = int(y.text)
    print(y_value)

    sum_ = x_value + y_value
    print(sum_)
    str_sum = str(sum_)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str_sum)

    btn = browser.find_element_by_xpath("//button")
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла