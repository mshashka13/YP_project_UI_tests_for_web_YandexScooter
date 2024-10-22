from selenium.webdriver.support import expected_conditions as EC
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
import allure


#Взаимодействие с логотипами
class Logo(BasePage):
    @allure.step('Клик по логотипу "Яндекс" для появления нового окна "ЯндексДзен"')
    def check_logo_yandex_open_new_window_dzen(self):
        original_handles = self.driver.window_handles
        self.click_element(LogoLocators.LOGO_YANDEX)
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_handle = [h for h in self.driver.window_handles if h != original_handles[0]][0]
        self.driver.switch_to.window(new_handle)
        return self.find_element_webdriverwait(LogoLocators.BUTTON_SEARCH_YANDEX_DZEN)

    @allure.step('Клик по логотипу "Самокат" для перехода на домашнюю страницу')
    def check_logo_scooter_change_url_home_page(self):
        original_url = self.driver.current_url
        self.click_element(LogoLocators.LOGO_SCOOTER)
        WebDriverWait(self.driver, 10).until(EC.url_changes(original_url))
        return self.driver.current_url
