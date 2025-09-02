"""

"""

from atm_app import islemler

hesap = {
    "isim": "Yavuz Yılmaz",
    "hesap_no": "12345678",
    "bakiye": 5000,
    "ek_hesap": 2000
}

while True:
    secim = input("""
    Lütfen bir seçim yapınız.
    ------------------------
    1-Bakiye Sorgula
    2-Para Yatır
    3-Para Çek
    4-Çıkış
    ------------------------
    """)
    if secim == "1":
        islemler.bakiye_sorgula(hesap)

    elif secim == "2":
        yatirilacak_miktar = float(input("Lütfen Yatırılacak Miktarı Giriniz:"))
        hesap = islemler.para_yatir(hesap, yatirilacak_miktar)

    elif secim == "3":
        cekilecek_miktar = float(input("Lütfen Çekilecek Miktarı Giriniz:"))
        hesap = islemler.para_cek(hesap, cekilecek_miktar)
    elif secim == "4":
        print("ATM işlemleri sonlandırıldı.")
        break
    else:
        print("Yanlış seçim yaptınız.tekrar deneyiniz.")
