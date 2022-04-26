from selenium import webdriver
import time 
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH,"//*[@id='price']"),"$100")
    )

    btn = browser.find_element_by_xpath("//button[@id='book']")
    btn.click()

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_value = browser.find_element_by_xpath("//*[@id='answer']")
    input_value.send_keys(y)
    btn = browser.find_element_by_xpath("//button[@id='solve']")
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла