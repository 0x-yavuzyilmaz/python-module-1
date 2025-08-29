# Alıştırma 1 (Kolay): Sabit Veriler

ayarlar = ("2.1", "Türkçe", "Koyu")
print("Tuple'ın ikinci elemanı:", ayarlar[1])
# Bu verilerin herhangi bir şekilde değişmesini istemediğimiz için tuple veri tipi kullanılmalıdır.

# Alıştırma 2 (Orta Zorluk): Veri Yapısı Dönüşümleri


gunler_tuple = ("Pzt", "Sal", "Çar", "Per", "Cum")
gunler_liste = list(gunler_tuple)
gunler_liste.extend(["Cmt", "Pzr"])
yeni_tuple= tuple(gunler_liste)
print("Tuple'a yeni günlerin eklenmiş hali:\n", yeni_tuple)


# Alıştırma 3 (İleri Seviye): Değişmezliğin Sınırları


ogrenci_verisi = ("Ahmet Yılmaz", 22, ["Matematik", "Fizik"])
#ogrenci_verisi[1] = 23
#tuple veri tipi atamaya izin vermediğinden TypeError hatası aldık.

ogrenci_verisi[2].append("Kimya")
print(ogrenci_verisi)

#kod hata vermedi. Çünkü ogrenci_verisi[2].append("Kimya") dediğimizde artık tuple değil tuple içindeki liste elemanına
#erişmiş olduğumuzdan .append metodu çalışır.