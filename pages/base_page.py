from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#Базовые методы
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    #Найти элемент
    def find_element_webdriverwait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    #Кликнуть элемент
    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    #Ввести текст в элементе
    def add_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    #Получить текст элемента
    def get_text_from_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    #Форматирование локатора
    def format_to_locator(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    #Скроллить до элемента
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
