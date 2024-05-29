from conftest import *
from locators import Locators


class TestLogin:

    def test_login_through_authorization_button(self, driver):  # по кнопке «Войти в аккаунт» на главной
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        order_button = driver.find_element(By.XPATH, Locators.ORDER_BUTTON).text
        assert order_button == 'Оформить заказ'

    def test_login_through_profile_button(self, driver):  # через кнопку «Личный кабинет»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        order_button = driver.find_element(By.XPATH, Locators.ORDER_BUTTON).text
        assert order_button == 'Оформить заказ'

    def test_login_through_login_link(self, driver):  # через кнопку в форме регистрации
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        driver.find_element(By.XPATH, Locators.REGISTER_LINK).click()
        driver.find_element(By.XPATH, Locators.LOGIN_LINK).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        order_button = driver.find_element(By.XPATH, Locators.ORDER_BUTTON).text
        assert order_button == 'Оформить заказ'

    def test_login_through_forgot_password_link(self, driver):  # через кнопку в форме восстановления пароля
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(By.XPATH, Locators.LOGIN_LINK).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        order_button = driver.find_element(By.XPATH, Locators.ORDER_BUTTON).text
        assert order_button == 'Оформить заказ'