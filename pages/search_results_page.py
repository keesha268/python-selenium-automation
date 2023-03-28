from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SIGN_IN = (By.XPATH, "//h1[@class='a-spacing-small']")
    CART_RESULTS = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def signin_page_open(self, expected_text):
        actual_result = self.driver.find_element(*self.SIGN_IN).text
        assert expected_text == actual_result, f'Expected {expected_text} but got {actual_result}'

    def verify_cart_empty(self, expected_text):
        actual_result = self.driver.find_element(*self.CART_RESULTS).text
        assert expected_text == actual_result, f'Expected {expected_text} but got {actual_result}'