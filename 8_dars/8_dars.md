# 8-dars

## Klaviatura nima?
Telegramdagi botlar ham xuddi shunday tarzda inson buyruqlari va
matnni tushunish uchun yaratilgan. Biroq, ba'zi hollarda, biz foydalanuvchiga
buyruqlarni yuborishni osonlashtirmoqchimiz yoki foydalanuvchining tanlovini
har biri tegishli klaviatura tugmalarida ifodalangan mumkin bo'lgan echimlar
to'plami bilan cheklashni xohlaymiz.

## Muhim eslatmalar!
Muloqot oynasiga o'rnatilgan har bir klaviatura **`ReplyKeyboardMarkup`** sinfining namunasidir va uning ichida biz ko'rsatgan tugmalar sonini o'z ichiga oladi.

Har bir tugma **`KeyboardButton()`** usuli yordamida o'rnatiladi, u
foydalanuvchi bajarishi mumkin bo'lgan ma'lum bir variantni belgilaydi.

## `KeyboardButton`
Klaviaturada ma'lum bir tugma nusxasini yaratishga imkon beruvchi Telegram API klassi. Matn parametri bilan. Ushbu parametrning qiymati bosilganda yuboriladi.
`text = str`

## `ReplyKeyboardRemove`
Ushbu sinfga qo'ng'iroq qilish joriy klaviaturani yopadi.
`remove_keyboard = True`