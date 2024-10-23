"""
Задача "Рассылка писем":
Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя
(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
Попробуем реализовать функцию с подробной логикой.

Создайте функцию send_email, которая принимает 2 обычных аргумента: 
сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
Внутри функции реализовать следующую логику:
Проверка на корректность e-mail отправителя и получателя.
Проверка на отправку самому себе.
Проверка на отправителя по умолчанию.

Пункты задачи:
Создайте функцию send_email, которая принимает 2 обычных аргумента: 
message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением 
по умолчанию sender = "university.help@gmail.com".
 Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", 
    то вывести на экран(в консоль) строку: 
  -  "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
 Если же sender и recipient совпадают, то вывести 
  -  "Нельзя отправить письмо самому себе!"

 Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: 
  -  "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."

 В противном случае вывести сообщение: 
  - "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
"""
import re


def main():
    print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
    print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
    print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
    print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    # Проверка на корректность e-mail отправителя и получателя.
    # for email in (sender, recipient):
    #     if '@' not in email or not email.endswith(('.ru', '.net', '.com')):
    #         return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    pattern = re.compile(r'[a-z0-9_-]+\.?[a-z0-9]*@[\w]+\.(com|ru|net)', re.IGNORECASE)
    if not (re.fullmatch(pattern, recipient) or re.fullmatch(pattern, sender)):
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    # Проверка на отправку самому себе.
    if sender is recipient:
        return f'Нельзя отправить письмо самому себе!'
    # Проверка на отправителя по умолчанию.
    elif sender != 'university.help@gmail.com':
        return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'
    else:
        return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'


if __name__ == '__main__':
    main()