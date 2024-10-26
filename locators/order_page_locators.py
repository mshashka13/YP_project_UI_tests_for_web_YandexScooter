from selenium.webdriver.common.by import By


class OrderButtonLocators:
    # Кнопки "Заказать"
    BUTTON_TO_ORDER_TOP = By.XPATH, ".//button[@class='Button_Button__ra12g']"  # Кнопка "Заказать" в верху страницы
    BUTTON_TO_ORDER_CENTER = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"  # Кнопка "Заказать" в центре страницы


class OrderFormPart1Locators:
    # Форма заказа, 1 часть
    FIELD_NAME = By.XPATH, ".//input[@placeholder='* Имя']"  # поле Имя
    FIELD_LAST_NAME = By.XPATH, ".//input[@placeholder='* Фамилия']"  # поле Фамилия
    FIELD_ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"  # поле Адрес
    FIELD_METRO = By.XPATH, ".//input[@placeholder='* Станция метро']"  # поле Метро
    METRO_CHERKIZOVSKAYA = By.XPATH, ".//*[contains(text(), 'Черкизовская')]"  # метро Черкизовская
    METRO_SOKOLNIKI = By.XPATH, ".//*[contains(text(), 'Сокольники')]"  # метро Сокольники
    FIELD_PHONE = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"  # поле Телефон
    BUTTON_NEXT = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"  # кнопка Далее


class OrderFormPart2Locators:
    # Форма заказа, 2 часть
    TITLE_ABOUT_RENT = By.XPATH, ".//*[@class='Order_Header__BZXOb']"  # заголовок Про аренду
    FIELD_DATA_ORDER = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"  # поле Когда привезти самокат
    CALENDAR_DATA_30 = By.XPATH, ".//*[@class='react-datepicker__day react-datepicker__day--030']"  # 30 число текущего месяца
    CALENDAR_DATA_31 = By.XPATH, ".//*[@class='react-datepicker__day react-datepicker__day--031']"  # 31 число текущего месяца
    FIELD_RENTAL_PERIOD = By.XPATH, ".//*[@class='Dropdown-placeholder']"  # поле Срок аренды
    RENT_1_DAY = By.XPATH, ".//*[contains(text(), 'сутки')]"  # сутки
    RENT_3_DAYS = By.XPATH, ".//*[contains(text(), 'трое суток')]"  # трое суток
    CHECKBOX_BLACK_COLOR = By.XPATH, ".//*[contains(@id, 'black')]"  # чекбокс Черный жемчуг
    CHECKBOX_GREY_COLOR = By.XPATH, ".//*[contains(@id, 'grey')]"  # чекбокс Серая безысходность
    FIELD_COMMENT_FOR_COURIER = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"  # поле Комментарий для курьера
    BUTTON_TO_ORDER_IN_FORM = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"  # кнопка Заказать в конце формы


class OrderPopUpLocators:
    # Поп-ап: потверждение заказа
    BUTTON_YES_ORDER = By.XPATH, ".//*[contains(text(), 'Да')]"  # кнопка потверждения заказа

    # Поп-ап: успешное оформление заказа
    POP_UP_WINDOW_SUCCESSFUL_ORDER = By.XPATH, ".//*[contains(text(), 'Заказ оформлен')]"  # Поп-ап Заказ оформлен
    BUTTON_VIEW_STATUS = By.XPATH, ".//*[contains(text(), 'Посмотреть статус')]"  # кнопка Посмотреть статус
