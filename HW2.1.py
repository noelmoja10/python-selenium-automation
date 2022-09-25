from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/noelcanlas/Documents/Automation/python-selenium-automation/chromedriver' )
driver.maximize_window() #make window bigger


driver.get('https://www.amazon.com/') #open the URL
driver.find_element(By.ID, 'nav-orders').click() #find element by ID and click
driver.find_element(By.XPATH, "//a[@class='a-spacing-small' and a[@class='a-input-text a-span12 auth-autofocus auth-required-field'")
driver.quit()

