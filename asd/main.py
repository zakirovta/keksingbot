import json
import telebot




# Создаем экземпляр бота
bot = telebot.TeleBot('5264941039:AAEIZ318TErur-JAGX3F1CZSyCd241Aic1M')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Пришли контакт, кого хочешь пригласить на свидание )')
# Получение сообщений от юзера



@bot.message_handler(content_types=["contact"])


def handle_text(message):
    username = str(message.from_user.id) # сохраняем id пользователя

    filename = 'sample3.json' 
    with open(filename) as f: # открываем json 
        data = json.load(f)

    if username in data.keys():
        data[username].append(str(message.contact.user_id)) # если пользователь уже есть в файле, добавляем его контакты
    if username not in data.keys():
        data[username] = [str(message.contact.user_id)] # если пользователь новый, создаем новую запись
    with open(filename, "w") as write_file:
        json.dump(data, write_file)
    #'''
    bot.send_message(message.chat.id, 'Контанкт добавлен')






if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

