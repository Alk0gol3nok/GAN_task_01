pass_check = 'Grigorev0611^^'
secret_message = 'ты получаешь "5" за эту работу'
password = input('Введите секретный пароль: ')
attempt = 3
while password != pass_check:
    if password == pass_check:
        print('Ваше секретное сообщение:', secret_message)
        break
    else:
        attempt -= 1
        print('Вы ввели не верный пароль, у вас осталось:', attempt, 'попытки')
        if attempt <= 0:
            print('Вы исчерпали своё количество попыток')
            break
        else:
            password = input('Введите секретный пароль: ')
else:
    print('Ваше секретное сообщение:', secret_message)
