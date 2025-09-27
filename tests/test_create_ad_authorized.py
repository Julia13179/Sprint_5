from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import time, random

URL = "https://qa-desk.stand.praktikum-services.ru/"

def test_create_ad_authorized():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    wait = WebDriverWait(driver, 20)

    existing_email = "zy@gmail.com"
    existing_password = "290886"

    # 1. «Вход и регистрация»
    driver.find_element(*Locators.LOGIN_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    # 2. Ввести email
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(existing_email)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))

    # 3. Ввести пароль
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(existing_password)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SUBMIT_LOGIN_BTN))

    # 4. Нажать «Войти»
    driver.find_element(*Locators.SUBMIT_LOGIN_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AVATAR_ICON))

    # 5. Проверка: имя User
    name = driver.find_element(*Locators.USER_NAME).text
    assert "User" in name

    # 6. Нажать «Разместить объявление»
    driver.find_element(*Locators.CREATE_AD_BTN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.NEW_AD_HEADER))

    # 7. Заполнить форму
    created_title = "Эксклюзив32"
    driver.find_element(*Locators.AD_TITLE_INPUT).send_keys(created_title)
    driver.find_element(*Locators.AD_DESC_INPUT).send_keys("Самый лучший23")
    driver.find_element(*Locators.AD_PRICE_INPUT).send_keys("125")

    # 8. Выбрать категорию
    driver.find_element(*Locators.DROPDOWN_ARROW).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.DROPDOWN_OPTION_FIRST))
    driver.find_element(*Locators.DROPDOWN_OPTION_FIRST).click()

    # 9. Выбрать город
    driver.find_element(*Locators.DROPDOWN_ARROW).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.DROPDOWN_OPTION_SECOND))
    driver.find_element(*Locators.DROPDOWN_OPTION_SECOND).click()

    # 10. Выбрать состояние товара
    driver.find_element(*Locators.CONDITION_RADIO).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PUBLISH_BTN))

    # 11. Нажать «Опубликовать»
    driver.find_element(*Locators.PUBLISH_BTN).click()
    time.sleep(1)

    # 12. Кликнуть по аватару
    driver.find_element(*Locators.AVATAR_BTN).click()
    # ждём, что открылась страница профиля с блоком «Мои объявления»
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MY_ADS_HEADER))

    # 13. Проскроллить к заголовку «Мои объявления»
    element = driver.find_element(*Locators.MY_ADS_HEADER)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # 14. Проверка: в списке есть карточка объявления
    ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.MY_AD_CARD))
    assert ad.is_displayed()