# Alıştırma 1
def menuyu_goster():
    print("""
        --- YAPILACAKLAR LİSTESİ ---
    1. Görevleri Göster
    2. Görev Ekle
    3. Görev Tamamla
    4. Görev Sil
    5. Çıkış
    ---------------------------""")


menuyu_goster()
menuyu_goster()


# Alıştırma 2

def ortalama_hesapla(notlar_listesi):
    ortalama = sum(notlar_listesi) / len(notlar_listesi)
    print(f"Notların ortalaması: {ortalama}")


ogrenci1_notlari = [80, 90, 100]
ogrenci2_notlari = [65, 75, 50, 85]

ortalama_hesapla(ogrenci1_notlari)
ortalama_hesapla(ogrenci2_notlari)


# Alıştırma 3

def profil_karti_olustur(isim: str, dogum_yili: int, meslek: str):
    yas = 2025 - dogum_yili

    print(f"""
=========================
PROFİL KARTI
-------------------------
İsim    : {isim.title()}
Meslek  : {meslek.title()}
Yaş     : {yas}
=========================
    """)


profil_karti_olustur("Yavuz", 1986, "Matematik Öğretmeni")
profil_karti_olustur("Cemil", 1960, "emekli")
