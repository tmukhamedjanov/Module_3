def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    if list(recipient) != "@" or list(sender) != "@":
        if len(recipient.split("@")) != 2 or len(sender.split("@")) != 2:
            #Проверка на наличие только одного "@" в адресе почты
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            return 0
        if (recipient.split("@")[1][-3:] != ".ru" and
            recipient.split("@")[1][-4:] != ".com" and
            recipient.split("@")[1][-4:] != ".net" or
            sender.split("@")[1][-3:] != ".ru" and
            sender.split("@")[1][-4:] != ".com" and
            sender.split("@")[1][-4:] != ".net"):
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
                return 0
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            return 0
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")








send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

