import telebot
import validators

from configs import BOT_TOKEN
from screen_status import get_status_code, make_screenshot

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет ✌️\n'
                     'Введи URL адрес страницы!')


@bot.message_handler(commands=['descriptions'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Введи URL адрес страницы '
                     'и я верну скриншот страницы и код ответа страницы!')


@bot.message_handler(content_types=['text'])
def send_message(message):
    url = message.text

    if validators.url(url):
        satus_code = get_status_code(url)
        file_path = make_screenshot(url)
        if satus_code:
            bot.send_message(
                message.from_user.id,
                f'Kод ответа страницы - {satus_code}')
        else:
            bot.send_message(message.from_user.id,
                             f'Ошибка соединения.Проверьте написание URL {url}'
                             )
        if file_path:
            with open(file_path, 'rb') as screenshot:
                bot.send_photo(message.from_user.id, screenshot)
    else:
        bot.send_message(message.from_user.id,
                         f'Проверьте правильно ли введен URL адрес {url}\n'
                         'или попробуйте проверить данный URL позже!'
                         )
    bot.send_message(message.from_user.id, 'Введите URL')


bot.polling(none_stop=True, interval=0)
