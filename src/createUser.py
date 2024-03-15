import re
import bcrypt
from db_connection import DBConnection

class SignUp:
    def __init__(self):
        self.db_connection = DBConnection.getInstance()

    def register_user(self, email, password):
        try:
            # Проверка валидности email
            if not email.endswith("@meteor.ru"):
                raise ValueError("Email должен заканчиваться на '@meteor.ru'")

            # Проверка валидности пароля
            if not self.is_password_valid(password):
                raise ValueError(
                    "Пароль должен иметь длину не менее 8 символов и включать заглавные буквы, цифры и специальные символы.")

            # Проверка доступности email
            if not self.is_email_available(email):
                raise ValueError("Аккаунт уже существует")

            # Хеширование пароля
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Вставка хешированного пароля в базу данных
            sql_query = f"INSERT INTO Profile ([e-mail], [password]) VALUES ('{email}', '{hashed_password.decode('utf-8')}')"
            self.db_connection.save_to_db(sql_query)

            # Создание профиля пользователя
            return "Success", {"email": email, "password": hashed_password.decode('utf-8')}
        except Exception as ex:
            return ex.args[0], None

    def is_email_available(self, email):
        query = f"SELECT COUNT(*) FROM Profile WHERE [e-mail] = '{email}'"
        count = self.db_connection.execute_scalar(query)
        return count == 0

    def is_password_valid(self, password):
        return bool(re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-zA-Z\d]).{8,25}$', password))