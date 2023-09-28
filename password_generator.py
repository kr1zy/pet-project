
import random
import string

# Функция для генерации пароля
def generate_password(length, use_digits, use_uppercase, use_lowercase, use_punctuation):
    characters = ""
    
    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_punctuation:
        characters += "!#$%&*+-=?@^_"
    
    if not characters:
        print("Выберите хотя бы одну опцию для генерации пароля.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Запрос параметров у пользователя
pwd_length = int(input('Введите длину пароля: '))
pwd_digits = input('Включать буквы? (yes = +, no = -): ')
pwd_uppercase = input('Включать заглавные буквы? (yes = +, no = -): ')
pwd_lowercase = input('Включать строчные буквы (yes = +, no = -): ')
pwd_punctuation = input('Включать символы "!#$%&*+-=?@^_"? (yes = +, no = -): ')

# Генерация пароля
password = generate_password(pwd_length, pwd_digits, pwd_uppercase, pwd_lowercase, pwd_punctuation)

if password:
    print(f"Сгенерированный пароль: {password}")