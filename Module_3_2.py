# https://github.com/VasilyDrozhzhin/Lesson0/blob/main/Module_3_2.py
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
	if '@' not in recipient or '@' not in sender or all(recipient.endswith(suffix) == 0 for suffix in ['.ru', '.net', '.com']) or all(sender.endswith(suffix) == 0 for suffix in ['.ru', '.net', '.com']):
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
send_email('Text', '1@go.ru', sender= 'ya@mail.com')