from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time, random

URL = "https://qa-desk.stand.praktikum-services.ru/"

def test_reg_new_user():
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

    # 3. Сгенерировать уникальный email
    email = f"autotest{int(time.time())}{random.randint(100,999)}@example.com"
    password = "Qwerty123!"

    # 4. Заполнить поля формы
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.PASSWORD_REPEAT_INPUT).send_keys(password)

    # 5. Нажать «Создать аккаунт»
    driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HOME_SEARCH_INPUT))

    # 6. Проверка: на главной есть поле поиска
    assert driver.find_element(*Locators.HOME_SEARCH_INPUT).is_displayed()

    # 7. Проверка: есть аватар и имя "User"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AVATAR_ICON))
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.USER_NAME))
    name = driver.find_element(*Locators.USER_NAME).text
    assert "User" in name

    driver.quit()