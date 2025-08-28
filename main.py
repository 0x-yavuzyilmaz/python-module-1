# Alıştırma 1

yasakli_kelimeler = ["reklam", "spam", "virüs", "bedava"]

cumle = "bu bir spam mail değil sadece bedava ürün tanıtımı"
kelimeler = cumle.split()
sayac = 0

for kelime in kelimeler:
    sayac += 1
    if kelime in yasakli_kelimeler:
        print(f"Yasaklı kelime tespit edildi: {kelime}")
        break
    if sayac == len(kelimeler):
        print("Yasaklı kelime bulunamadı")

# Alıştırma 2
veri_akisi = [10, 20, -5, 30, -15, 40, 50, -2]
pozitif_sayilar = []
toplam = 0
for sayi in veri_akisi:
    if sayi < 0:
        continue
    pozitif_sayilar.append(sayi)

for pozitif_sayi in pozitif_sayilar[:3]:
    toplam += pozitif_sayi

print("Pozitif Sayılar:", pozitif_sayilar)
print("Toplam:", toplam)

# Alıştırma 3
yapilacaklar = []
while True:
    gorev = input("\n Ne yapmak istersin? (ekle / sil / göster / çıkış):").lower()
    if gorev == "ekle":
        yapilacaklar.append(input("Eklenecek görevi yaz: "))
    elif gorev == "sil":
        silinecek_gorev = input("Silinecek görevi yaz: ")
        if silinecek_gorev in yapilacaklar:
            yapilacaklar.remove(silinecek_gorev)
        else:
            print("Böyle bir görev bulunamadı.")
    elif gorev == "göster":
        print(f"Yapılacaklar Listesi:\n {yapilacaklar}")
    elif gorev == "çıkış":
        print("Çıkış yapıldı.")
        break
    else:
        print("Geçersiz Seçim")
