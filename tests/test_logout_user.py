from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time, random
from data import existing_email, existing_password

class TestLogoutUser:
    def test_logout_user(self, driver, url):
        driver.get(url)
  


    # 1. Нажать «Вход и регистрация»
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    # 2. Ввести email
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(existing_email)

    # 3. Ввести пароль
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(existing_password)

    # 4. Нажать «Войти»
        driver.find_element(*Locators.SUBMIT_LOGIN_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.HOME_SEARCH_INPUT))

    # 5. Проверка: отображается аватар
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AVATAR_BTN))

    # 6. Нажать «Выйти»
        driver.find_element(*Locators.LOGOUT_BTN).click()

    # 7. Проверка: появилась кнопка «Вход и регистрация»
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BTN))
        assert driver.find_element(*Locators.LOGIN_BTN).is_displayed()

        driver.quit()