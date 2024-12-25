def send_email(message, recipient, sender='university.help@gmail.com'):
    check_str = ['@', ['.com', '.net', '.ru']]
    include = True
    include1 = True
    include2 = True
    if check_str[0] in sender and check_str[0] in recipient :
        for symb in check_str[1] :
            if symb in sender :
                include1 = True
                break
            else :
                include1 = False
        for symb in check_str[1] :
            if symb in recipient :
                include2 = True
                break
            else :
                include2 = False
        include = include1 * include2
    else :
        include = False
    if not include :
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес ', recipient)
        return
    elif sender == recipient :
        print('Нельзя отправить письмо самому себе!')
        return
    elif sender == 'university.help@gmail.com' :
        print('Письмо успешно отправлено с адреса ', sender, 'на адрес ', recipient)
        return
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес ', recipient)
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')