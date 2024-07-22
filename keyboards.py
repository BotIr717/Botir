from aiogram.types import InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton

lang_menu = ReplyKeyboardMarkup(resize_keyboard=True)
lang_menu.add(KeyboardButton('Ko\'p so\'raladigan savollar'))



savollar_menu = ReplyKeyboardMarkup(resize_keyboard=True)
savollar_menu.add(KeyboardButton('Uzum nasiya muddatli to\'lovi haqida')),
savollar_menu.add(KeyboardButton('Shartnoma')),
savollar_menu.add(KeyboardButton('Xizmat bilan bog\'liq muammolar')),
savollar_menu.add(KeyboardButton('Aloqa usullari')),


About_Tolov_menu = ReplyKeyboardMarkup(resize_keyboard=True)
About_Tolov_menu.add(KeyboardButton('Uzum nasiya nima?'))
About_Tolov_menu.add(KeyboardButton('Qanday ta\'riflar mavjud?'))
About_Tolov_menu.add(KeyboardButton('Qaysi do\'konlarda sizlar taqdim etayotgan muddatli to\'lovdan foydalansak bo\'ladi?'))
About_Tolov_menu.add(KeyboardButton('Uzum nasiya to\'lovi banki kreditdan nimasi bilan farq qiladi?'))

Shartnoma = ReplyKeyboardMarkup(resize_keyboard=True)
Shartnoma.add(KeyboardButton('Qanday qilib ro\'yxatdan o\'tish va limitni olish mumkin?'))
Shartnoma.add(KeyboardButton('Muddatli to\'lovni rasmiylashtirish uchun qanday talablar mavjud?'))
Shartnoma.add(KeyboardButton('Muddatli to\'lov shartnomalari/to\'lov jadvali/qarz qoldig\'ini qayerda ko\'rishim mumkin?'))
Shartnoma.add(KeyboardButton('Shartnomani qanday bekor qilish mumkin?'))

Muammolar = ReplyKeyboardMarkup(resize_keyboard=True)
Muammolar.add(KeyboardButton('Nima uchun men bloklandim?'))
Muammolar.add(KeyboardButton('Xizmatingizdan qanday foydalanishni tushunmadim?'))
Muammolar.add(KeyboardButton('Nima uchun uzum nasiya ilovasida mahsulotni korib bolmaydi?'))
Muammolar.add(KeyboardButton('Men kartamni ulay olmayapman.'))

Aloqa = ReplyKeyboardMarkup(resize_keyboard=True)
Aloqa.add(KeyboardButton('Operator bilan bog\'lanish.'))
Aloqa.add(KeyboardButton('Orqaga'))