import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector(".post-160 :nth-child(2)").click()
driver.find_element_by_css_selector(".reviews_tab").click()
driver.find_element_by_css_selector(".star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("name")
driver.find_element_by_id("email").send_keys("name@track.com")
driver.find_element_by_css_selector("#submit.submit").click()