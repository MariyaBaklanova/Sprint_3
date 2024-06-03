from conftest import *
from random import randint
from locators import Locators


class TestRegistration:

    def test_registration_success(self, driver):  # успешная регистрация
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_LINK).click()
        driver.find_element(By.NAME, Locators.NAME_FIELD).send_keys('Мари')
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys(f"marybaklanova{randint(1,100000)}@ya.ru")
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(f"{randint(100000,999999)}")
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()
        login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).text
        assert login_button == 'Войти'

    def test_registration_incorrect_password(self, driver):   # ошибка для некорректного пароля
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_LINK).click()
        driver.find_element(By.NAME, Locators.NAME_FIELD).send_keys('Мари')
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys(f"marybaklanova{randint(1,100000)}@ya.ru")
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(f"{randint(10000,99999)}")
        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()
        incorrect_password_message = driver.find_element(By.XPATH, Locators.INCORRECT_PASSWORD_MESSAGE).text
        assert incorrect_password_message == 'Некорректный пароль'