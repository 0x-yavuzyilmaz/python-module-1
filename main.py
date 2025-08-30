# # Alıştırma 1 (Kolay): Ortalama Bulucu
def ortalama_hesapla(*sayilar):
    if not sayilar:
        return 0
    else:
        return sum(sayilar) / len(sayilar)


print(f"Sayıların aritmetik ortalması: {ortalama_hesapla():.2f}")
print(f"Sayıların aritmetik ortalması: {ortalama_hesapla(10, 20, 30):.2f}")
print(f"Sayıların aritmetik ortalması: {ortalama_hesapla(1, 2, 3, 4, 5, 6, 7):.2f}")


# Alıştırma 2 (Orta Zorluk): Detaylı Rapor Oluşturucu

def rapor_olustur(rapor_basligi, *bolumler, **ek_bilgiler):
    print(rapor_basligi.upper())
    print(f"--- BÖLÜMLER---")
    for bolum in bolumler:
        print(f"-{bolum}")
    print("-" * 20)

    if ek_bilgiler:
        for anahtar, deger in ek_bilgiler.items():
            print(f"{anahtar.title()}: {deger}")


rapor_olustur(
    "Aylık Satış Raporu",
    "Giriş: Bu rapor, son ayın satış verilerini özetlemektedir.",
    "Gelişme: Satışlarda %15'lik bir artış gözlemlenmiştir.",
    "Sonuç: Büyüme trendi devam etmektedir.",
    yazar="Yavuz Yılmaz",
    tarih="2025-08-30",
    versiyon="1.1"
)


# Alıştırma 3 (İleri Seviye): Fonksiyon Fabrikası

def detayli_selamlama(isim, unvan=""):
    if unvan:
        print(f"Hoş geldiniz, {unvan} {isim}!")
    else:
        print(f"Merhaba, {isim}!")


def guvenli_cagirici(hedef_fonksiyon, *args, **kwargs):
    print("Çağrı yapılıyor...")
    hedef_fonksiyon(*args, **kwargs)
    print("Çağrı tamamlandı.")


guvenli_cagirici(detayli_selamlama, "Ali")
guvenli_cagirici(detayli_selamlama, "Ayşe", unvan="Dr.")
