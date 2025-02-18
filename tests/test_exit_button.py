from locators import Locators
from data import Urls
from data import FixedUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestClickOnExitButton:
    def test_authorized_user_move_to_login_page_by_click_on_exit_button(self, driver):
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
        driver.find_element(*Locators.SEARCH_EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_TEXT_ON_LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {Urls.LOGIN_PAGE}'