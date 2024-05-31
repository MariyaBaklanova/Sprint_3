from conftest import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestAccount:

    def test_account_before_login(self, driver):  # по клику на «Личный кабинет» до авторизации
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        login_h2 = driver.find_element(By.XPATH, Locators.LOGIN_H2).text
        assert login_h2 == 'Вход'

    def test_account_after_login(self, driver):  # по клику на «Личный кабинет» после авторизации
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        #time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.PROFILE_BUTTON))).click()
        #driver.find_element(By.XPATH, Locators.PROFILE_BUTTON).click()
        save_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.SAVE_BUTTON))).text
        assert save_button == 'Сохранить'