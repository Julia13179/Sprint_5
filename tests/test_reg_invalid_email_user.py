from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

URL = "https://qa-desk.stand.praktikum-services.ru/"


def test_reg_invalid_email_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 20)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators  
URL = "https://qa-desk.stand.praktikum-services.ru/"

def test_reg_invalid_email_user():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    # 1. Клик по «Вход и регистрация» → ждём «Нет аккаунта»
    driver.find_element(*Locators.LOGIN_BTN).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))

    # 2. Клик по «Нет аккаунта» → ждём поле email
    driver.find_element(*Locators.NO_ACCOUNT_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    # 3. Ввести неверный email и пароли
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("not-an-email")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("Qwerty123!")
    driver.find_element(*Locators.PASSWORD_REPEAT_INPUT).send_keys("Qwerty123!")

    # 4. Клик по «Создать аккаунт» → ждём «Ошибка»
    driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))

    # 5. Проверки
    assert driver.find_element(*Locators.ERROR_TEXT).is_displayed()
    assert driver.find_element(*Locators.EMAIL_ERROR).is_displayed()
    assert driver.find_element(*Locators.PASSWORD_ERROR).is_displayed()
    assert driver.find_element(*Locators.PASSWORD_REPEAT_ERROR).is_displayed()

    driver.quit()