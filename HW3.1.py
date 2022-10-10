from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/noelcanlas/Documents/Automation/python-selenium-automation/chromedriver' )
driver.maximize_window() #make window bigger


driver.get('https://www.amazon.com/') #open the URL
driver.find_element(By.CSS_SELECTOR, "a[href*='nav_orders_first']").click() #find element by ID and click
driver.quit()

