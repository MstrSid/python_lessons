import re

password = input("Введите пароль (не менее 8 символов):\n")

p = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
pattern = re.compile(p)
while re.match(pattern, password) is None:
    print("Не соблюдены условия")
    password = input("Введите пароль (не менее 8 символов)\n")
print(f"Пароль {password} принят.")