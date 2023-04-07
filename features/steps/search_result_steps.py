from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
BESTSELLERS_ICON = (By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
BESTSELLER_LINKS = (By.ID, 'zg_header a')
#SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
# SIGN_IN = (By.XPATH, "//h1[@class='a-spacing-small']")



@then('Verify {expected_result} page is opened')
def verify_search_result(context, expected_result):
    context.app.search_results_page.signin_page_open(expected_result)


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)


@then('Verify books department is selected')
def verify_selected_dept(context):
    context.app.search_results_page.verify_selected_dept()


@then('Verify appliances department is selected')
def verify_appliance_dept(context):
    context.app.search_results_page.verify_appliance_dept()


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


@when('Click on bestsellers icon')
def click_first_product(context):
    context.driver.find_element(*BESTSELLERS_ICON).click()
    sleep(2)


@then('Verify there are {expected_amount} links')
def verify_bestseller_links(context, expected_amount):
    expected_amount = int(expected_amount)
    bestseller_links = context.driver.find_elements(*BESTSELLER_LINKS)
    assert len(bestseller_links) == expected_amount, f'Expected {expected_amount} links but got {len(bestseller_links)}'


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    # [WebElement1, WebElement2, WebElement3, ..]
    print(f'Amount of products found: {len(all_products)}')
    print(all_products)

    for product in all_products:
        print(product)
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image is missing'

        product_tile = product.find_element(*PRODUCT_TITLE).text
        print(product_tile)
        assert product_tile, 'Product title is missing'




