import pytest
from pages.base_page import BasePage
from locators.order_page_locators import OrderButtonLocators, OrderFormPart1Locators, OrderFormPart2Locators, OrderPopUpLocators
from data import UserData
import allure


# Оформление заказа
class OrderPage(BasePage):

    @allure.step('Перейти на форму заказа через кнопку "Заказать" в верху страницы')
    def check_button_to_order_top(self):
        self.click_element(OrderButtonLocators.BUTTON_TO_ORDER_TOP)
        return self.find_element_webdriverwait(OrderFormPart1Locators.FIELD_NAME)

    @allure.step('Перейти на форму заказа через кнопку "Заказать" в центре страницы')
    def check_button_to_order_center(self):
        self.scroll_to_element(OrderButtonLocators.BUTTON_TO_ORDER_CENTER)
        self.click_element(OrderButtonLocators.BUTTON_TO_ORDER_CENTER)
        return self.find_element_webdriverwait(OrderFormPart1Locators.FIELD_NAME)

    @allure.step('Заполнить форму заказа')
    @pytest.mark.parametrize(
        "name, last_name, address, metro, phone, calendar_date, rental_day, comment_for_courier",
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
    def add_user_data_to_form_order(self, name, last_name, address, metro, phone, calendar_date, rental_day,
                                    comment_for_courier):
        self.add_text_to_element(OrderFormPart1Locators.FIELD_NAME, name)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_LAST_NAME, last_name)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_ADDRESS, address)
        self.click_element(OrderFormPart1Locators.FIELD_METRO)
        self.click_element(metro)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_PHONE, phone)
        self.click_element(OrderFormPart1Locators.BUTTON_NEXT)
        self.click_element(OrderFormPart2Locators.FIELD_DATA_ORDER)
        self.click_element(calendar_date)
        self.click_element(OrderFormPart2Locators.FIELD_RENTAL_PERIOD)
        self.click_element(rental_day)
        self.click_element(OrderFormPart2Locators.CHECKBOX_BLACK_COLOR)
        self.add_text_to_element(OrderFormPart2Locators.FIELD_COMMENT_FOR_COURIER, comment_for_courier)
        self.click_element(OrderFormPart2Locators.BUTTON_TO_ORDER_IN_FORM)
        return self.find_element_webdriverwait(OrderPopUpLocators.BUTTON_YES_ORDER)

    @allure.step('Завершить заказ, получить поп-ап об успешном оформлении заказа')
    def check_window_successful_order(self):
        self.click_element(OrderPopUpLocators.BUTTON_YES_ORDER)
        return self.get_text_from_element(OrderPopUpLocators.POP_UP_WINDOW_SUCCESSFUL_ORDER)
