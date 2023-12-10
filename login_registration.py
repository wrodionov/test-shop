
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("reg_email").send_keys("name@track.com")
# driver.find_element_by_id("reg_password").send_keys("89103407649")
# driver.find_element_by_css_selector('.button[name="register"]').click()

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("name@track.com")
driver.find_element_by_id("password").send_keys("89103407649")
driver.find_element_by_css_selector('.button[name="login"]').click()
element=driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link--customer-logout a')
element_get_text = element.text
assert element_get_text=='Logout'

