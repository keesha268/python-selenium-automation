from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(executable_path='/Users/keesh/python-selenium-automation/chromedriver.exe')


# Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By.ID, 'continue')

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, "//a[@id='auth-fpp-link-bottom']")

# Other issues with Sign-In link
driver.find_element(By.ID, "//a[@id='ap-other-signin-issues-link']")

# Create your Amazon account button
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")

# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Privacy Notice link



