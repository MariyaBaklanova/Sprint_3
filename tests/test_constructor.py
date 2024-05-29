from conftest import *
from locators import Locators


class TestConstructor:

    def test_buns_section(self, driver):  # переход к разделу «Булки»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_SECTION).click()
        driver.find_element(By.XPATH, Locators.NO_SELECT_BUNS_SECTION)
        driver.find_element(By.XPATH, Locators.BUNS_SECTION).click()
        driver.find_element(By.XPATH, Locators.SELECT_BUNS_SECTION)
        #assert select_buns_section == 'Булки'

    def test_sauces_section(self, driver):  # переход к разделу «Соусы»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_SECTION).click()
        driver.find_element(By.XPATH, Locators.SELECT_SAUCES_SECTION)
        #assert select_sauces_section == 'Соусы'

    def test_toppings_section(self, driver):  # переход к разделу «Начинки»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys('marybaklanova006@ya.ru')
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys('123yaya')
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.TOPPINGS_SECTION).click()
        driver.find_element(By.XPATH, Locators.SELECT_TOPPINGS_SECTION)
        #assert select_toppings_section == 'Начинки'