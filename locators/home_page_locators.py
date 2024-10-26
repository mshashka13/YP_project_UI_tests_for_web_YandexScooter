from selenium.webdriver.common.by import By


class HomePageLocators:
    # Вопросы о важном
    LOCATOR_QUESTION = By.XPATH, ".//*[@id='accordion__heading-{}']"  # вопрос
    LOCATOR_ANSWER = By.XPATH, ".//*[@id='accordion__panel-{}']"  # ответ
    LOCATOR_QUESTION_8 = By.XPATH, ".//*[@id='accordion__heading-7']"  # вопрос № 8
    LOCATOR_ANSWER_8 = By.XPATH, ".//*[@id='accordion__panel-7']"  # ответ № 8
