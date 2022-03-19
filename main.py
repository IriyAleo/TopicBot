import telebot  # Импортируем библиотеку телеграм
from telebot import types
import logging

# В телеграме обращаемся к @Fatherbot, создаем имя и API.
# Импортируем данные в программу


bot = telebot.TeleBot("5222318034:AAGD-0LljyHb4zEArfh7lyqgvYl5MYqs01Y")

'''
Прописываем команды help, start и их вывод
'''


@bot.message_handler(commands=['start', 'help'])
def sent_welcome(message):
    bot.reply_to(message, 'Привет! Чем  могу тебе помочь?')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопки в сообщениях")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def inline_key(message):
    if message.text == "Кнопки в сообщениях":
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
        key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
        mainmenu.add(key1, key2)
        bot.send_message(message.chat.id, 'Это главное меню!', reply_markup=mainmenu)
    else:
        bot.reply_to(message, message.text)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
        key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
        mainmenu.add(key1, key2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "key1":
        next_menu = types.InlineKeyboardMarkup()
        key1_1 = types.InlineKeyboardButton(text='Кнопка 1.1', callback_data='key1_1')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu.add(key1_1, back)
        bot.edit_message_text('Это меню уровня 2, для кнопки1!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu)
    elif call.data == "key2":
        next_menu2 = types.InlineKeyboardMarkup()
        key2_1 = types.InlineKeyboardButton(text='Кнопка 2.1', callback_data='key2_1')
        key2_2 = types.InlineKeyboardButton(text='Кнопка 2.2', callback_data='key2_2')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu2.add(key2_1, key2_1, key2_2, back)
        bot.edit_message_text('Это меню уровня 2, для кнопки2!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2)
    elif call.data == "key1_1":
        bot.edit_message_text('Вы ввели кнопку 1.1', call.message.chat.id, call.message.message_id)
    elif call.data == "key2_1":
        bot.edit_message_text('Вы ввели кнопку 2.1', call.message.chat.id, call.message.message_id)
    elif call.data == "key2_2":
        bot.edit_message_text('Вы ввели кнопку 2.2', call.message.chat.id, call.message.message_id)


# Для запуска бота
bot.polling()
