from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time, random

URL = "https://qa-desk.stand.praktikum-services.ru/"

def test_login_existing_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 20)

    # 1. Нажать «Вход и регистрация»
    driver.find_element(*Locators.LOGIN_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    # 2. Ввести email
    existing_email = "zy@gmail.com"
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(existing_email)

    # 3. Ввести пароль
    existing_password = "290886"
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(existing_password)

    # 4. Нажать «Войти»
    driver.find_element(*Locators.SUBMIT_LOGIN_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HOME_SEARCH_INPUT))

    # 5. Проверка: поле поиска отображается
    assert driver.find_element(*Locators.HOME_SEARCH_INPUT).is_displayed()

    # 6. Проверка: отображается аватар и имя "User"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AVATAR_ICON))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.USER_NAME))
    name = driver.find_element(*Locators.USER_NAME).text
    assert "User" in name

    driver.quit()