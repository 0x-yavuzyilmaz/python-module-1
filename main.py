# Alıştırma 1
sayac = 10
while sayac > 0:
    print(sayac)
    sayac -= 1
print("Fırlat!")

# Alıştırma 2
kullanici_girdisi = ""
while kullanici_girdisi.lower() != "çıkış":
    kullanici_girdisi = input("Bir mesaj yazın ('çıkış' yazarak programı sonlandırın):")
    if kullanici_girdisi.lower() != "çıkış":
        print(f"Tekrar ediliyor: {kullanici_girdisi}")
print("Döngü sonlandırıldı")

# Alıştırma 3

toplam = 0
while toplam < 50:
    eklenecek_sayi = int(input("Eklenecek bir sayı girin: : "))
    toplam += eklenecek_sayi
    print(f"Şu anki toplam: {toplam}")

print(f"Tebrikler! Toplam {toplam} oldu ve 50'yi geçtiniz. Oyun bitti.")
