import selenium
import pytest
from selenium import webdriver
from urls import URLS
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URLS.MAIN_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_data():
    return {'email': 'marybaklanova006@ya.ru', 'password': '123yaya'}




