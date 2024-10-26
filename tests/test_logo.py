from pages.logo import Logo
from data import Url
import time
import allure


@allure.title('Тесты на переход при клике по логотипам')
class TestLogo:

    @allure.title('Проверка перехода на ЯндексДзен при клике на логотип "Яндекс"')
    @allure.description(
        'Находим на домашней странице логотип "Яндекс" и проверяем, что при клике на него происходит переход на новый URL ЯндексДзен')
    def test_check_logo_yandex_open_new_window_dzen(self, driver):
        driver.get(Url.URL_HOME)
        logo = Logo(driver)
        original_window = driver.current_window_handle
        logo.check_logo_yandex_open_new_window_dzen()
        time.sleep(2)
        all_windows = driver.window_handles
        assert len(all_windows) > 1
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)
        current_url = driver.current_url
        assert Url.URL_YANDEX_DZEN in current_url

    @allure.title('Проверка перехода на домашнюю страницу "ЯндексСамокат" при клике на логотип "Самокат"')
    @allure.description(
        'Находим на странице формы заказа логотип "Самокат" и проверяем, что при клике на него происходит переход на домашнюю страницу "ЯндексСамокат"')
    def test_check_logo_scooter_change_url_home_page(self, driver):
        driver.get(Url.URL_FORM_ORDER)
        logo = Logo(driver)
        new_url = logo.check_logo_scooter_change_url_home_page()
        assert new_url == Url.URL_HOME
