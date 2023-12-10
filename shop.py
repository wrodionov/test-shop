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
# driver.find_element_by_id("username").send_keys("name@track.com")
# driver.find_element_by_id("password").send_keys("89103407649")
# driver.find_element_by_css_selector('.button[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
# element=driver.find_element_by_css_selector('.summary.entry-summary h1')
# element_get_text = element.text
# assert element_get_text=='HTML5 Forms'

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
# driver.find_element_by_id("username").send_keys("name@track.com")
# driver.find_element_by_id("password").send_keys("89103407649")
# driver.find_element_by_css_selector('.button[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('.cat-item.cat-item-19 a').click()
# items_count = driver.find_elements_by_css_selector(".product_cat-html")
# assert len(items_count) == 3

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("name@track.com")
# driver.find_element_by_id("password").send_keys("89103407649")
# driver.find_element_by_css_selector('.button[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# get_value = driver.find_element_by_css_selector('.orderby')
# select_value = get_value.get_attribute("value")
# print(select_value)
# assert select_value == 'menu_order'
# element = driver.find_element_by_css_selector('.orderby')
# select = Select(element)
# select.select_by_value("price-desc")
# get_value1 = driver.find_element_by_css_selector('.orderby')
# select_value1 = get_value1.get_attribute("value")
# print(select_value1)
# assert select_value1 == 'price-desc'

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.find_element_by_id("menu-item-50").click()
# driver.find_element_by_id("username").send_keys("name@track.com")
# driver.find_element_by_id("password").send_keys("89103407649")
# driver.find_element_by_css_selector('.button[name="login"]').click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('.post-169').click()
# element=driver.find_element_by_css_selector('del .woocommerce-Price-amount.amount')
# element_get_text = element.text
# assert element_get_text=='₹600.00'
# element1=driver.find_element_by_css_selector('ins .woocommerce-Price-amount.amount')
# element_get_text = element1.text
# assert element_get_text=='₹450.00'
# WebDriverWait(driver, 1).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, '[alt="Android Quick Start Guide"]')) )
# driver.find_element_by_css_selector('[alt="Android Quick Start Guide"]').click()
# WebDriverWait(driver, 3).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')) )
# driver.find_element_by_css_selector('.pp_close').click()


# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(3)
# element=driver.find_element_by_css_selector('.cartcontents')
# element_get_text=element.text
# assert element_get_text=="1 Item"
# element1=driver.find_element_by_css_selector('.wpmenucart-contents :nth-child(3)')
# element_get_text=element1.text
# assert element_get_text=='₹180.00'
# driver.find_element_by_css_selector('.wpmenucart-contents').click()
# some_element= WebDriverWait(driver, 5).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart-subtotal"), "180"))
# some_element1= WebDriverWait(driver, 5).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total"), "183.60"))

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(3)
# driver.find_element_by_css_selector('[data-product_id="180"]').click()
# time.sleep(3)
# driver.find_element_by_css_selector('.wpmenucart-contents').click()
# # time.sleep(3)
# driver.find_element_by_css_selector('.remove[data-product_id="182"]').click()
# time.sleep(3)
# driver.find_element_by_css_selector('.woocommerce-message :nth-child(1)').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input').clear()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input').send_keys('3')
# time.sleep(3)
# driver.find_element_by_css_selector('[name="update_cart"]').click()
# get_value = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
# quantity_value = get_value.get_attribute("value")
# assert quantity_value == '3'
# time.sleep(3)
# driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# element=driver.find_element_by_css_selector('.woocommerce-error :nth-child(1)')
# element_get_text=element.text
# assert element_get_text=="Please enter a coupon code."

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.maximize_window()
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(3)
driver.find_element_by_css_selector('[title="View your shopping cart"]').click()
time.sleep(6)
btn=WebDriverWait(driver, 6).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")) )
driver.find_element_by_css_selector('.checkout-button').click()
fields=WebDriverWait(driver, 6).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")) )
driver.find_element_by_id('billing_first_name').send_keys('Name')
driver.find_element_by_id('billing_last_name').send_keys('LAstName')
driver.find_element_by_id('billing_email').send_keys('name@track.com')
driver.find_element_by_id('billing_phone').send_keys('1234567890')
driver.find_element_by_id('select2-chosen-1').click()
driver.find_element_by_id('s2id_autogen1_search').send_keys('Russia')
driver.find_element_by_id('select2-results-1').click()
driver.find_element_by_id('billing_address_1').send_keys('street 23')
driver.find_element_by_id('billing_city').send_keys('dyra')
driver.find_element_by_id('billing_state').send_keys('dyrovsk')
driver.find_element_by_id('billing_postcode').send_keys('67585')
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(3)
driver.find_element_by_css_selector('[for="payment_method_cheque"]').click()
driver.find_element_by_id('place_order').click()
text_chk=WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
pay_chk=WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method"), "Check Payments"))