alinacaklar_listesi = []
ogrenci_notlari = [85, 92, 78, 65, 100]
kisisel_bilgiler = ["Yavuz", 39, "Gümüşhane", True]
print("Boş liste:", alinacaklar_listesi)
print("Öğrenci notları:", ogrenci_notlari)
print("Kişisel bilgiler:", kisisel_bilgiler)
print("Öğrenci notları listesinin tipi:", type(ogrenci_notlari))

not_sayisi = len(ogrenci_notlari)
print(f"Öğrenci notu sayısı: {not_sayisi}")
alinacaklar_sayisi = len(alinacaklar_listesi)
print(f"Alınacaklar sayısı: {alinacaklar_sayisi}")

alinacaklar_listesi = ["peynir", "ekmek", "su"]
print(f"Alınacaklar listesi: {alinacaklar_listesi}")
print(f"Alınacaklar sayısı: {len(alinacaklar_listesi)}")

alinacaklar_listesi.append("süt")
print(f"Alınacaklar listesi: {alinacaklar_listesi}")
print(f"Alınacaklar sayısı: {len(alinacaklar_listesi)}")

alinacaklar_listesi.append("çay")
print(f"Alınacaklar listesi: {alinacaklar_listesi}")
print(f"Alınacaklar sayısı: {len(alinacaklar_listesi)}")
