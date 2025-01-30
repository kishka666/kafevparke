
TOKEN = '6883998687:AAH_SK5mf4kkAmkhPrugZmuxDo6DgoJDk5Y'


import telebot 
from telebot import types


bot = telebot.TeleBot('6883998687:AAH_SK5mf4kkAmkhPrugZmuxDo6DgoJDk5Y')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("сайт🌐")
    btn2 = types.KeyboardButton("детали❓")
    btn3 = types.KeyboardButton("записаться✍🏼")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Здравствуйте, {0.first_name}!👋🏻 \n Я — онлайн ассистент банкетного зала «Кафе в Парке»".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(func=lambda message: message.text == "записаться✍🏼")
def handle_appointment(message):
    # Отправка сообщения с инструкциями пользователю
    bot.send_message(message.chat.id, "\n Для записи на встречу понадобятся некоторые детали \n \n Ответьте на следующие вопросы👇🏻 \n \n Пожалуйста, убедитесь, что вы не допустили ошибок! \n \n 1️⃣ Укажите, пожалуйста, ваш номер телефона:")

    # Ожидание ответа от пользователя
    bot.register_next_step_handler(message, processphonenumber)

def processphonenumber(message):
    phone_number = message.text
    # Сохранение номера телефона и переход к следующему вопросу
    bot.send_message(message.chat.id, "2️⃣ Укажите планируемый формат мероприятия:")

    # Ожидание ответа от пользователя
    bot.register_next_step_handler(message, processeventformat, phone_number)

def processeventformat(message, phone_number):
    event_format = message.text
    # Сохранение формата мероприятия и переход к следующему вопросу
    bot.send_message(message.chat.id, "3️⃣ Укажите количество гостей:")

    # Ожидание ответа от пользователя
    bot.register_next_step_handler(message, processguestcount, phone_number, event_format)

def processguestcount(message, phonenumber, eventformat):
    guest_count = message.text
    # Сохранение количества гостей и переход к следующему вопросу
    bot.send_message(message.chat.id, "4️⃣ Укажите дату мероприятия:")

    # Ожидание ответа от пользователя
    bot.register_next_step_handler(message, processeventdate, phonenumber, eventformat, guest_count)

def processeventdate(message, phonenumber, eventformat, guest_count):
    event_date = message.text
    # Сохранение даты мероприятия и завершение диалога
    # Здесь вы можете сохранить все данные в базе данных или переменных для дальнейшей обработки
    manager_id = '1750314815' 
    bot.send_message(manager_id, f"Новая заявка на запись: \n"
                                 f"Номер телефона: {phonenumber} \n"
                                 f"Формат мероприятия: {eventformat} \n"
                                 f"Количество гостей: {guest_count} \n"
                                 f"Дата мероприятия: {event_date}")
    bot.send_message(message.chat.id, "Спасибо, что ответили на все вопросы! \n \n Менеджер свяжется с вами в ближайшее время 🙌🏻 \n \n До встречи в банкетном зале «Кафе в Парке»✨")
    
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "сайт🌐":
        bot.send_photo(message.chat.id, "https://sun9-12.userapi.com/impg/OH2YvOIY_8NuEMQauj8wET5OqiysX8GfEfZHOw/eMKd-o-Hzrk.jpg?size=705x615&quality=95&sign=7e1222ad03dc1b19a5564ca3451a1a46&type=album", caption=" У нас есть очень хороший сайт, где есть много полезной информации! \n \n Ознакомиться с сайтом можно по ссылке 👇🏼 \n \n <a href='https://parksporta.com/kafevparke#rec67125770'> 🌐  перейти на сайт  </a>", parse_mode="HTML")

    elif(message.text == "детали❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("➕плюсы➕")
        btn2 = types.KeyboardButton("формат")
        btn3 = types.KeyboardButton("кухня")
        btn4 = types.KeyboardButton("контакты")
        btn5 = types.KeyboardButton("где нас найти?")
        back = types.KeyboardButton("↩️")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    

    elif message.text == "➕плюсы➕":
        bot.send_photo(message.chat.id, "https://sun9-3.userapi.com/impg/MbleXbXSH-hb8ZRK7FN06oTpaKFmZzlHflBQ3w/FXfBOEemS2w.jpg?size=862x554&quality=95&sign=7385e8c467634409f57a7568dc8da108&type=album", caption="")
        bot.send_photo(message.chat.id, "https://sun9-17.userapi.com/impg/J9aAjbm3bPOaZgeGD2fZlOqCavfTDMX6COTxZg/5oZbv87nfuM.jpg?size=864x546&quality=95&sign=d12443586e6d742e258d4b319dc1bd4e&type=album", caption="")
        bot.send_photo(message.chat.id, "https://sun9-79.userapi.com/s/v1/ig2/D1-8Q4WajYiWmaszFYRjlV2PZOYMfigiKU6MjyfA9YxezIMgVPKv-SD0XO56VhZfeX6yzDke7mFG7JkXddGRa7Sw.jpg?quality=95&as=32x20,48x30,72x46,108x68,160x101,240x152,360x228,480x304,540x342,640x405,720x456,865x548&from=bu&u=-y5f2i_0rImc2YDDFZZFdCCXtVUx98BbIxnUvj292o8&cs=865x548", caption="")
        bot.send_message(message.chat.id,   "\n \n  Наши основные преимущества: "
                                            "\n \n  ✅ Качественный банкетный сервис"
                                            "\n \n  ✅ Опытная команда профессионалов"
                                            "\n \n  ✅ Русская, европейская и авторская кухня"
                                            "\n \n  ✅ Просторный, светлый, многофункциональный зал площадью 300 кв/м"
                                            "\n \n  ✅ Вместимость \n Банкетная рассадка до 200 человек \n Фуршетная рассадка до 300 человек"
                                            "\n \n  ✅ Три площадки для выездных церемоний"
                                            "\n \n  ✅ Благоустроенная парковая территория"
                                            "\n \n  ✅ Географическая доступность и удобная транспортная развязка"
                                            "\n \n  ✅ Собственная парковка"
                                            "\n \n  ✅ Барная зона"
                                            "\n \n  ✅ Профессиональное звуковое, световое оборудование и LED-экран"
                                            "\n \n  ✅ Выездное обслуживание")

    elif message.text == "формат":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("кейтеринг")
        button2 = types.KeyboardButton("акции")
        button3 = types.KeyboardButton("банкет")
        button4 = types.KeyboardButton("аренда зала")
        back = types.KeyboardButton("↩️")
        markup.add(button1, button2, button3, button4, back)
        bot.send_message(message.chat.id, text="выберете интересующий вас формат", reply_markup=markup)

    elif(message.text == "кухня"):
        bot.send_photo(message.chat.id, "https://sun9-34.userapi.com/impg/20n8qI43mmGdHEkUeFFI6Kqs1YLUpyV26Wexww/pBc0t8yGZ2w.jpg?size=860x553&quality=95&sign=d075a1fb5231a0319167f9b4e9d7bdff&type=album", caption=  "В меню включены блюда: европейской, авторской и русской кухни ✨ \n \n Наша кухня является сочетанием проверенных рецептов и новых веяний современного искусства! \n \n Наше меню насчитывает более 200 блюд \n \n Вы можете воспользоваться нашим меню, либо мы предложим индивидуальный вариант, согласно вашим пожеланиям и вкусам ❤️ \n \n  На ваше усмотрение, возможно самостоятельно организовать алкоголь для мероприятия. \n \n Для вашего мероприятия вы  можете самостоятельно привезти необходимый алкоголь, который вам нравится, либо воспользоваться работой нашего бара  \n \n * Пробковый сбор отсутствует — вы никак не доплачиваете нам за распитие привезенного алкоголя 🙌🏻")

    elif(message.text == "контакты"):
        bot.send_message(message.chat.id, "\n \n Связаться с нами можно любый удобным способом: \n \n 📞 +7 (3852) 76 00 76  \n \n WhatsApp: \n +7 (913) 221 74 64 \n \n E-mail: \n cafevparke@yandex.ru")

    elif(message.text == "где нас найти?"):
        bot.send_photo(message.chat.id, "https://sun9-29.userapi.com/impg/_6XFBpiqDtho3XW9Ewz4a6NKhoeNigs4cUbcFQ/CrHqXhekDGM.jpg?size=835x439&quality=95&sign=ac01f59a57bad48bb976f0c5899033e5&type=album", caption= "\n \n Мы находимся по адресу: \n \n Город Барнаул \n 📍 ул. Энтузиастов 12в, к2")

    elif(message.text == "кейтеринг"):
        bot.send_photo(message.chat.id, "https://sun9-72.userapi.com/impg/sRy72ODDlCuOSH42RhLou4LFdhzh1ZW8EMe49Q/ln1iQqn629w.jpg?size=859x552&quality=95&sign=587f670de70cc982d4645b0e7a0e0b46&type=album", caption="\n Кейтеринг, простыми словами, — это выездной «ресторан», который может накормить ваших гостей 🙌🏻 \n \n 🏷️ Средний чек: \n 5600₽ на человека \n \n📍Область доставки: \n В пределах города Барнаула \n (далее по договоренности) \n \n * Обслуживание, доставка и пригтовление еды уже включены в средний чек")
    
    elif(message.text == "акции"):
        bot.send_message(message.chat.id, "На данный момент, к сожалению, акций нет, но ближе к летнему сезону они обязательно появятся! ✨")

    elif(message.text == "банкет"):
       bot.send_photo(message.chat.id, "https://sun9-39.userapi.com/s/v1/ig2/0n4DJQ4QVIZip5fcPOQH3FLqY_aFKgsx38M7SglbNgPCubwTSAnjV0Y673QRIeqVjGp3wAq2lbwULhnIj4t6aO4X.jpg?quality=95&as=32x20,48x31,72x46,108x69,160x102,240x153,360x229,480x305,540x344,640x407,720x458,866x551&from=bu&u=au0d_3Me4U3T_tl9v8vdCmKdOFrl6pV25x0M3PPG7i8&cs=866x551", caption="\n  Банкет — это праздничный обед или ужин в честь какого-либо торжественного события или даты✨ \n \n Это может быть что угодно: \n свадьба, юбилей или выпускной, мы рады всем праздникам! \n  \n  🏷️ Средний чек:\n 4500₽ на человека \n  \n — Что входит в средний чек? \n \n  Аренда зала, полное обслуживание, вкусное меню приготовленное специально для вас 🙌🏻 \n  \n Так же у нас есть целых 3 площадки для выездных регистраций: \n \n Две на открытом воздухе и одна под крышей, чтобы дождик не испортил ваш праздник ❤️")

    elif(message.text == "аренда зала"):
        bot.send_photo(message.chat.id, "https://sun9-68.userapi.com/impg/vuws3ZVx8qUgL3bGJ12dIn6y399YwsR8KxC6Gg/oYvDgJZ1QZk.jpg?size=1280x960&quality=95&sign=2093d6f8e6c70b9590927dc00fb2ee58&type=album", caption="\n  Наш зал 300кв/м можно снять в аренду 🙌🏻 \n \n Подойдет для проведения конференций, собраний и т.д. \n \n Организация фуршетной линии и чайной зоны, по желанию ✨\n \n Закрытие зала от суммы \n 50 000₽ \n \n В эту сумму входит аренда помещения, персонала, мебели и необходимой фурнитуры!")
    
    elif (message.text == "↩️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("сайт🌐")
        button2 = types.KeyboardButton("детали❓")
        button3 = types.KeyboardButton("записаться✍🏼")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован 🙄 \n \nПопробуйте, пожалуйста, воспользоваться кнопками, с ними я дружу отлично 😉 ")

bot.polling(none_stop=True)