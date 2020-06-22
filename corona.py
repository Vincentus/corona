import telebot
from telebot import types
import COVID19Py

covid19= COVID19Py.COVID19()
bot= telebot.TeleBot('1077881028:AAGSDFsYA4SNaI9ddRB1jRMfJpAWJ5VVbkA')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Japan')
    btn2 = types.KeyboardButton('Ukraine')
    btn3 = types.KeyboardButton('Russia')
    btn4 = types.KeyboardButton('USA')
    markup.add(btn1, btn2, btn3, btn4)
    send_message = f'<b> Hello {message.from_user.first_name}!</b>\nChoose a country'
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip()
    if get_message_bot == "USA":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "Ukraine":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "Russia":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "Japan":
        location = covid19.getLocationByCountryCode("JP")
    else:
        location = covid19.getLatest()

        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")

        time = date[1].split(".")

        final_message = f"<u>Data for the country:</u>\nPopulation: {location[0]['country_population']:,}\n" \
                        f"Last update: {date[0]} {time[0]}\nLast data:\n<b>" \
                        f"Cases: </b>{location[0]['latest']['confirmed']:,}\n<b>Deaths: </b>" \
                        f"{location[0]['latest']['deaths']:,}"


    bot.send_message(message.chat.id, final_message,parse_mode='html')

bot.polling(none_stop=True)
