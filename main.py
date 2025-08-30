# Alıştırma 1 (Kolay): Alan Hesaplayıcı

def dikdortgen_alani_hesapla(kisa_kenar, uzun_kenar):
    return kisa_kenar * uzun_kenar


hesaplanan_alan = dikdortgen_alani_hesapla(5, 8)

print(f"Kenarları 5 ve 8 olan dikdörtgenin alanı: {hesaplanan_alan}")


# Alıştırma 2 (Orta Zorluk): Liste Analizi
def liste_analiz_et(sayi_listesi):
    if not sayi_listesi:
        return 0, 0
    else:
        return min(sayi_listesi), max(sayi_listesi)


rakamlar = [9, 1, 5, 22, 13, 8]

en_kucuk, en_buyuk = liste_analiz_et(rakamlar)

print(f"Listenin en küçük elemanı {en_kucuk}, en büyük elemanı {en_buyuk}.")


def gecme_durumu_hesapla(vize_notu, final_notu):
    ortalama = vize_notu * 0.4 + final_notu * 0.6
    if ortalama >= 50:
        return "Geçti"
    else:
        return "Kaldı"


sonuc = gecme_durumu_hesapla(50, 80)
print(f"Öğrencinin vizesi 50, finali 80 ise geçme durumu: {sonuc}")

# Aşağıdaki durum başarılı olacaktır.Çünkü gecme_durumu_hesapla(30, 40) -> "Kaldı" strinigini çıktı verecektir
# "Kaldı"=="Kaldı" True olacağından if bloku print("Test başarılı!") çalışaacaktır.
if gecme_durumu_hesapla(30, 40) == "Kaldı": print("Test başarılı!")
