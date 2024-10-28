from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure


# Вопросы о важном, домашняя страница
class HomePage(BasePage):
    @allure.step('Получить текст вопросов')
    def check_question_text(self, num):
        locator_q_formatted = self.format_to_locator(HomePageLocators.LOCATOR_QUESTION, num)
        self.scroll_to_element(HomePageLocators.LOCATOR_QUESTION_8)
        self.find_element_webdriverwait(locator_q_formatted)
        return self.get_text_from_element(locator_q_formatted)

    @allure.step('Получить текст ответов')
    def check_answer_text(self, num):
        locator_q_formatted = self.format_to_locator(HomePageLocators.LOCATOR_QUESTION, num)
        locator_a_formatted = self.format_to_locator(HomePageLocators.LOCATOR_ANSWER, num)
        self.scroll_to_element(HomePageLocators.LOCATOR_QUESTION_8)
        self.click_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
