from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/keesh/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()
expected_text = 'Sign-In'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(actual_text)

print('Test case passed')

driver.quit()


