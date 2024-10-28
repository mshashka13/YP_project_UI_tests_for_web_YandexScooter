from selenium.webdriver.common.by import By


class LogoLocators:
    # Логотипы
    LOGO_YANDEX = By.XPATH, ".//*[@class='Header_LogoYandex__3TSOI']"  # логотип Яндекс
    LOGO_SCOOTER = By.XPATH, ".//*[@class='Header_LogoScooter__3lsAR']"  # логотип Самокат

    # Кнопки
    BUTTON_SEARCH_YANDEX_DZEN = By.XPATH, ".//button[contains(text(), 'Найти')]"  # кнопка "Найти" на странице Я.Дзен
