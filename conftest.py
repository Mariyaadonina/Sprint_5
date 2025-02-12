import pytest
from selenium import webdriver
from generators import AuthGenerator


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def generated_user():
    generated_user = AuthGenerator()
    generated_user.login = generated_user.login_generator()
    generated_user.password = generated_user.correct_password_generator()
    yield generated_user