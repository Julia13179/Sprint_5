from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time, random

URL = "https://qa-desk.stand.praktikum-services.ru/"

def test_create_ad_unauthorized():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 20)

    # 1. Нажать «Разместить объявление»
    driver.find_element(*Locators.CREATE_AD_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTH_REQUIRED_MODAL))

    # 2. Проверить, что появилось модальное «Чтобы разместить объявление, авторизуйтесь»
    assert driver.find_element(*Locators.AUTH_REQUIRED_MODAL).is_displayed()

    driver.quit()