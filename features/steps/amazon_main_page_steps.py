from selenium.webdriver.common.by import By
from behave import given, when, then


AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {text}')
def input_search_word(context, text):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)
    # print(element)


@then('Verify that footer has {expected_amount} links')
def verify_footer_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))  # '42'
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))  # => 42

    footer_links = context.driver.find_elements(*FOOTER_LINKS)
    print(footer_links)
    print('\nLink count: ', len(footer_links))
    # assert 42 == 42
    assert len(footer_links) == expected_amount, f'Expected {expected_amount} links, but got {len(footer_links)}'


@then('Verify that header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links but got {len(header_links)}'


#@when('Input for coffee')
#def input_search_word(context):
#    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')


@when('Click on cart button')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@when('Click on orders button')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify that text "Your Amazon Cart is empty" are shown')
def verify_search_result(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


@then('Verify that text "Sign in" are shown')
def verify_search_result(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'

