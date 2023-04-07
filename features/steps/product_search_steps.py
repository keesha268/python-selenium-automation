from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()


@then('Verify that the user sees the deals')
def verify_deals_shown(context):
    context.app.header.verify_deals_shown()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
