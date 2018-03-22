import config
import telebot
import re

bot = telebot.TeleBot(config.token)
cout = {}

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id,
                            'Я дофига умный медицинский бот! Вот что умею:   Формула Кокрофта-Голта  \nДля мужчин введите 1 \nДля женщин 2')
 #   print(message.text)
    bot.register_next_step_handler(sent, gender)

def gender(message):
    if str(message.text) == '1':
        print('Men')
        sent = bot.send_message(message.chat.id,
                                'Теперь введите данные в формате: возраст в годах, масса тела в кг, креатин крови в мкмоль/л. Например: 45 80 135')
        bot.register_next_step_handler(sent, men)
    elif str(message.text) == '2':
        print('Women')
        sent = bot.send_message(message.chat.id,
                                'Теперь введите данные в формате: возраст в годах, масса тела в кг, креатин крови в мкмоль/л. Например: 45 80 135')
        bot.register_next_step_handler(sent, women)
    else:
        wrong_sent = bot.send_message(message.chat.id, 'Вы ввели какую-то дичь, попробуйте еще раз \nВведите /start')
        bot.register_next_step_handler(wrong_sent, start)

def check_user_input(data):
    pattern = re.compile(r'\d{0,3} \d{0,3} \d{0,4}')

    if pattern.match(data) is None:
        return False
    else:
        return True

def men(message):
    print('enter v men')
    print(str(message.text))
    if check_user_input(str(message.text)):
        data = str(message.text).split(' ')
        int_data=[]
        for i in data:
            i=int(i)
            int_data.append(i)
            print(i)
        result = 1.23 * (((140 - int_data[0]) * int_data[1])/int_data[2])
        print(result)
        bot.send_message(message.chat.id, 'Вот тебе и СКФ:  ' + str(result) + '\nА вообще-то норма для мужчин: 90 - 150 мл/мин \n')
        sent = bot.send_message(message.chat.id, 'Могу еще разок! :)  \nВведите /start')
        bot.register_next_step_handler(sent, start)
    else:
        sent = bot.send_message(message.chat.id, 'Retry  \nВведите /start')
        bot.register_next_step_handler(sent, start)

def women(message):
    if check_user_input(str(message.text)):
        print('enter v women')
        data = str(message.text).split(' ')
        int_data=[]
        for i in data:
            i=int(i)
            int_data.append(i)
            print(i)
        result = 1.05 * (((140 - int_data[0]) * int_data[1])/int_data[2])
        print(result)
        bot.send_message(message.chat.id, 'Вот тебе и СКФ:  ' + str(result) + '\nА вообще-то норма для женщин: 90 - 130 мл/мин \n')
        sent = bot.send_message(message.chat.id, 'Могу еще разок! :)  \nВведите /start')
        bot.register_next_step_handler(sent, start)
    else:
        sent = bot.send_message(message.chat.id, 'Retry  \nВведите /start')
        bot.register_next_step_handler(sent, start)

# def count_for_men(message):
#     data = list(message.text)
#     print(data)
#



# def in_age():
#
#         age = int(message.text)
#         #a = age + 1
#         print(age)
#         bot.send_message(message.chat.id, 'Теперь введите массу тела в килограммах, например 60.5 (десятые через точку)')
#         m = int(message.text)
#         bot.send_message(message.chat.id, 'Теперь введите креатин крови в мкмоль/л')
#         kre = int(message.text)
#         skf = 1.23 *((140 - age * m)/kre)
#         bot.send_message(message.chat.id, 'СКФ = ' + skf)
#    else:
#       print('Women')

if __name__ == '__main__':
    bot.polling(none_stop=True)

