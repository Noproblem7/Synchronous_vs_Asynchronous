"""

Pythonda asinxron va sinxron dasturlash o'rtasidagi farqi:

Synchronous (sinxron):
Bloklash arxitekturasi: Sinxron kodda har bir operatsiya oldingisini bajarishga bog'liq.
Amalga oshirish ketma-ket amalga oshiriladi.
bitta tarmoq: bir vaqtning o'zida faqat bitta operatsiya ishlaydi.
Misol: Serverga bir so'rov yubdiz birinchi sorovni javobini olinishini kutamiz.

Asynchronous (Asinxron):
Bloklanmaydigan arxitektura: Async kod vazifalarni mustaqil ravishda bajarishga imkon beradi.
Amalga oshirish avvalgi vazifalarning bajarilishiga bog'liq emas.
Ko'p tarmoqli: operatsiyalar parallel ravishda bajarilishi mumkin.
Misol: Har bir javobni kutmasdan bir vaqtning o'zida serverga bir nechta so'rov yuborish.

Xulosa qilib aytganda, sinxron kod bosqichma-bosqich yondashuvga amal qiladi,
asinxron kod esa vazifalarni bir vaqtda bajarishga imkon beradi, bu esa samaradorlik va sezgirlikni oshiradi.

"""