from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/keesh/python-selenium-automation/chromedriver.exe')

# By CSS, using class
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')


# By CSS, using ID
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_password')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
driver.find_element(By.CSS_SELECTOR, '#continue')


# CSS, from parent to child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*=condition_of_use]")
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*=privacy_notice]")


# Attributes, partial match *=
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid']")


