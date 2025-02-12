from locators import Locators
from data import Urls
from data import FixedUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:
    def test_user_should_login_successfully_by_button_on_main_page(self, driver):
        driver.get(Urls.LINK)
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_EMAIL_FIELD))
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED

    def test_user_should_login_successfully_by_account_button_in_header(self, driver):
        driver.get(Urls.LINK)
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_EMAIL_FIELD))
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED

    def test_user_should_login_successfully_by_button_on_register_page(self, driver):
        driver.get(Urls.LINK)
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.SEARCH_REGISTER_REFERENCE).click()
        driver.find_element(*Locators.SEARCH_LOGIN_REFERENCE_ON_REGISTER_PAGE).click()
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_EMAIL_FIELD))
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED

    def test_user_should_login_successfully_by_button_on_forgot_password_page(self, driver):
        driver.get(Urls.LINK)
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.SEARCH_FORGOT_PASSWORD_REFERENCE_ON_LOGIN_PAGE).click()
        driver.find_element(*Locators.SEARCH_LOGIN_REFERENCE_ON_REGISTER_PAGE).click()
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_EMAIL_FIELD))
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED