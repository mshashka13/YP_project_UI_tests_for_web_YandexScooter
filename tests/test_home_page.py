import allure
import pytest
from data import Url, Questions, Answers
from pages.home_page import HomePage


@allure.title('Тесты на соответствие текста в вопросах и ответах')
class TestHomePage:
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, Questions.QUESTION_1),
            (1, Questions.QUESTION_2),
            (2, Questions.QUESTION_3),
            (3, Questions.QUESTION_4),
            (4, Questions.QUESTION_5),
            (5, Questions.QUESTION_6),
            (6, Questions.QUESTION_7),
            (7, Questions.QUESTION_8)
        ]
    )
    @allure.title('Проверка соответствия текста в вопросах')
    @allure.description(
        'Находим на домашней странице раздел "Вопросы о важном" и проверяем, что текст в вопросах соответствует заявленному')
    def test_check_questions_text(self, driver, num, result):
        driver.get(Url.URL_HOME)
        home_page = HomePage(driver)
        assert home_page.check_question_text(num) == result

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, Answers.ANSWER_1),
            (1, Answers.ANSWER_2),
            (2, Answers.ANSWER_3),
            (3, Answers.ANSWER_4),
            (4, Answers.ANSWER_5),
            (5, Answers.ANSWER_6),
            (6, Answers.ANSWER_7),
            (7, Answers.ANSWER_8)
        ]
    )
    @allure.title('Проверка соответствия текста в ответах')
    @allure.description(
        'Находим на домашней странице раздел "Вопросы о важном", кликаем вопросы и проверяем, что текст в их ответах соответствует заявленному')
    def test_check_answers_text(self, driver, num, result):
        driver.get(Url.URL_HOME)
        home_page = HomePage(driver)
        assert home_page.check_answer_text(num) == result
