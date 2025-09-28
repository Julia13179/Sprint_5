from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import existing_email, existing_password, invalid_email, password_text
import time, random


class TestRegistration:
    def test_reg_new_user(self, driver, url):
        driver.get(url)
    
    
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

    
    
    def test_reg_existing_user(self, driver, url):
        driver.get(url)
    


    # 1. Нажать «Вход и регистрация»
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))

    # 2. Нажать «Нет аккаунта»
        driver.find_element(*Locators.NO_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    # 3. Заполнить форму существующими данными
  
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

        
    def test_reg_invalid_email_user(self, driver, url):
        driver.get(url)
    
    # 1. Клик по «Вход и регистрация» → ждём «Нет аккаунта»
        driver.find_element(*Locators.LOGIN_BTN).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))

    # 2. Клик по «Нет аккаунта» → ждём поле email
        driver.find_element(*Locators.NO_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    # 3. Ввести неверный email и пароли
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(invalid_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password_text)
        driver.find_element(*Locators.PASSWORD_REPEAT_INPUT).send_keys(password_text)

    # 4. Клик по «Создать аккаунт» → ждём «Ошибка»
        driver.find_element(*Locators.CREATE_ACCOUNT_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))

    # 5. Проверки
        assert driver.find_element(*Locators.ERROR_TEXT).is_displayed()
        assert driver.find_element(*Locators.EMAIL_ERROR).is_displayed()
        assert driver.find_element(*Locators.PASSWORD_ERROR).is_displayed()
        assert driver.find_element(*Locators.PASSWORD_REPEAT_ERROR).is_displayed()

        driver.quit()   
        
        
