from conftest import *
from locators import Locators
import time

class TestLogout:

    def test_logout(self, driver, login_data):  # по кнопке «Выйти» в личном кабинете
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys(login_data['email'])
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(login_data['password'])
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).click()
        login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).text
        assert login_button == 'Войти'