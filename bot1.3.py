import sqlite3
import telebot
from telebot import types # для указание типов

conn = sqlite3.connect('db/database.db', check_same_thread=False)
cursor = conn.cursor()


token = ''
bot = telebot.TeleBot(token)

def db_table_val(cash: int, tasks: int, user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (cash, tasks, user_id) VALUES (?, ?, ?, ?, ?, ?)', (cash, tasks, user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Подпишись", url='https://t.me/Moneypocketfree')
    markup.add(button1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name} с каналом MoneyPocket можно заработать быстро и без усилий, попробуй прямо сейчас.".format(message.from_user), reply_markup=markup)#PLAVAET KNOPKA
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Заработать")
    btn2 = types.KeyboardButton("Личный кабинет")
    btn3 = types.KeyboardButton("Поддержка")
    btn4 = types.KeyboardButton("FAQ")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="ОБЯЗАТЕЛЬНО ОЗНАКОМЬСЯ С ПУНКТОМ FAQ".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "FAQ"):
        bot.send_message(message.chat.id, text="""Правила команды MoneyPocket.
1) Расценка на оформления карт постоянно меняется, уточните информацию по подходящему вам предложению у оператора в поддержке
2) После оформления заявки обязательно отпишите оператору, со скриншотом вашей заявки на карту/займ
3) После получения карты/займа сообщите об этом оператору. 
Так мы проконтролируем и устраним ошибки с нашей партнерской системой, чтобы вы не остались без вознаграждения.
4) После предоставления всей информации оператору, ожидайте выплату, они происходят в ручном режиме на любую банковскую карту/qiwi кошелек""")
    elif(message.text == "Заработать"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Дебетовые карты")
        btn2 = types.KeyboardButton("Кредитные карты")
        btn3 = types.KeyboardButton("Оформление займов")
        btn4 = types.KeyboardButton("Устройство на работу")
        back = types.KeyboardButton("Нaзaд")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Выберите один из способов заработать", reply_markup=markup)
    elif(message.text == "Дебетовые карты"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Альфа", url='https://alfa.me/hildQg')
        button2 = types.InlineKeyboardButton("Тинькофф", url='bit.ly/3opOYGy')
        button3 = types.InlineKeyboardButton("Райффайзен", url='bit.ly/3L7E4Pb')
        button4 = types.InlineKeyboardButton("ВТБ", url='bit.ly/3Ln3KHZ')
        button5 = types.InlineKeyboardButton("УБРиР", url='bit.ly/3rnkmqW')
        button6 = types.InlineKeyboardButton("Промсвязьбанк", url='bit.ly/3sl6DQC')
        button7 = types.InlineKeyboardButton("Газпромбанк", url='bit.ly/3oMlNxB')
        button8 = types.InlineKeyboardButton("Росбанк", url='bit.ly/3sbhAUI')
        button9 = types.InlineKeyboardButton("Хоум Кредит", url='bit.ly/3rovBiS')
        button10 = types.InlineKeyboardButton("Открытие", url='bit.ly/3sgnrbu')
        button11 = types.InlineKeyboardButton("ОТП Банк", url='bit.ly/34FqBO4')
        button12 = types.InlineKeyboardButton("БАНК", url='bit.ly/34FqBO4')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
        bot.send_message(message.chat.id, text="Дебетовы карты список: ".format(message.from_user), reply_markup=markup)
     
    elif(message.text == "Оформление займов"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Max.Credit", url='bit.ly/3sbhsES')
        button2 = types.InlineKeyboardButton("Деньги сразу", url='bit.ly/3AZgf7q')
        button3 = types.InlineKeyboardButton("Creditter", url='bit.ly/3uuCd10')
        button4 = types.InlineKeyboardButton("Ракета-деньги", url='https://t.me/Moneypocketfree')
        button5 = types.InlineKeyboardButton("До Зарплаты", url='bit.ly/3omNf4r')
        button6 = types.InlineKeyboardButton("Надо Денег", url='bit.ly/3sbhsES')
        button7 = types.InlineKeyboardButton("еКапуста", url='bit.ly/3sbhsES')
        button8 = types.InlineKeyboardButton("One Click Money", url='bit.ly/3sbhsES')
        button9 = types.InlineKeyboardButton("Отличные наличные", url='bit.ly/3sbhsES')
        button10 = types.InlineKeyboardButton("МигКредит", url='bit.ly/3sbhsES')
        button11 = types.InlineKeyboardButton("Pay P.S.", url='bit.ly/3sbhsES')
        button12 = types.InlineKeyboardButton("Умные наличные", url='bit.ly/3sbhsES')
        button13 = types.InlineKeyboardButton("Credit7", url='bit.ly/3sbhsES')
        button14 = types.InlineKeyboardButton("Займер", url='bit.ly/3sbhsES')
        button15 = types.InlineKeyboardButton("Ezaem", url='bit.ly/3sbhsES')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15)
        bot.send_message(message.chat.id, text="Микрозайм:".format(message.from_user), reply_markup=markup)
    
    elif(message.text == "Устройство на работу"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("«Яндекс.Еда»: курьер", url='bit.ly/3sbhsES')
        button2 = types.InlineKeyboardButton("«Яндекс.Еда»: сборщик", url='bit.ly/3AZgf7q')
        button3 = types.InlineKeyboardButton("DeliveryClub: курьер по доставке еды", url='bit.ly/3uuCd10')
        button4 = types.InlineKeyboardButton("KFC: сотрудник ресторана.", url='https://t.me/Moneypocketfree')
        button5 = types.InlineKeyboardButton("«Бургер Кинг»: сотрудник ресторана.", url='bit.ly/3omNf4r')
        button6 = types.InlineKeyboardButton("«Сбермаркет»", url='bit.ly/3sbhsES')
        button7 = types.InlineKeyboardButton("«Самокат»: курьер", url='bit.ly/3sbhsES')
        button8 = types.InlineKeyboardButton("«ВкусВилл»: трудоустройство", url='bit.ly/3sbhsES')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8 )
        bot.send_message(message.chat.id, text="Открытые ванаксий:".format(message.from_user), reply_markup=markup)

    elif(message.text == "Кредитные карты"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Альфа", url='bit.ly/3sbhsES')
        button2 = types.InlineKeyboardButton("Тинькофф", url='bit.ly/3AZgf7q')
        button3 = types.InlineKeyboardButton("Райффайзен", url='bit.ly/3uuCd10')
        button4 = types.InlineKeyboardButton("ВТБ", url='https://t.me/Moneypocketfree')
        button5 = types.InlineKeyboardButton("Открытие", url='bit.ly/3omNf4r')
        markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, text="Кредитные карты список: ".format(message.from_user), reply_markup=markup) 

    elif(message.text == "Поддержка"):
        bot.send_message(message.chat.id, "@MoneyPocketSupport")
    
    elif message.text == "Личный кабинет":
            bot.send_message(message.chat.id, text="""
КЛИЕНТ:  {0.first_name} 
ID:
                """.format(message.from_user))



    
    elif (message.text == "Нaзaд"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Заработать")
        button2 = types.KeyboardButton("Личный кабинет")
        button3 = types.KeyboardButton("Поддержка")
        button4 = types.KeyboardButton("FAQ")
        markup.add(button1, button2, button3, button4)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Введите корректную команду")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Личный кабинет':

         
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


bot.polling(none_stop=True)
