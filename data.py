import random


class Url:
    # URL Яндекс Самокат
    URL_HOME = 'https://qa-scooter.praktikum-services.ru/'
    URL_FORM_ORDER = 'https://qa-scooter.praktikum-services.ru/order/'
    URL_YANDEX_DZEN = 'https://dzen.ru/'


class Questions:
    # Вопросы о важном: вопросы
    QUESTION_1 = 'Сколько это стоит? И как оплатить?'
    QUESTION_2 = 'Хочу сразу несколько самокатов! Так можно?'
    QUESTION_3 = 'Как рассчитывается время аренды?'
    QUESTION_4 = 'Можно ли заказать самокат прямо на сегодня?'
    QUESTION_5 = 'Можно ли продлить заказ или вернуть самокат раньше?'
    QUESTION_6 = 'Вы привозите зарядку вместе с самокатом?'
    QUESTION_7 = 'Можно ли отменить заказ?'
    QUESTION_8 = 'Я жизу за МКАДом, привезёте?'


class Answers:
    # Вопросы о важном: ответы
    ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_2 = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто '
                'сделать несколько заказов — один за другим.')
    ANSWER_3 = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени '
                'аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
                '20:30, суточная аренда закончится 9 мая в 20:30.')
    ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_6 = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься '
                'без передышек и во сне. Зарядка не понадобится.')
    ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


class UserData:
    # 1 вариант - Данные пользователя для создания заказа
    name_1 = 'Мария'
    last_name_1 = 'Шаша'
    address_1 = 'Байконурская, 14'
    metro_1 = 'Черкизовская'
    phone_1 = f'8{random.randint(1000000000, 9999999999)}'
    comment_for_courier_empty = f''

    # 2 вариант - Данные пользователя для создания заказа
    name_2 = 'са'
    last_name_2 = 'ша'
    address_2 = 'наб. канала Грибоедова, 17'
    metro_2 = 'Сокольники'
    phone_2 = f'7{random.randint(1000000000, 9999999999)}'
    comment_for_courier_1 = 'позвонить заранее'
