""""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
def person_data(**data):
    for key, value in data.items():
        print(f'{key}: {value},', end=' ')

person_data(имя='Гвидо', фамилия='Ван Россум', год_рождения=1956, город_проживания='Амстердам', email='python@gmail.com', телефон=1234567890)


