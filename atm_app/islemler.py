"""
Atm işlemleri için gerekli olan "bakiye sorgulama", "para çekme", "para yatırma" fonksiyonları modülü.
"""


def bakiye_sorgula(hesap: dict) -> None:
    """ Sözlük olarak tanımlanmış kullanıcı verilerinden bakiye sorgular.

    Sözlük olarak belirlenmiş. İçerisinde "isim" ,"hesap_no" ,"bakiye, "ek hesap bakiye" gibi verilerin bulunduğu
    sözlükten bu verileri alır ve ekrana bir düzenle yazdırır.


    Args:
        hesap(dict): hesap bilgilerini bulunduran sözlük.

    Returns:
        None: Fonksiyon bir veri döndürmez. ekrana bilgileri yazdırır.
    """

    print(f"Hesap Sahibi: {hesap['isim']}\nHesap No: {hesap['hesap_no']}"
          f"\nHesap Bakiyesi: {hesap['bakiye']} TL\nEk Hesap Limiti: {hesap['ek_hesap']} TL")


def para_yatir(hesap: dict, yatirilacak_miktar: float) -> dict:
    """Hesaba para yatırma işlemlerini gerçekleştirir.

    Hesaba yatıralacak miktarı float olarak alır. Sonra bu miktarı önce ek hesaba yatırır. ardından kalırsa normal
    bakiye hesabına yatırır. Hem yeni hesap değerlerini döndürür. HEm hesap değerlerini ekrana yazdırır.

    Args:
        hesap(dict): hesap bilgilerini bulunduran sözlük.
        yatirilacak_miktar: Yatırılacak miktarın float veritipinde TL olarak değeri

    Returns:
        dict: Para yatırma işlemi sonundaki yeni hesap değerlerini döndürür.

    """
    if yatirilacak_miktar >= 0:
        if hesap['ek_hesap'] == 2000:
            hesap['bakiye'] = hesap['bakiye'] + yatirilacak_miktar
        else:
            if yatirilacak_miktar <= (2000 - hesap['ek_hesap']):
                hesap['ek_hesap'] = hesap['ek_hesap'] + yatirilacak_miktar
            else:
                hesap['ek_hesap'] = 2000
                hesap['bakiye'] = yatirilacak_miktar - 2000

        print(f" İşlem Başarılı!\n {yatirilacak_miktar} TL hesabınıza yatırıldı."
              f"\nYeni Hesap Bakiyesi: {hesap['bakiye']} TL\n"
              f"Ek Hesap Bakiyesi: {hesap['ek_hesap']} TL ")
        return hesap
    else:
        print("Geçersiz miktar.")
        return hesap


def para_cek(hesap: dict, cekilecek_miktar: float) -> dict:
    """Hesaptan para çekme işlemlerini gerçekleştirir.

    Hesaptan çekilecek miktarı float olarak alır. Bakiye yeterliyse bu miktarı ana bakiyeden karşılar.
     Ana bakiye yetersizse ek bakiyeden karşılar. her ikisi birden yetersizse "Bakiye Yetersiz Uyarısı" verir
     Hem yeni hesap değerlerini döndürür. HEm hesap değerlerini ekrana yazdırır

    Args:
        hesap(dict): hesap bilgilerini bulunduran sözlük.
        cekilecek_miktar: Çekilecek miktarın float veritipinde TL olarak değeri

    Returns:
        dict: Para cekme işlemi sonundaki yeni hesap değerlerini döndürür.
    """
    if cekilecek_miktar > (hesap['bakiye'] + hesap['ek_hesap']):
        print("Yetersiz Bakiye!")
        return hesap
    elif cekilecek_miktar <= hesap['bakiye']:
        hesap['bakiye'] = hesap['bakiye'] - cekilecek_miktar
        print(f"{cekilecek_miktar} TL hesabınızdan çekildi.\nYeni Hesap Bakiyesi: {hesap['bakiye']} TL\n"
              f"Ek Hesap Bakiyesi: {hesap['ek_hesap']} TL ")
        return hesap
    else:
        son_ek_hesap_limiti = hesap['ek_hesap'] + hesap['bakiye'] - cekilecek_miktar
        hesap['ek_hesap'] = son_ek_hesap_limiti
        hesap['bakiye'] = 0
        print(f"{cekilecek_miktar} TL hesabınızdan çekildi.\nYeni Hesap Bakiyesi: {hesap['bakiye']} TL\n"
              f"Yeni Ek Hesap Bakiyesi: {hesap['ek_hesap']} TL ")
        return hesap
