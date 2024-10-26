# qa_python_sprint_6

#Тесты
test_home_page - Тесты на соответствие текста в вопросах и ответах:
1) test_check_questions_and_answers_text - Проверка соответствия текста в вопросах и ответах

test_order_page - Тесты на оформление заказа:
1) test_check_button_to_order_top - Проверка перехода на форму заказа через кнопку "Заказать" в верху страницы
2) test_check_button_to_order_center - Проверка перехода на форму заказа через кнопку "Заказать" в центре страницы
3) test_order_with_different_user_data - Проверка оформления заказа с разными данными пользователя

test_logo - Тесты на переход при клике по логотипам:
1) test_check_logo_yandex_open_new_window_dzen - Проверка появления нового окна "ЯндексДзен" при клике на логотип "Яндекс
2) test_check_logo_scooter_change_url_home_page - Проверка перехода на домашнюю страницу "ЯндексСамокат" при клике на логотип "Самокат"


#Страницы для шагов тестов
base_page - Базовые методы:
1) find_element_webdriverwait - Найти элемент
2) click_element - Кликнуть элемент
3) add_text_to_element - Ввести текст в элементе
4) get_text_from_element - Получить текст элемента
5) format_to_locator - Форматирование локатора
6) scroll_to_element - Скроллить до элемента

home_page - Вопросы о важном, главная страница:
1) check_question_text - Получить текст вопросов
2) check_answer_text - Получить текст ответов

order_page - Оформление заказа:
1) check_button_to_order_top - Перейти на форму заказа через кнопку "Заказать" в верху страницы
2) check_button_to_order_center - Перейти на форму заказа через кнопку "Заказать" в центре страницы
3) add_user_data_to_form_order - Заполнить форму заказа 
4) check_window_successful_order - Завершить заказ, получить поп-ап об успешном оформлении заказа

logo - Взаимодействие с логотипами:
1) check_logo_yandex_open_new_window_dzen - Клик по логотипу "Яндекс" для появления нового окна "ЯндексДзен"
2) check_logo_scooter_change_url_home_page - Клик по логотипу "Самокат" для перехода на домашнюю страницу


#Вспомогательные элементы
home_page_locators - Локаторы: вопросы о важном
order_page_locators - Локаторы: кнопки "Заказать", форма заказа, поп-апы подтверждения и завершения заказа
logo_locators - Локаторы: логотипы, кнопки
data - Константы: Url, вопросы, ответы, данные пользователя набор 1, данные пользователя набор 2
conftest - Фикстуры: драйвер Firefox
requirements - Файл с внешними зависимостями


