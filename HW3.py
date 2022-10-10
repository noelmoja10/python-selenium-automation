from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/noelcanlas/Documents/Automation/python-selenium-automation/chromedriver' )

driver.find_element(By.CSS_SELECTOR, "a-icon a-icon-logo")
driver.find_element(By.CSS_SELECTOR, "a-spacing-small")
driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "a-input-text a-span12 a-spacing-micro auth-required-field auth-require-claim-validation")
driver.find_element(By.ID, "ap_password")
driver.find_element((By.CSS_SELECTOR, "a-alert-content"))
driver.find_element(By.ID, "ap_password_check")
driver.find_element(By.CSS_SELECTOR, "a-button-input"))
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a-link-emphasis")

