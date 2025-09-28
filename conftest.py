import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    service = Service()
    drv = webdriver.Chrome(service=service)
    drv.maximize_window()
    yield drv
    drv.quit()

@pytest.fixture
def url():
    return "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)
