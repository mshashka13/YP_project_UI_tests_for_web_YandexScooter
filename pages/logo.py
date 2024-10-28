from selenium.webdriver.support import expected_conditions as EC
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time


# Взаимодействие с логотипами
class Logo(BasePage):

    @allure.step('Клик по логотипу "Яндекс" для появления нового окна "ЯндексДзен"')
    def check_logo_yandex_open_new_window_dzen(self):
        original_window = self.driver.current_window_handle
        self.click_element(LogoLocators.LOGO_YANDEX)
        time.sleep(2)
        all_windows = self.driver.window_handles
        assert len(all_windows) > 1
        for window in all_windows:
            if window != original_window:
                self.driver.switch_to.window(window)
        return self.driver.current_url

    @allure.step('Клик по логотипу "Самокат" для перехода на домашнюю страницу')
    def check_logo_scooter_change_url_home_page(self):
        original_url = self.driver.current_url
        self.click_element(LogoLocators.LOGO_SCOOTER)
        WebDriverWait(self.driver, self.time).until(EC.url_changes(original_url))
        return self.driver.current_url
