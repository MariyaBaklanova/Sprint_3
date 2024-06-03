from conftest import *
from locators import Locators




class TestConstructor:

    #Проверка, что работают переходы к разделам
    def test_buns_section(self, driver, login_data):  # переход к разделу «Булки»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys(login_data['email'])
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(login_data['password'])
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_SECTION).click()
        driver.find_element(By.XPATH, Locators.BUNS_SECTION).click()
        assert 'tab_tab_type_current' in driver.find_element(By.XPATH, Locators.BUNS_SECTION).get_attribute('class')


    def test_sauces_section(self, driver, login_data):  # переход к разделу «Соусы»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys(login_data['email'])
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(login_data['password'])
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.SAUCES_SECTION).click()
        assert 'tab_tab_type_current' in driver.find_element(By.XPATH, Locators.SAUCES_SECTION).get_attribute(
            'class')



    def test_toppings_section(self, driver, login_data):  # переход к разделу «Начинки»
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.AUTHORIZATION_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_FIELD).send_keys(login_data['email'])
        driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(login_data['password'])
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, Locators.TOPPINGS_SECTION).click()
        assert 'tab_tab_type_current' in driver.find_element(By.XPATH, Locators.TOPPINGS_SECTION).get_attribute(
            'class')

