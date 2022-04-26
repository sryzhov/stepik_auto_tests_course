from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_value = browser.find_element_by_xpath("//*[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)
    input_value.send_keys(y)
    robot_check = browser.find_element_by_xpath("//*[@id='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)
    robot_check.click()
    robot_radio = browser.find_element_by_xpath("//*[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()
    btn = browser.find_element_by_xpath("//button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла