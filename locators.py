from selenium.webdriver.common.by import By


class Locators:
    # Авторизация / регистрация
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    PASSWORD_REPEAT_INPUT = (By.XPATH, "//input[@name='submitPassword']")
    SUBMIT_LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Войти')]")
    NO_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
    LOGOUT_BTN = (By.XPATH, "//button[@class='spanGlobal btnSmall' and normalize-space()='Выйти']")
    
    # Профиль / аватар
    AVATAR_ICON = (By.XPATH, "//button[@class='circleSmall']//*[name()='svg']")
    AVATAR_BTN = (By.XPATH, "//button[@class='circleSmall']")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")

    # Меню профиля
    PROFILE_MY_ADS_BTN = (By.XPATH, "//a[contains(text(),'Мои объявления')] | //button[contains(text(),'Мои объявления')]")

    # Размещение объявления
    CREATE_AD_BTN = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
    NEW_AD_HEADER = (By.XPATH, "//h1[contains(text(),'Новое объявление')]")
    AD_TITLE_INPUT = (By.XPATH, '//input[@name="name"]')
    AD_DESC_INPUT = (By.XPATH, '//textarea[@name="description"]')
    AD_PRICE_INPUT = (By.CSS_SELECTOR, 'input[name="price"]')
    AUTH_MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class,'popUp_XBtn')]")
    
    # Выпадающие списки (категория/город)
    DROPDOWN_ARROW = (By.XPATH, "//div[contains(@class, 'dropDownMenu_input')]//button[contains(@class,'dropDownMenu_arrowDown')]")
    DROPDOWN_OPTION_FIRST = (By.XPATH, "//div[contains(@class, 'dropDownMenu_options')]//button[1]")
    DROPDOWN_OPTION_SECOND = (By.XPATH, "//div[contains(@class, 'dropDownMenu_options')]//button[2]")

    # Радиобаттон состояния товара
    CONDITION_RADIO = (By.CSS_SELECTOR, "div[class*='inputRegular__']")

    # Публикация
    PUBLISH_BTN = (By.XPATH, '//button[text()="Опубликовать"]')

    # Мои объявления
    MY_ADS_HEADER = (By.XPATH, "//h1[@class='h1' and text()='Мои объявления']")
    MY_AD_CARD = (By.CSS_SELECTOR, "div[class*='grid_threeColumns'] .card")
    
    # Пункт «Мои объявления» в меню профиля (и как <a>, и как <button>)
    PROFILE_MY_ADS_BTN = (By.XPATH, "//a[normalize-space()='Мои объявления'] | //button[normalize-space()='Мои объявления']")

    # Любая карточка объявления в сетке «Мои объявления»
    MY_AD_CARD = (By.CSS_SELECTOR, "div[class*='grid_threeColumns'] .card")
    
    
    # Ошибки / валидация
    AUTH_REQUIRED_MODAL = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    ERROR_TEXT = (By.XPATH, "//span[contains(text(),'Ошибка')]")
    EMAIL_ERROR = (By.XPATH, "//input[@name='email']/ancestor::div[contains(@class,'Error')]")
    PASSWORD_ERROR = (By.XPATH, "//input[@placeholder='Пароль']/ancestor::div[contains(@class,'Error')]")
    PASSWORD_REPEAT_ERROR = (By.XPATH, "//input[@name='submitPassword']/ancestor::div[contains(@class,'Error')]")

    # Главная
    HOME_SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='name'],[accept='text']")