## __Тестирование UI Яндекс Самокат__ 
[Яндекс Самокат](https://qa-scooter.praktikum-services.ru "Перейти на сайт")

___

### __Тесты (tests):__  
__*test_home_page - Тесты на соответствие текста в вопросах и ответах:*__
- test_check_questions_and_answers_text - Проверка соответствия текста в вопросах и ответах

__*test_order_page - Тесты на оформление заказа:*__
- test_check_button_to_order_top - Проверка перехода на форму заказа через кнопку "Заказать" в верху страницы
- test_check_button_to_order_center - Проверка перехода на форму заказа через кнопку "Заказать" в центре страницы
- test_order_with_different_user_data - Проверка оформления заказа с разными данными пользователя

__*test_logo - Тесты на переход при клике по логотипам:*__
- test_check_logo_yandex_open_new_window_dzen - Проверка появления нового окна "ЯндексДзен" при клике на логотип "Яндекс
- test_check_logo_scooter_change_url_home_page - Проверка перехода на домашнюю страницу "ЯндексСамокат" при клике на логотип "Самокат"


### __Страницы для шагов тестов:__
__*base_page - Базовые методы:*__
- find_element_webdriverwait - Найти элемент
- click_element - Кликнуть элемент
- add_text_to_element - Ввести текст в элементе
- get_text_from_element - Получить текст элемента
- format_to_locator - Форматирование локатора
- scroll_to_element - Скроллить до элемента

__*home_page - Вопросы о важном, главная страница:*__
- check_question_text - Получить текст вопросов
- check_answer_text - Получить текст ответов

__*order_page - Оформление заказа:*__
- check_button_to_order_top - Перейти на форму заказа через кнопку "Заказать" в верху страницы
- check_button_to_order_center - Перейти на форму заказа через кнопку "Заказать" в центре страницы
- add_user_data_to_form_order - Заполнить форму заказа 
- check_window_successful_order - Завершить заказ, получить поп-ап об успешном оформлении заказа

__*logo - Взаимодействие с логотипами:*__
- check_logo_yandex_open_new_window_dzen - Клик по логотипу "Яндекс" для появления нового окна "ЯндексДзен"
- check_logo_scooter_change_url_home_page - Клик по логотипу "Самокат" для перехода на домашнюю страницу  


### __Вспомогательные элементы:__
1. home_page_locators - Локаторы: вопросы о важном
2. order_page_locators - Локаторы: кнопки "Заказать", форма заказа, поп-апы подтверждения и завершения заказа
3. logo_locators - Локаторы: логотипы, кнопки
4. data - Константы: Url, вопросы, ответы, данные пользователя набор 1, данные пользователя набор 2
5. conftest - Фикстуры: драйвер Firefox
6. requirements - Файл с внешними зависимостями


