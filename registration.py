class Database:                                                                            # Создаем класс базы данных
    def __init__(self):                                                                    # Добавляем конструктор, который создает пустой словарь для хранения данных
        self.data = {}                                                                     # Создаем словарь для хранения данных

    def add_user(self, username, password):                                                # Добавляем метод для добавления пользователя в базу данных
        self.data[username] = password                                                     # Добавляем пользователя и пароль в словарь


class User:  # Создаем класс пользователя
    """
    Класс пользователя, содержащий имя пользователя, пароль и подтверждение пароля.
    """
    def __init__(self, username, password, password_confirm):                              # Добавляем конструктор, который принимает имя пользователя, пароль и подтверждение пароля.
        self.username = username                                                           # Добавляем имя пользователя
        self.password = password                                                           # Добавляем пароль
        self.password_confirm = password_confirm                                           # Добавляем подтверждение пароля

    def valid_password(self, password, password_confirm):                                  # Метод для проверки валидности пароля
        if password != password_confirm:                                                   # Проверяем, что пароли совпадают
            return False, 'Пароли не совпадают'                                            # Если пароли не совпадают, выводим сообщение об ошибке

        if len(password) < 8:                                                              # Проверяем длину пароля
            return False, 'Пароль должен содержать не меньше 8 символов'

        upper_case = any(char.isupper() for char in password)                              # Проверяем, есть ли в пароле заглавные буквы
        if not upper_case:
            return False, 'Пароль должен содержать хотя бы одну заглавную букву'

        lower_case = any(char.islower() for char in password)                              # Проверяем, есть ли в пароле строчные буквы
        if not lower_case:
            return False, 'Пароль должен содержать хотя бы одну строчную букву'

        digit = any(char.isdigit() for char in password)                                   # Проверяем, есть ли в пароле цифры
        if not digit:
            return False, 'Пароль должен содержать хотя бы одну цифру'

        else:
            return True, 'Пароль успешно создан'


if __name__ == "__main__":                                                                 # Точка входа в приложение
    database_try = Database()                                                              # Создаем экземпляр базы данных
    while True:                                                                            # Бесконечный цикл для ввода пользователей
        choice = input('Выберите действие:\n1. Создать нового пользователя \n2. Войти\n')  # Выбор действия
        if choice == '2':                                                                  # Если выбрано вход
            login = input('Введите логин: ')                                               # Ввод логина
            password = input('Введите пароль: ')                                           # Ввод пароля
            if login in database_try.data:                                                 # Если пользователь существует в базе данных
                print('Вход успешен!')
        if choice == '1':                                                                  # Если выбрано создание нового пользователя
            username = input('Введите логин: ')
            password1 = input('Введите пароль: ')
            password2 = input('Повторите пароль: ')                                        # Создаем экземпляр пользователя с введенными данными
            user = User(username, password1, password2)
            is_valid, message = user.valid_password(password1, password2)
            if is_valid:
                database_try.add_user(user.username, user.password)
                print(f"Пользователь '{user.username}' успешно зарегистрирован.")
            else:
                print(message)