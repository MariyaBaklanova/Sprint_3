from conftest import *
from locators import Locators


class TestFromAccount_to_constructor:

    def test_move_by_click_to_constructor(self, driver):  # по клику на «Конструктор»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        constructor_h1 = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_H1).text
        assert constructor_h1 == 'Соберите бургер'

    def test_move_by_click_to_logo_with_registration(self, driver, login_data):  # по клику на логотип Stellar Burgers
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys(login_data['email'])
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(login_data['password'])
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.LOGO).click()
        constructor_h1 = driver.find_element(By.XPATH, Locators.CONSTRUCTOR_H1).text
        assert constructor_h1 == 'Соберите бургер'