def send_email(message, recipient, sender = "university.help@gmail.com"):
	if '@' not in recipient or '@' not in sender or all(element not in recipient for element in ['.ru', '.com', '.net']) or all(element not in sender for element in ['.ru', '.com', '.net']):
		print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
	elif recipient == sender:
		print('Нельзя отправить письмо самому себе')
	elif sender == 'university.help@gmail.com':
		print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
	else:
		print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
send_email('Тест', 'info@ya.ru')
send_email('Hello', 'test.com')
send_email('New message', 'university.help@gmail.com')
send_email('Text', '1@go.ru', 'ya@mail.com')