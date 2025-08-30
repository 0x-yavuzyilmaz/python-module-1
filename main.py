# Alıştırma 1 (Kolay): Basit Docstring Ekleme
def gecme_durumu_hesapla(vize_notu, final_notu):
    """ Vize ve final notu verilen bir öğrencinin dersi geçip geçmeyeceğini belirler"""
    ortalama = vize_notu * 0.4 + final_notu * 0.6
    if ortalama >= 50:
        return "Geçti"
    else:
        return "Kaldı"


help(gecme_durumu_hesapla)
print(gecme_durumu_hesapla.__doc__)


# Alıştırma 2 (Orta Zorluk): Detaylı Docstring Yazma

def gorevi_tamamla(gorevler_listesi, gorev_numarasi):
    """Görev listesindeki belirli bir görevi tamamlandı olarak işaretler.


    Bu fonksiyon, verilen görev numarasını (1 tabanlı) liste indeksine çevirir ve ilgili görevin tamamlanma durumunu
    True yapar.

    Args:
        gorevler_listesi:(list) Her elemanı [gorev_metni, durum] formatında olan iç içe görev listesi
        gorev_numarasi:(int): Tamamlanacak görevin kullanıcı tarafından görülen sıra numarası (1'den başlar).

    Returns:
        bool: İşlemin başarılı olup olmadığını belirten bir boolean değer. Eğer görev numarası geçerliyse True,
        geçersizse False döndürür.

    """

    indeks = gorev_numarasi - 1
    if indeks >= len(gorevler_listesi) or indeks < 0:
        return False
    else:
        # Eğer zaten tamamlandıysa uyar, değilse tamamlandı olarak işaretle
        if gorevler_listesi[indeks][1]:
            gorevler_listesi[indeks][1] = True
            return True


help(gorevi_tamamla)


# Alıştırma 3 (İleri Seviye): Mevcut Bir Fonksiyonu Belgeleme

def rapor_olustur(rapor_basligi, *bolumler, **ek_bilgiler):
    """Bir rapor taslağı oluşturur.

    Rapor başlığı ve kullanıcı tarafından eğer verilirse raporun bölümleri ile kullanıcının raporfda bulunmasını
    istediği ek bilgiler rapora eklenir.

    Args:
        rapor_basligi: (str) Raporun başlığını oluşturacak metin.
        *bolumler: (tuple) Raporun bölümlerini içeren tuple.Bu tuple'daki veriler for döngüsü ile başına '-'
        yazılarak sıralanır.
        **ek_bilgiler: (dict) Ek bilgileri içeren sözlük. Bu sözlükteki veriler for döngüsü ile anahtar: değer
        şeklinde yazılır.

    Returns:
        None: "Bu fonksiyon bir şey döndürmez.

    """
    print(rapor_basligi.upper())
    for bolum in bolumler:
        print(f"- {bolum}")
    if ek_bilgiler:
        print("-" * 20)
        print("Ek Bilgiler:")
        for anahtar, deger in ek_bilgiler.items():
            print(f"{anahtar.title()}: {deger}")


help(rapor_olustur)
