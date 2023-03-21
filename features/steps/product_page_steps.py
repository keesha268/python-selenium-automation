from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(4)

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()     # This would only click 1 color

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)

    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current Color: ', current_color)