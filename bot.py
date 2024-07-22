from aiogram import Dispatcher,Bot,executor,types
from keyboards import lang_menu,savollar_menu,About_Tolov_menu,Shartnoma,Muammolar,Aloqa
api = '6726592936:AAECEtZEt7noWVa_ZHUCovUDq2uLb0vKr0c'
bot = Bot(api)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer(text=f'Assalamu aleykum {sms.from_user.first_name} bizning botimizga xush kelibsiz iltimos o\'zingizga yoqgan menuni tanlang:',reply_markup=lang_menu)


@dp.message_handler(text='Ko\'p so\'raladigan savollar')
async def send_menu(sms:types.Message):
    await sms.answer(text='Ko\'p so\'raladigan savollar:',
                     reply_markup=savollar_menu)


@dp.message_handler(text='Uzum nasiya muddatli to\'lovi haqida')
async def send_menu(sms:types.Message):
    await sms.answer(text='Ko\'p so\'raladigan savollar:',
                     reply_markup=About_Tolov_menu)
    

@dp.message_handler(text='Uzum nasiya nima?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Uzum Nasiya — bu butun O\'zbekiston bo\'ylab hamkorlik nuqtalarda foydalanish mumkin bo\'lgan, tovar va xizmatlarni muddatli to\'lovga xarid qilishga mo\'ljallangan xizmatdir.\n Buning uchun Uzum Nasiya mobil ilovasida yoki uzumnasiya.uz. saytida ro\'yxatdan o\'tish kerak:\n\n''Sizni qiziqtirgan savolni tanlang:',               
                     reply_markup=About_Tolov_menu)
    

@dp.message_handler(text='Qanday ta\'riflar mavjud?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Birinchisi: 0-0-3 muddatli to\'lovi ya\'ni ustamasiz va boshlang\'ich to\'lovsiz 3 ta teng qismga bo\'lib to\'lash. Mavjud maksimal miqdor — 5 mln. so\'m. Siz nasiyaning ushbu turidan O\'zbekiston bo\'ylab 1 000 dan ortiq hamkor nuqtalarda xarid uchun foydalanishingiz mumkin.\n\nIkkinchisi: 6 yoki 12 oy muddatga 20 mln. so\'mgacha bo\'lgan limit bilan dastlabki to\'lovsiz 0-12-20 muddatli to\'lovi. Ushbu muddatli to\'lovdan respublikamiz bo\'ylab 5 000 dan ortiq hamkor nuqtalarda foydalanishingiz mumkin.\n\nMuddatli to\'lovdan qanday do\'konlarda foydalanish mumkinligini esa uzumnasiya.uz veb-saytida va ijtimoiy tarmoqlardagi sahifalarimizda bilishingiz mumkin.:\n\nO\'zingizni qiziqtirgan bo\'limni tanlang:',
                     reply_markup=About_Tolov_menu)

@dp.message_handler(text='Qaysi do\'konlarda sizlar taqdim etayotgan muddatli to\'lovdan foydalansak bo\'ladi?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Siz uzum.uz marketpleysida yoki butun respublikamiz bo‘ylab hamkorlik tarmog’ida (5 000 hamkor nuqtalar) xaridlarni amalga oshirishingiz va xizmatlardan foydalanishingiz mumkin. Biz Mediapark, Elmakon, Artel, Radius, Idea, Mi-Store, Macbro, Just, Selfie, Bellstore, Adamari kabi do\'konlar bilan hamkorlik qilamiz va ko\'proq ma\'lumotni uzumnasiya.uz saytida hamda ijtimoiy tarmoqlardagi sahifalarimizda topishingiz mumkin:',
                     reply_markup=About_Tolov_menu)

@dp.message_handler(text='Uzum nasiya to\'lovi banki kreditdan nimasi bilan farq qiladi?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Nasiyada boshlang\'ich to\'lov yo\'q, shuningdek, bank kreditidan farqli ravishda to‘lovni kechiktirganlik uchun penya va jarimalar ham bo\'lmaydi.\n\nMahsulot yoki xizmatni muddatli to\'lovga sotib olayotganda mijoz oylik va umumiy to‘lov miqdorini, shuningdek, to‘lov muddatini aniq biladi. Shartlar shaffof bo\'ladi va shartnoma oxirigacha o\'zgarishsiz qoladi.\n\nKredit va nasiya o\'rtasidagi yana bir farq shundaki, xaridor kredit olish uchun ariza berish orqali bank bilan huquqiy munosabatlarni o\'rnatadi. Bank ushbu puldan foydalanganlik uchun qarz oluvchiga ma\'lum foiz stavkasi bo\'yicha pul mablag\'larini taqdim etadi va xaridor bu pul bilan darhol istalgan do\'konda xarid uchun to\'laydi.\n\nNasiya esa ushbu xizmat mavjud bo\'lgan sheriklar tarmog\'iga ega bo\'ladi. Sotib olayotganda, xizmat tanlangan do\'konda xaridor uchun to\'laydi, ya\'ni mablag\'lar to\'g\'ridan-to\'g\'ri xaridorga taqdim etilmaydi. O‘z navbatida, xaridor muddatli to\'lov xizmati mijoziga aylanadi va xarid uchun to\'lovni bo\'lib-bo\'lib amalga oshiradi.\nO\'zingizni qiziqtirgan bo\'limni tanlang',
                     reply_markup=About_Tolov_menu)



@dp.message_handler(text='Shartnoma')
async def send_menu(sms:types.Message):
    await sms.answer(text='O\'zingizni qiziqtirgan savollarni tanlang:',
                     reply_markup=Shartnoma)

@dp.message_handler(text='Qanday qilib ro\'yxatdan o\'tish va limitni olish mumkin?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Ro\'yxatdan o\'tish Uzum Nasiya ilovasida amalga oshiriladi, ilovani App Store yoki Play Market\'dan yuklab olish mumkin.\nTezkor ro\'yxatdan o\'tish uchun sizga quyidagilar kerak:\n1. Asosiy daromadga ega bank kartasiga SMS-xabar o\'rnatilgan telefon raqamini kiritish;2. Pasport/ID-kartangizning seriya raqami va tug\'ilgan sanangizni kiritish;3. Shaxsni tasdiqlash uchun yuzni skanerlash.\nUshbu bosqichdan muvaffaqiyatli o\'tsangiz, sizga avtomatik ravishda 5 000 000 so\'m limit taqdim etiladi. Ushbu limitni to\'liq ro\'yxatdan o\'tish orqali oshirish mumkin.\nBuning uchun sizga quyidagilar kerak:\n4. Plastik karta ma\'lumotlari va telefoningizga keladigan SMS-xabardagi kodni kiritish;5. Ikki yaqin kishining (ishonchli shaxslarning) aloqa ma’lumotlarini kiritish.\nTo‘lov qobiliyati tahlilidan kelib chiqib sizga asosiy limit doirasida 20 million so’mgacha hamda 0-0-3 tarifi bo\'yicha 5 million so‘mgacha limit taqdim etiladi.\nMuhim: Karta uchun SMS-xabarnoma ulangan telefon raqamingiz, shuningdek pasport va plastik karta egasi to\'liq mos kelishi kerak.\n\nO\'zingizni qiziqtirgan bo\'limni tanlang',
                     reply_markup=Shartnoma)

@dp.message_handler(text='Muddatli to\'lovni rasmiylashtirish uchun qanday talablar mavjud?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Uzum Nasiya tizimida ro\'yxatdan o\'tish uchun sizga quyidagilar kerak:\n\n- 22 yoshdan 65 yoshgacha bo\'lish;\n- pasport yoki ID-karta ma\'lumotlarini taqdim etish;\n- oxirgi 3 oy davomida oylik tushumga ega va oxirgi 4 oy ichida faol bo’lgan asosiy daromad kartasiga ega bo\'lish\n\nO\'zingizni qiziqtirgan bo\'limni tanlang',
                     reply_markup=Shartnoma)

@dp.message_handler(text='Muddatli to\'lov shartnomalari/to\'lov jadvali/qarz qoldig\'ini qayerda ko\'rishim mumkin?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Uzum Nasiya orqali rasmiylashtirilgan muddatli to\'lov shartnomalarini shaxsiy kabinetingizdagi "Shartnomalar" bo\'limida ko\'rishingiz mumkin. Siz tizimda ro\'yxatdan o\'tgan telefon raqamingiz orqali shaxsiy kabinetingizga kirishingiz mumkin.\n\nO\'zingizni qiziqtirgan bo\'limni tanlang',
                     reply_markup=Shartnoma)


@dp.message_handler(text='Shartnomani qanday bekor qilish mumkin?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Shartnomani bekor qilish uchun siz mahsulot yoki xizmatni sotib olgan hamkor nuqtaga murojaat qilishingiz va bekor qilish sababini ko\'rsatishingiz kerak. Pulni qaytarish hamkor do\'kon tomonidan belgilangan shartlarga muvofiq amalga oshiriladi.\n\nO\'zingizni qiziqtirgan bo\'limni tanlang',
                     reply_markup=Shartnoma)
    

@dp.message_handler(text='Xizmat bilan bog\'liq muammolar')
async def send_menu(sms:types.Message):
    await sms.answer(text='O\'zingizni qiziqtirgan savollarni tanlang:',
                     reply_markup=Muammolar)


@dp.message_handler(text='Nima uchun men bloklandim?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Tizim avtomatik ravishda muddatli to\'lov limitini belgilaydi.  Quyidagi hollarda rad javobini olishingiz mumkin:- oylik daromadingiz belgilangan minimal moqdordan kam bo\'lsa;- boshqa kredit tizimlarida muddati o\'tgan majburiyatlaringiz mavjud bo\'lsa;- boshqa do\'konlar va tizimlarda muddatli to\'lovga mahsulot xarid qilib o\'z vaqtida to\'lamagan bo\'lsangiz;- yosh chegarasi (22 yoshdan 65 yoshgacha) to\'g\'ri kelmasa;- avval ishlatilgan pasport ma\'lumotlari bilan yangi raqamdan qayta ro\'yxatdan o\'tishga harakat qilsangiz.\n\nKo\'p so\'raladigan savollar:',
                     reply_markup=Muammolar)
    

@dp.message_handler(text='Xizmatingizdan qanday foydalanishni tushunmadim?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Uzum Nasiya sizga tovar yoki xizmatlarni boshlang\'ich to\'lovsiz muddatli to\'lovga xarid qilishga yordam beradi. Bu xizmat yurtimiz bo\'ylab 5000 hamkor nuqtalarda mavjud.\n\nTezkor xaridlar uchun 0-0-3 tarifidan boshlang\'ich to‘lovsiz va ustamasiz 3 oy davomida foydalanishingiz mumkin. Katta xaridlar uchun esa 0-12-20 tarifidan 6 yoki 12 oyga dastlabki to\'lovsiz foydalanishingiz mumkin.\n\nKerakli mahsulot yoki xizmatlarni hamkor do\'konlarda yoki uzum.uz marketpleysida topishingiz va o‘zingizga ajratilgan muddatli to‘lov limitidan foydalangan holda xarid qilishingiz mumkin.\n\nO\'zingizni qiziqtirgan savollarni tanlang:\n\n',
                     reply_markup=Muammolar)
    

@dp.message_handler(text='Nima uchun uzum nasiya ilovasida mahsulotni korib bolmaydi?')
async def send_menu(sms:types.Message):
    await sms.answer(text='Uzum Nasiya tizimi ro\'yxatdan o\'tish va xaridlar uchun limit olishga mo\'ljallangan. Mahsulotlarni esa hamkorlarimizda yoki uzum.uz marketpleysida topishingiz mumkin.',
                     reply_markup=Muammolar)
    
@dp.message_handler(text='Men kartamni ulay olmayapman.')
async def send_menu(sms:types.Message):
    await sms.answer(text='Bunday holda, sizning to\'lov kartangiz:\n\n-aynan sizga tegishliligiga ishonch hosil qiling;\n\n- bu sizning asosiy daromadga ega plastik kartangiz bo’lishi kerak, aniqrog’i KREDIT, KORPORATIV, PENSIYA, STIPEDNIYA va shu kabi turdagi plastik kartalarni tizim qabul qilmaydi;\n\n- so\'nggi 6 oy ichida faol;\n\n- so\'nggi 4 oy davomida oylik tushimi aylanmasi kamida 1 mln so’mga teng bo’lishi kerak;\n\n',
                     reply_markup=Muammolar)
    

@dp.message_handler(text='Aloqa usullari')
async def send_menu(sms:types.Message):
    await sms.answer(text='Ko\'p so\'raladigan savollar:',
                     reply_markup=Aloqa)


@dp.message_handler(text='Operator bilan bog\'lanish.')
async def send_menu(sms:types.Message):
    await sms.answer(text='Biz bilan +998787771515 raqami orqali bog‘lanishingiz mumkin. Biz sizning barcha savollaringizga mamnuniyat bilan javob beramiz.',
                     reply_markup=Aloqa)


@dp.message_handler(text='Orqaga')
async def send_menu(sms:types.Message):
    await sms.answer(text='Ko\'p so\'raladigan savollar:',
                     reply_markup=Aloqa)


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
