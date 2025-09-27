from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time, random

URL = "https://qa-desk.stand.praktikum-services.ru/"

def test_reg_existing_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 20)


    # 1. Нажать «Вход и регистрация»
    driver.find_element(*Locators.LOGIN_BTN).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))

    # 2. Нажать «Нет аккаунта»
    driver.find_element(*Locators.NO_ACCOUNT_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    # 3. Заполнить форму существующими данными
    existing_email = "testuser@example.com"
    existing_password = "Qwerty123!"
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*Locators.PASSWORD_REPEAT_INPUT).send_keys(existing_password)

    # 4. Нажать «Создать аккаунт»
    driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))

    # 5. Проверки: под Email есть «Ошибка», все поля подсвечены красным
    assert driver.find_element(*Locators.ERROR_TEXT).is_displayed()
    assert driver.find_element(*Locators.EMAIL_ERROR).is_displayed()
    assert driver.find_element(*Locators.PASSWORD_ERROR).is_displayed()
    assert driver.find_element(*Locators.PASSWORD_REPEAT_ERROR).is_displayed()

    driver.quit()
