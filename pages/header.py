from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart-count-container')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS = (By.XPATH, "//a[@aria-label='New Arrivals']")
    ARRIVAL_DEALS = (By.CSS_SELECTOR, '.nav-fullWidthSubnavFlyout.nav-flyout')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def orders_button(self):
        self.click(*self.ORDERS_BTN)

    def cart_icon(self):
        self.click(*self.CART)

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self):
        department_drop_d = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_drop_d)
        select.select_by_value('search-alias=stripbooks')

    def select_dept(self):
        department_drop_down = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_drop_down)
        select.select_by_value('search-alias=appliances')

    def hover_new_arrivals(self):
        arrivals_options = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(arrivals_options)
        actions.perform()

    def verify_deals_shown(self):
        self.wait_for_element_appear(*self.ARRIVAL_DEALS)
