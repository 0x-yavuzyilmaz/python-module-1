# Döngüyü Kırma: break
sayilar = [1, 5, 12, 15, 22, 30, 45]
for sayi in sayilar:
    print(f"Kontrol edilen sayi: {sayi}")
    if sayi == 22:
        print("Aranan sayı bulundu! Döngüden çıkılıyor.")
        break
    else:
        print("Sayı bulunamadı")

# Adımı Atlamak: continue

# Sadece çift sayıları toplayalım, tek sayıları pas geçelim.
sayilar = [1, 2, 3, 4, 5, 6, 7, 8]
toplam = 0

for sayi in sayilar:
    # Eğer sayı tek ise (2'ye bölümünden kalan 1 ise)...
    if sayi % 2 != 0:
        continue  # Bu adımı atla, aşağıdaki toplama işlemini yapma.

    # Bu satıra sadece sayı çift ise ulaşılır.
    toplam += sayi
    print(f"{sayi} eklendi. Yeni toplam: {toplam}")

print(f"Sonuç: Sadece çift sayıların toplamı = {toplam}")

sayilar = [1, 2, 3, 4, 5, 6, 7, 8]
toplam = 0
for sayi in sayilar:
    if sayi % 2 != 0:
        continue
    toplam = toplam + sayi
    print(f"{sayi} eklendi. Yeni toplam: {toplam}")

print(f"Listedeki çift sayılarn toplamı: {toplam}")

# Varlık Kontrolü: in Operatörü
izinli_kullanicilar = ["yavuz", "admin", "guest", "root"]

kullanici_adi = input("Kullanici adinizi giriniz: ").lower()

if kullanici_adi in izinli_kullanicilar:
    print("Giriş izni verildi")
else:
    print("Bu kullanıcı adı listede yok. Erişim reddedildi.")

# Listeden Eleman Silme


gorevler = ["e-postaları kontrol et", "raporu yaz", "toplantıya katıl", "kahve iç"]
print(f"Orijinal liste: {gorevler}")

gorevler.remove("raporu yaz")
print("'.remove()' sonrası:", gorevler)

biten_gorev = gorevler.pop()
print(f"Bitirilen ve listeden çıkarılan görev: {biten_gorev}")
print("'.pop()' sonrası:", gorevler)

ilk_gorev = gorevler.pop(0)
print(f"İptal edilen ilk görev: {ilk_gorev}")
print("'.pop(0)' sonrası:", gorevler)
