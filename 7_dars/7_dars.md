# Guruh administratori

## Bot nima qiladi
Bot shaxsiy xabarlarda ham, guruh chatida ham yangilanishlar va
xabarlarni kuzatishi va tahlil qilishi mumkin. Bu funksiya bizga botdan
guruh administratori sifatida foydalanish imkoniyatini beradi.

## Ushbu videoda biz buni ko'rib chiqamiz.
Biz joylashuv va fotosuratlarni yuborishni ham ko'rib chiqamiz.

## Muhim eslatmalar!
Foydalanuvchiga kontent yuborish uchun `send_something()` funksiyasidan foydalaniladi,
uning `chat_id` argumenti bot xabar yuborishi kerak bo‘lgan **chat identifikatori**ni
bildiradi.

Agar biz foydalanuvchi "lichka"-siga xabar yubormoqchi bo'lsak, u holda
`message.from_user.id`-dan foydalanamiz, agar guruhga xabar yubormoqchi bo'lsak,
`message.chat.id`-dan foydalanamiz.

## `message.answer()`
Har doim foydalanuvchi xabar yuborgan joyga xabar yuboradi.

## `bot.send_photo()`
Bu usul **fotosurat** yuboradi.
```
chat_id = chat identifikatori
photo = fotosuratga havola
```
## `bot.send_location()`
Bu usul **joylashuv** yuboradi.
```
chat_id = chat identifikatori
latitude, longitude = kenglik, uzunlik
```