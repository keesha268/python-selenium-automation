from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
HEADER_LINKS = (By.CSS_SELECTOR, "#nav-xshop a.nav-a[data-csa-c-type='link']")
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')


@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Input text {text}')
def input_search_word(context, text):
    #context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)
    context.app.header.input_search_text(text)


@when('Click on search button')
def click_search(context):
    #context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()


@when('Click Amazon Orders link')
def orders_button(context):
    context.app.header.orders_button()


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@when('Click Sign In from popup')
def click_signin(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()


@when('Hover over language options')
def hover_lang_options(context):
    context.app.header.hover_lang_options()


@then('Verify Spanish option present')
def verify_lang_shown(context):
    context.app.header.verify_lang_shown()


@when('Select department books')
def select_department(context):
    context.app.header.select_department()


@when('Select department appliances')
def select_dept(context):
    context.app.header.select_dept()


@then('Verify hamburger menu icon present')
def verify_ham_menu_present(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    print('Before refresh')
    print(context.ham_menu)
    context.driver.refresh()
    # print(element)


@when('Click on ham menu')
def click_ham_menu(context):
    context.ham_menu = context.driver.find_element(*HAM_MENU)
    print('After refresh')
    print(context.ham_menu)
    context.ham_menu.click()


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


@then('Verify that text "Your Amazon Cart is empty" are shown')
def verify_search_result(context):
    expected_result = "Your Amazon Cart is empty"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'


# @then('Verify that text "Sign in" are shown')
# def verify_search_result(context):
#     expected_result = "Sign in"
#     actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
#     assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'
#     assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'


@when('Wait for {sec} sec')
def wait_for_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign in popup shown')
def verify_signin_popup_visible(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN),
        message='Signin btn not clickable'
    )

@then('Verify Sign in popup disappears')
def verify_signin_popup_not_visible(context):
    context.driver.wait.until_not(
        EC.visibility_of_element_located(SIGN_IN_BTN),
        message='Signin btn did not disappear'
    )

    # @when('Click on orders button')
    # def click_cart(context):
    #     context.driver.find_element(By.ID, 'nav-orders').click()
