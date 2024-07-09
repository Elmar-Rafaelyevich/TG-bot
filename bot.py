import telebot
from telebot import types
from token_bot import bot_token
from main import *
import os

if not os.path.exists('documents'):
    os.makedirs('documents')
    

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def main(message):
    
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton("✈️ Reyslar", callback_data=reys)
    b2 = types.InlineKeyboardButton("📌 Narxlar", callback_data=narxlar) 
    b3 = types.InlineKeyboardButton("📷 Videolar", callback_data=videolar) 
    b4 = types.InlineKeyboardButton("📲 Bo'glanish", callback_data=boglanish) 
    b5 = types.InlineKeyboardButton("🛎 Mexmonxonalar", callback_data=mexmonxonalar)
    b6 = types.InlineKeyboardButton("⏳ Namoz vaqtlari", callback_data=namoz)
    b7 = types.InlineKeyboardButton("✏️ Ro'yxatdan otish", callback_data=test)

    markup.row(b1, b2)
    markup.row(b3,b4)
    markup.row(b5)
    markup.row(b6)
    markup.row(b7)
    
    bot.send_message(message.chat.id, f"Assalomu alekum {message.from_user.first_name}\nSalaam travelga hush kelibsiz !", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: True)
def checkout_message(call):
    if call.data == reys:
        bot.send_message(call.message.chat.id, "Reyslar boicha malumot:")
        send_last_image(call.message)
        
    elif call.data == ortga:
        main(call.message)
        
    elif call.data == narxlar:
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("🛫 Ekanom", callback_data=ekanom)
        b2 = types.InlineKeyboardButton("🛫 Standart", callback_data=standart)
        b3 = types.InlineKeyboardButton("🛫 Luks", callback_data=luks)
        exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
        
        markup.row(b1,b2,b3)
        markup.row(exit_b)
        bot.send_message(call.message.chat.id, narxlar_comment, reply_markup=markup)       
        
    elif call.data == ekanom:
        ekanom_fun(call.message)
        
    elif call.data == standart:
        standart_fun(call.message)
        
    elif call.data == luks:
        luks_fun(call.message)
        
    elif call.data == videolar:
        video_fun(call.message)
        
    elif call.data == boglanish:
        call_fun(call.message)
        
    elif call.data == mexmonxonalar:
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("🕋 Makka", callback_data=makka)
        b2 = types.InlineKeyboardButton("🕋 Madina", callback_data=madina)
        exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
        
        markup.row(b1, b2)
        markup.row(exit_b)
        
        bot.send_message(call.message.chat.id, "🕋 Qaysi birini tanlaysiz ?", reply_markup=markup)
    
    elif call.data == makka:
        makka_hotel_fun(call.message)
    
    elif call.data == madina:
        madina_hotel_fun(call.message)
    
    elif call.data == namoz:
        bot.send_message(call.message.chat.id, "Namoz vaqtlari boicha malumot :")
        send_last_namoz_time(call.message)
        
    elif call.data == test:
        name = bot.send_message(call.message.chat.id, "✍️ Ism Familiya yozib qoldiring!\nMisol: Abduganiyev, Islombek")
        bot.register_next_step_handler(name, get_name)

def get_name(message):
    global name
    name = message.text.strip()
    if name:
        phone = bot.send_message(message.chat.id, "📞 Telefon raqam kiriting!\nMisol: +998977777777")
        bot.register_next_step_handler(phone, get_phone)
    else:
        bot.send_message(message.chat.id, "Ism Familiya noto'g'ri. Iltimos qaytadan kiriting.")
        retry_name = bot.send_message(message.chat.id, "✍️ Ism Familiya yozib qoldiring!\nMisol: Abduganiyev, Islombek")
        bot.register_next_step_handler(retry_name, get_name)

def get_phone(message):
    global phone
    phone = message.text
    if phone.startswith('+') and len(phone) == 13:
        bot.send_message(message.chat.id, "Ma'lumotlaringiz qabul qilindi.")
        bot.send_message(-1002187998767, f"{name} - {phone}")
    else:
        bot.send_message(message.chat.id, "Telefon raqam noto'g'ri. Iltimos qaytadan kiriting.")
        retry_phone = bot.send_message(message.chat.id, "📞 Telefon raqam kiriting!\nMisol: +998977777777")
        bot.register_next_step_handler(retry_phone, get_phone)

        
def madina_hotel_fun(message):
    exit_markup = types.InlineKeyboardMarkup()
    exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
    with open("hotel/madina_video.mp4", 'rb') as photo:
        exit_markup.row(exit_b)
        bot.send_video(message.chat.id, photo, reply_markup=exit_markup)
        
def makka_hotel_fun(message):
    exit_markup = types.InlineKeyboardMarkup()
    exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
    with open("hotel/madina_video.mp4", 'rb') as img:
        exit_markup.row(exit_b)
        bot.send_video(message.chat.id, img, reply_markup=exit_markup)
        
        
def call_fun(message):
    exit_markup = types.InlineKeyboardMarkup()
    exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
    exit_markup.add(exit_b)
        
    bot.send_message(message.chat.id, admin_info, reply_markup=exit_markup)
    
def video_fun(message):
    exit_markup = types.InlineKeyboardMarkup()
    exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
    exit_markup.add(exit_b)
        
    bot.send_message(message.chat.id, videolar, reply_markup=exit_markup)
    
    
def luks_fun(message):
    exit_markup = types.InlineKeyboardMarkup()
    exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
    exit_markup.add(exit_b)
    
    bot.send_message(message.chat.id, luks_list, reply_markup=exit_markup)
    
    
def standart_fun(message):
    exit_markup = types.InlineKeyboardMarkup()
    exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
    exit_markup.add(exit_b)
    
    bot.send_message(message.chat.id, standart_list, reply_markup=exit_markup)
    
        
        
def ekanom_fun(message):
    exit_markup = types.InlineKeyboardMarkup()
    exit_b = types.InlineKeyboardButton("◀️ O'rtga", callback_data=ortga)
    exit_markup.add(exit_b)
    
    bot.send_message(message.chat.id, ekanom_list, reply_markup=exit_markup)
    

@bot.message_handler(content_types=['text'])
def admin_panel_fun(message):
    
    if message.text == "/reys":
        msg = bot.send_message(message.chat.id, "Menga PNG faylni yuklang !")
        bot.register_next_step_handler(msg, file_checkout_fun)
        
    elif message.text == "/namoz":
        namoz_msg = bot.send_message(message.chat.id, "Menga PNG faylni yuklang !")
        bot.register_next_step_handler(namoz_msg, namoz_msg_checkout_fun)
        
        
def namoz_msg_checkout_fun(message):
    if message.document:
        if message.document.mime_type == 'image/png' or message.document.mime_type == 'image/jpeg':
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            file_path = os.path.join('namoz', message.document.file_name)
            with open(file_path, "wb") as new_file:
                new_file.write(downloaded_file)
            
            bot.send_message(message.chat.id, f"{message.document.mime_type.upper()} Jonatilgan fayl saqlandi")
        else:
            bot.send_message(message.chat.id, "Qaytatan menga PNG JPG faylni yuklang ! /start")
    else:
        bot.send_message(message.chat.id, "Qaytatan menga PNG JPG faylni yuklang ! /start")
        
    
def send_last_namoz_time(message):
    files = sorted(
        [f for f in os.listdir('namoz') if f.endswith('.png') or f.endswith('.jpg')],
        key=lambda x: os.path.getmtime(os.path.join('namoz', x)),
        reverse=True
    )
    
    if files:
        last_file = files[0]
        file_path = os.path.join('namoz', last_file)
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, "Fayl mavjud emas !")

def file_checkout_fun(message):
    if message.document:
        if message.document.mime_type == 'image/png' or message.document.mime_type == 'image/jpeg':
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            file_path = os.path.join('documents', message.document.file_name)
            with open(file_path, "wb") as new_file:
                new_file.write(downloaded_file)
            
            bot.send_message(message.chat.id, f"{message.document.mime_type.upper()} Jonatilgan fayl saqlandi")
        else:
            bot.send_message(message.chat.id, "Qaytatan menga PNG JPG faylni yuklang ! /start")
    else:
        bot.send_message(message.chat.id, "Qaytatan menga PNG JPG faylni yuklang ! /start")

def send_last_image(message):
    files = sorted(
        [f for f in os.listdir('documents') if f.endswith('.png') or f.endswith('.jpg')],
        key=lambda x: os.path.getmtime(os.path.join('documents', x)),
        reverse=True
    )
    
    if files:
        last_file = files[0]
        file_path = os.path.join('documents', last_file)
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, "Fayl mavjud emas !")

bot.polling(non_stop=True)
