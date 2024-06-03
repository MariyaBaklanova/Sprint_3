class Locators:

    AUTHORIZATION_BUTTON = "//*[text()='Войти в аккаунт']"  # кнопка Войти в аккаунт
    LOGIN_H2 = ".//h2[text()='Вход']"  # заголовок Вход на странице /login
    REGISTER_LINK = ".//a[text()='Зарегистрироваться']"  # ссылка Зарегистрироваться на странице /login
    NAME_FIELD = 'name'  # поле ввода Имя на странице /registration
    EMAIL_FIELD = ".//label[text()='Email']//following-sibling::*"  # поле ввода Email на страницах /registration и /login
    PASSWORD_FIELD = ".//input[@name='Пароль']"  # поле ввода Пароль на страницах /registration и /login
    REGISTER_BUTTON = ".//button[text()='Зарегистрироваться']"  # кнопка Зарегистрироваться на странице /registration
    INCORRECT_PASSWORD_MESSAGE = ".//p[text()='Некорректный пароль']"  # уведомление Некорректный пароль на странице /registration
    LOGIN_LINK = ".//a[text()='Войти']"  # ссылка Войти на странице /registration
    LOGIN_BUTTON = ".//button[text()='Войти']"   # кнопка Войти на странице /login
    FORGOT_PASSWORD_LINK = ".//a[text()='Восстановить пароль']"  # ссылка Восстановить пароль на странице /login
    PROFILE_BUTTON = ".//p[text()='Личный Кабинет']"  # кнопка Личный кабинет
    SAVE_BUTTON = ".//button[text()='Сохранить']"  # кнопка Сохранить на странице /account
    LOGOUT_BUTTON = ".//button[text()='Выход']"  # кнопка Выход на странице /account
    CONSTRUCTOR_BUTTON = ".//p[text()='Конструктор']"  # кнопка Конструктор
    LOGO = ".//div[@class='AppHeader_header__logo__2D0X2']"  # логотип
    CONSTRUCTOR_H1 = ".//h1[text()='Соберите бургер']"   # заголовок Соберите бургер
    BUNS_SECTION = ".//span[text()='Булки']/parent::div"  # раздел Булки
    NO_SELECT_BUNS_SECTION = ".//div[contains(@class, 'noselect') and not (contains(@class, 'current'))]/child::span[text()='Булки']" # невыбранный раздел Булки
    SELECT_BUNS_SECTION = ".//div[contains(@class, 'current')]/child::span[text()='Булки']"  # выбранный раздел Булки
    SAUCES_SECTION = ".//span[text()='Соусы']/parent::div"  # раздел Соусы
    SELECT_SAUCES_SECTION = ".//div[contains(@class, 'current')]/child::span[text()='Соусы']"  # выбранный раздел Соусы
    TOPPINGS_SECTION = ".//span[text()='Начинки']/parent::div"  # раздел Начинки
    SELECT_TOPPINGS_SECTION = ".//div[contains(@class, 'current')]/child::span[text()='Начинки']"  # выбранный раздел Начинки
    ORDER_BUTTON = ".//button[text()='Оформить заказ']"  # кнопка Оформить заказ