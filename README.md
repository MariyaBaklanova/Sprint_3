Автотесты для сервиса Stellar Burgers -- https://stellarburgers.nomoreparties.site

Сервис Stellar Burgers - это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

test_registration
Регистрация 
   test_registration_success -- успешная регистрация
    поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен:
    например, 123@ya.ru. Минимальный пароль — шесть символов
   test_registration_incorrect_password -- ошибка для некорректного пароля

test_login
Вход
   test_login_through_authorization_button -- по кнопке «Войти в аккаунт» на главной,
   test_login_through_profile_button -- через кнопку «Личный кабинет»,
   test_login_through_login_link -- через кнопку в форме регистрации,
   test_login_through_forgot_password_link -- через кнопку в форме восстановления пароля

test_account
Переход в личный кабинет
   test_account_login_before_authorization -- по клику на «Личный кабинет» до авторизации
   test_account_login_after_authorization -- по клику на «Личный кабинет» после авторизации

test_from_account_to_constructor
Переход из личного кабинета в конструктор
   test_move_by_click_to_constructor -- по клику на «Конструктор»
   test_move_by_click_to_logo_with_registration -- по клику на логотип Stellar Burgers

test_logout
Выход из аккаунта
   test_logout -- по кнопке «Выйти» в личном кабинете

test_constructor
Раздел «Конструктор» 
   test_buns_section -- переход к разделу «Булки»
   test_sauces_section -- переход к разделу «Соусы»
   test_toppings_section -- переход к разделу «Начинки»#   S p r i n t _ 3 
 
 