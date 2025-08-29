# Alıştırma 1 (Kolay): İsim Kontrolü

isimler = ["", "Ali", "Veli", "", "Ayşe", ""]
for isim in isimler:
    if isim:
        print(f"Hoş geldin, {isim}!")

# Alıştırma 2 (Orta Zorluk): Alışveriş Sepeti Durumu

sepet = []

if not sepet:
    print("Sepetiniz şu anda boş.")

sepet.extend(["elma", "armut"])

if sepet:
    print("Sepetinizde ürünler var.")
    print("-" * 30)
    print("Sepetinizdeki ürünler:")
    for nesne in sepet:
        print(nesne.title())

# Alıştırma 3 (İleri Seviye): Oyun Başlatma Onayı

onay = None
while not onay:
    cevap = input("Oyuna başlamak için 'evet' veya 'hayır' yazın: ").lower()
    if cevap == "evet":
        onay = "başla"
    elif cevap == "hayır":
        onay = "iptal"
    else:
        print("Lütfen sadece 'evet' veya 'hayır' yazın.")

if onay == "başla":
    print("Oyun başlıyor!")
elif onay == "iptal":
    print("Oyun iptal edildi.")
