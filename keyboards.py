from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

start_keyboard = [
        
            [InlineKeyboardButton("Подробнее об АН", callback_data="/about")],
            [InlineKeyboardButton("Расписание собраний", callback_data="/schedule")],
            [InlineKeyboardButton("Задать вопрос", url="https://t.me/Iraivano")],
        
    ]

start_admin_keyboard = [
        
            [InlineKeyboardButton("Подробнее об АН", callback_data="/about")],
            [InlineKeyboardButton("Расписание собраний", callback_data="/schedule")],
            [InlineKeyboardButton("Задать вопрос", url="https://t.me/Iraivano")],
            [InlineKeyboardButton("Редактировать сообщения", callback_data="/admin")],

        
    ]

start_keyboard = InlineKeyboardMarkup(start_keyboard)
start_admin_keyboard = InlineKeyboardMarkup(start_admin_keyboard)

about_keyboard = [
        
            [InlineKeyboardButton("Анонимность", callback_data="/anonymous")],
            [InlineKeyboardButton("Кто является членом АН?", callback_data="/whoismember")],
            [InlineKeyboardButton("Что из себя представляет АН?", callback_data="/whatisna")],
            [InlineKeyboardButton("О собраниях Анонимных Наркоманов?", callback_data="/whatismeeting")],
            [InlineKeyboardButton("Хочешь прийти в первый раз?", callback_data="/firsttime")],
            [InlineKeyboardButton("Мы в Интернете", callback_data="/weweb")],
            [InlineKeyboardButton("В начало", callback_data="/main")]
        
    ]
about_keyboard = InlineKeyboardMarkup(about_keyboard)
web_keyboard = [
        
            [InlineKeyboardButton("Сайт", url="https://na-russia.org")],
            [InlineKeyboardButton("Youtube", url="https://youtube.com/@narcotics_anonymous_russia")],
            [InlineKeyboardButton("Яндекс.Дзен", url="https://dzen.ru/narcotics_anonymous")],
            [InlineKeyboardButton("Instagram", url="https://www.instagram.com/narcotics_anonymous_russia")],
            [InlineKeyboardButton("VK", url="https://m.vk.com/na_russia_official")],
            [InlineKeyboardButton("Подкасты", url="https://podcastna.mave.digital")],
            [InlineKeyboardButton("В начало", callback_data="/main")]
        
    ]
web_keyboard = InlineKeyboardMarkup(web_keyboard)

first_time_keyboard = [
        
            [InlineKeyboardButton("Зависимый ли я?", callback_data="/addicted")],
            [InlineKeyboardButton("Несколько правил собраний АН", callback_data="/rules")],
            [InlineKeyboardButton("Несколько личных историй", url="https://radio-na.ru/")],
            [InlineKeyboardButton("В начало", callback_data="/main")]
        
    ]
first_time_keyboard = InlineKeyboardMarkup(first_time_keyboard)


schedule_keyboard = [
        
            [InlineKeyboardButton("Пхукет", callback_data="/phuket")],
            [InlineKeyboardButton("Таиланд", url="https://na-thailand.org/meetings/")],
            [InlineKeyboardButton("Россия", url="https://na-russia.org/")],
            [InlineKeyboardButton("Другие страны", url="https://www.na.org/meetingsearch/")],
            [InlineKeyboardButton("В начало", callback_data="/main")]
        
    ]
schedule_keyboard = InlineKeyboardMarkup(schedule_keyboard)

KEYBOARDS = {
    '/about': about_keyboard,
    '/schedule': schedule_keyboard,
    '/ask': start_keyboard,
    '/anonymous': about_keyboard,
    '/whoismember': about_keyboard,
    '/whatisna': about_keyboard,
    '/whatismeeting': about_keyboard,
    '/firsttime': first_time_keyboard,
    '/weweb': web_keyboard,
    '/main': start_keyboard,
    '/cite': web_keyboard,
    '/youtube': web_keyboard,
    '/dzen': web_keyboard,
    '/insta': web_keyboard,
    '/vk': web_keyboard,
    '/podcasts': web_keyboard,
    '/addicted': first_time_keyboard,
    '/rules': first_time_keyboard,
    '/history': first_time_keyboard,
    '/phuket': schedule_keyboard,
    '/thai': schedule_keyboard,
    '/russia': schedule_keyboard,
    '/countries': schedule_keyboard,
    '/history': first_time_keyboard
    }