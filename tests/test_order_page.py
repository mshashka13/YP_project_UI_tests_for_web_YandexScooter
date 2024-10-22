from data import Url
from pages.order_page import OrderPage
import allure

@allure.title('Тесты на оформление заказа')
class TestOrderPage:
    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в верху страницы')
    @allure.description('Проверяем, что при клике на кнопку "Заказать" в верху домашней страницы происходит переход на форму заказа')
    def test_check_button_to_order_top(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_top()
        assert element is not None

    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в центре страницы')
    @allure.description('Проверяем, что при скролле до кнопки "Заказать" в центре домашней страницы и клике на нее происходит переход на форму заказа')
    def test_check_button_to_order_center(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_center()
        assert element is not None

    @allure.title('Проверка заполнения 1 части формы заказа с 1 набором данных пользователя')
    @allure.description('Проверяем, что 1 часть формы заказа заполняется с 1 набором данных пользователя, происходит переход на 2 часть формы заказа')
    def test_add_user_data_1_to_form_order_part_1(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        order_page.check_button_to_order_top()
        element = order_page.add_user_data_1_to_form_order_part_1()
        assert element is not None

    @allure.title('Проверка заполнения 2 части формы заказа с 1 набором данных пользователя')
    @allure.description('Проверяем, что 2 часть формы заказа заполняется с 1 набором данных пользователя, открывается поп-ап для подтверждения заказа')
    def test_add_user_data_1_to_form_order_part_2(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        order_page.check_button_to_order_top()
        order_page.add_user_data_1_to_form_order_part_1()
        element = order_page.add_user_data_1_to_form_order_part_2()
        assert element is not None

    @allure.title('Проверка заполнения 1 части формы заказа с 2 набором данных пользователя')
    @allure.description('Проверяем, что 1 часть формы заказа заполняется с 2 набором данных пользователя, происходит переход на 2 часть формы заказа')
    def test_add_user_data_2_to_form_order_part_1(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        order_page.check_button_to_order_center()
        element = order_page.add_user_data_2_to_form_order_part_1()
        assert element is not None

    @allure.title('Проверка заполнения 2 части формы заказа с 2 набором данных пользователя')
    @allure.description('Проверяем, что 2 часть формы заказа заполняется с 2 набором данных пользователя, открывается поп-ап для подтверждения заказа')
    def test_add_user_data_2_to_form_order_part_2(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        order_page.check_button_to_order_center()
        order_page.add_user_data_2_to_form_order_part_1()
        element = order_page.add_user_data_2_to_form_order_part_2()
        assert element is not None

    @allure.title('Проверка успешного оформления заказа и появление поп-апа')
    @allure.description('Проверяем, что появился поп-ап, обозначающий успешное оформление заказа при заполнении двух частей формы и подтверждения заказа в всплывающем поп-апе')
    def test_check_window_successful_order(self, driver):
        driver.get(Url.URL_HOME)
        order_page = OrderPage(driver)
        order_page.check_button_to_order_top()
        order_page.add_user_data_1_to_form_order_part_1()
        order_page.add_user_data_1_to_form_order_part_2()
        text = order_page.check_window_successful_order()
        assert 'Заказ оформлен' in text

