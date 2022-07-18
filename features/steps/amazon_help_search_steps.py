from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')