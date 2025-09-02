def bakiye_sorgula(hesap: dict) -> None:
    print(f"Hesap Sahibi: {hesap['isim']}\nHesap No: {hesap['hesap_no']}"
          f"\nHesap Bakiyesi: {hesap['bakiye']} TL\n Ek Hesap Limiti: {hesap['ek_hesap']} TL")


def para_yatir(hesap: dict, yatirilacak_miktar: float) -> dict:
    if yatirilacak_miktar >= 0:
        hesap['bakiye'] = hesap['bakiye'] + yatirilacak_miktar
        print(f" İşlem Başarılı!\nYeni Hesap Bakiyesi: {hesap['bakiye']} TL")
        return hesap
    else:
        print("Geçersiz miktar.")
        return hesap


def para_cek(hesap: dict, cekilecek_miktar: float) -> dict:
    if cekilecek_miktar >= hesap['bakiye'] + hesap['ek_hesap']:
        print("Yetersiz Bakiye!")
        return hesap
    elif cekilecek_miktar <= hesap['bakiye']:
        hesap['bakiye'] = hesap['bakiye'] - cekilecek_miktar
        print(f"{cekilecek_miktar} TL hesabınızdan çekildi.\nYeni Hesap Bakiyesi: {hesap['bakiye']} TL ")
        return hesap
    else:
        son_ek_hesap_limiti = hesap['ek_hesap'] + hesap['bakiye'] - cekilecek_miktar
        hesap['ek_hesap'] = son_ek_hesap_limiti
        hesap['bakiye'] = 0
        print(f"{cekilecek_miktar} TL hesabınızdan çekildi.\nYeni Hesap Bakiyesi: {hesap['bakiye']} TL\n"
              f"Yeni Ek Hesap Bakiyesi: {hesap['ek_hesap']} TL ")
        return hesap
