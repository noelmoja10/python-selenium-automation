from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BESTSELLER = (By.CSS_SELECTOR, '_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq')

@when('Open Amazon Bestsellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then("User sees 5 links on page")
def links_on_page(context):
    links = context.driver.find.element(*BESTSELLER)
    assert len(links) == 5, "Expected 5 links but got {len(links)}"