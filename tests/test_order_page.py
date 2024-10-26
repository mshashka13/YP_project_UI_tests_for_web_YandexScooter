import pytest
from data import Url, UserData
from pages.order_page import OrderPage
from locators.order_page_locators import OrderFormPart1Locators, OrderFormPart2Locators
import allure


@allure.title('Тесты на оформление заказа')
class TestOrderPage:
    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в верху страницы')
    @allure.description(
        'Проверяем, что при клике на кнопку "Заказать" в верху домашней страницы происходит переход на форму заказа')
    def test_check_button_to_order_top(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_top()
        assert element is not None

    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в центре страницы')
    @allure.description(
        'Проверяем, что при скролле до кнопки "Заказать" в центре домашней страницы и клике на нее происходит переход на форму заказа')
    def test_check_button_to_order_center(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_center()
        assert element is not None

    @allure.title('Проверка оформления заказа с разными данными пользователя')
    @allure.description('Проверяем, что заказ успешно оформляется с разными данными пользователя.')
    @pytest.mark.parametrize(
        "user_data",
        [
            (UserData.name_1, UserData.last_name_1, UserData.address_1, OrderFormPart1Locators.METRO_CHERKIZOVSKAYA,
             UserData.phone_1, OrderFormPart2Locators.CALENDAR_DATA_30, OrderFormPart2Locators.RENT_1_DAY,
             UserData.comment_for_courier_empty),
            (UserData.name_2, UserData.last_name_2, UserData.address_2, OrderFormPart1Locators.METRO_SOKOLNIKI,
             UserData.phone_2, OrderFormPart2Locators.CALENDAR_DATA_31, OrderFormPart2Locators.RENT_3_DAYS,
             UserData.comment_for_courier_1)
        ],
        ids=['Оформление заказа с данными пользователя 1', 'Оформление заказа с данными пользователя 2']
    )
    def test_order_with_different_user_data(self, driver, user_data):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        name, last_name, address, metro, phone, calendar_date, rental_day, comment_for_courier = user_data
        order_page.check_button_to_order_top()
        order_page.add_user_data_to_form_order(name, last_name, address, metro, phone, calendar_date, rental_day,
                                               comment_for_courier)
        text = order_page.check_window_successful_order()
        assert 'Заказ оформлен' in text
