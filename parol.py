import random
import string

# Переменная с возможными символами для пароля
symbols = string.ascii_letters + string.digits + "+-/*!&$#?=@"

# Запрос длины пароля у пользователя
password_length = int(input("Введите длину пароля: "))

# Переменная для хранения сгенерированного пароля
generated_password = ""

# Генерация пароля
for _ in range(password_length):
    generated_password += random.choice(symbols)

# Вывод сгенерированного пароля
print("Сгенерированный пароль:", generated_password)
