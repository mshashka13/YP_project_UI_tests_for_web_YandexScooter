from pages.base_page import BasePage
from locators.order_page_locators import OrderButtonLocators, OrderFormPart1Locators, OrderFormPart2Locators, OrderPopUpLocators
from data import UserData
import allure

#Оформление заказа
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

    @allure.step('Заполнить 1 часть формы заказа с 1 набором данных пользователя')
    def add_user_data_1_to_form_order_part_1(self):
        self.add_text_to_element(OrderFormPart1Locators.FIELD_NAME, UserData.name_1)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_LAST_NAME, UserData.last_name_1)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_ADDRESS, UserData.address_1)
        self.click_element(OrderFormPart1Locators.FIELD_METRO)
        self.click_element(OrderFormPart1Locators.METRO_CHERKIZOVSKAYA)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_PHONE, UserData.phone_1)
        self.click_element(OrderFormPart1Locators.BUTTON_NEXT)
        return self.find_element_webdriverwait(OrderFormPart2Locators.FIELD_DATA_ORDER)

    @allure.step('Заполнить 2 часть формы заказа с 1 набором данных пользователя')
    def add_user_data_1_to_form_order_part_2(self):
        self.click_element(OrderFormPart2Locators.FIELD_DATA_ORDER)
        self.click_element(OrderFormPart2Locators.CALENDAR_DATA_30)
        self.click_element(OrderFormPart2Locators.FIELD_RENTAL_PERIOD)
        self.click_element(OrderFormPart2Locators.RENT_1_DAY)
        self.click_element(OrderFormPart2Locators.BUTTON_TO_ORDER_IN_FORM)
        return self.find_element_webdriverwait(OrderPopUpLocators.BUTTON_YES_ORDER)

    @allure.step('Заполнить 1 часть формы заказа с 2 набором данных пользователя')
    def add_user_data_2_to_form_order_part_1(self):
        self.add_text_to_element(OrderFormPart1Locators.FIELD_NAME, UserData.name_2)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_LAST_NAME, UserData.last_name_2)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_ADDRESS, UserData.address_2)
        self.click_element(OrderFormPart1Locators.FIELD_METRO)
        self.click_element(OrderFormPart1Locators.METRO_SOKOLNIKI)
        self.add_text_to_element(OrderFormPart1Locators.FIELD_PHONE, UserData.phone_2)
        self.click_element(OrderFormPart1Locators.BUTTON_NEXT)
        return self.find_element_webdriverwait(OrderFormPart2Locators.FIELD_DATA_ORDER)

    @allure.step('Заполнить 2 часть формы заказа с 2 набором данных пользователя')
    def add_user_data_2_to_form_order_part_2(self):
        self.click_element(OrderFormPart2Locators.FIELD_DATA_ORDER)
        self.click_element(OrderFormPart2Locators.CALENDAR_DATA_31)
        self.click_element(OrderFormPart2Locators.FIELD_RENTAL_PERIOD)
        self.click_element(OrderFormPart2Locators.RENT_3_DAYS)
        self.click_element(OrderFormPart2Locators.CHECKBOX_BLACK_COLOR)
        self.add_text_to_element(OrderFormPart2Locators.FIELD_COMMENT_FOR_COURIER, UserData.comment_for_courier)
        self.click_element(OrderFormPart2Locators.BUTTON_TO_ORDER_IN_FORM)
        return self.find_element_webdriverwait(OrderPopUpLocators.BUTTON_YES_ORDER)

    @allure.step('Завершить заказ, получить поп-ап об успешном оформлении заказа')
    def check_window_successful_order(self):
        self.click_element(OrderPopUpLocators.BUTTON_YES_ORDER)
        return self.get_text_from_element(OrderPopUpLocators.POP_UP_WINDOW_SUCCESSFUL_ORDER)
