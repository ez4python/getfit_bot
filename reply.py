from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def bot_menu():
    btn1 = KeyboardButton(text="Filial 📍")
    btn2 = KeyboardButton(text="Start ✅")
    btn3 = KeyboardButton(text="Admin 👨🏻‍💻")
    btn4 = KeyboardButton(text="News")
    design = [
        [btn1, btn2],
        [btn3],
        [btn4]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def start():
    btn1 = KeyboardButton(text="Woman️")
    btn2 = KeyboardButton(text="Men")
    btn3 = KeyboardButton(text="🔙 Back")
    design = [
        [btn1, btn2],
        [btn3]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def man_woman():
    btn1 = KeyboardButton(text="1-oy")
    btn2 = KeyboardButton(text="2-oy")
    btn3 = KeyboardButton(text="3-oy")
    btn4 = KeyboardButton(text="4-oy")
    btn5 = KeyboardButton(text="🔙 Back")
    design = [
        [btn1, btn2],
        [btn3, btn4],
        [btn5]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def week_days():
    btn1 = KeyboardButton(text="Dushanba")
    btn2 = KeyboardButton(text="Seshanba")
    btn3 = KeyboardButton(text="Chorshanba")
    btn4 = KeyboardButton(text="Payshanba")
    btn5 = KeyboardButton(text="Juma")
    btn6 = KeyboardButton(text="Shanba")
    btn7 = KeyboardButton(text="🔙 Back")
    design = [
        [btn1, btn2, btn3],
        [btn4, btn5, btn6],
        [btn7]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
