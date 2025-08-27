"""
Alıştırma 1 (Kolay): Sayı Tahmin Oyunu

Kodunun en başında, gizli_sayi adında bir değişken oluştur ve ona 1 ile 10 arasında aklından tuttuğun bir tam sayı
değeri ata (örn: gizli_sayi = 7). Kullanıcıya input() ile "1 ile 10 arasında bir sayı tahmin et: " diye sor.
Kullanıcının girdiği tahmini int() fonksiyonu ile tam sayıya çevir. Bir if yapısı kullanarak kullanıcının tahmininin
gizli_sayi'ya eşit olup olmadığını kontrol et. Eğer eşitse, ekrana "Tebrikler! Doğru tahmin ettin." yazdır. Eğer eşit
değilse (else bloğu), ekrana "Maalesef yanlış tahmin. Doğru sayı şuydu: [gizli_sayi]" yazdır.
"""
gizli_sayi = 7

tahmin = int(input("Lütfen gizli sayıyı tahmin ediniz:"))

if tahmin == gizli_sayi:
    print("Tebrikler! Doğru tahmin ettin.")
else:
    print(f" Maalesef yanlış tahmin. Doğru sayı şuydu: {gizli_sayi}")

"""
Alıştırma 2 (Orta Zorluk): Basit Bir Giriş (Login) Ekranı

Bu alıştırmada, önceden belirlenmiş bir kullanıcı adı ve şifreyi kontrol edeceğiz.

Programının başında dogru_kullanici_adi = "admin" ve dogru_sifre = "12345" şeklinde iki değişken tanımla. 
Kullanıcıdan sırasıyla kullanıcı adını ve şifresini input() ile al. Bir if koşulu ile hem girilen kullanıcı adının 
dogru_kullanici_adi'na hem de girilen şifrenin dogru_sifre'ye eşit olup olmadığını kontrol et. (İpucu: İki koşulu 
birden kontrol etmek için mantıksal and operatörünü kullanabilirsin: if kosul1 and kosul2:) Eğer ikisi de doğruysa, 
"Giriş başarılı!" yazdır. elif kullanarak, sadece kullanıcı adı doğru ama şifre yanlışsa, "Şifre hatalı!" yazdır. 
elif kullanarak, kullanıcı adı yanlış ama şifre doğruysa (bu pek olası bir senaryo olmasa da pratiğimiz için 
yapalım), "Kullanıcı adı hatalı!" yazdır. else kullanarak, ikisi de yanlışsa, "Kullanıcı adı ve şifre hatalı!" 
yazdır.
"""
dogru_kullanici_adi = "admin"
dogru_sifre = "12345"

kullanici_adi = input("Lütfen kullanıcı adı giriniz: ")
sifre = input("Lütfen şifre giriniz: ")

if kullanici_adi == dogru_kullanici_adi and sifre == dogru_sifre:
    print("Giriş Başarılı!")
elif kullanici_adi == dogru_kullanici_adi and sifre != dogru_sifre:
    print("Şifre hatalı!")
elif kullanici_adi != dogru_kullanici_adi:  # Şifrenin doğru/yanlış olmasına bakmaksızın kullanıcı adı yanlışsa...
    print("Kullanıcı adı hatalı!")
# Bu versiyonda 'else' bloğuna pek ihtiyaç kalmıyor, ama istersen genel bir hata için eklenebilir.

"""
Kullanıcıdan input() ile kilosunu kilogram cinsinden (örn: 75.5) ve boyunu santimetre cinsinden (örn: 180) al. 
Aldığın kilo değerini float()'a, boy değerini ise int()'e çevir. Santimetre olarak aldığın boyu 100'e bölerek metreye 
çevir (örn: 180 -> 1.8). Bu yeni değeri boy_metre adında bir değişkende sakla. VKİ'yi vki = kilo / (boy_metre * 
boy_metre) formülüyle hesapla. Hesapladığın vki değerine göre, aşağıdaki koşulları if/elif/else yapısıyla kontrol 
ederek ekrana uygun mesajı yazdır: Eğer VKİ 18.5'ten küçükse: "Zayıf" Eğer VKİ 18.5 ile 24.9 arasındaysa: "Normal 
kilolu" Eğer VKİ 25 ile 29.9 arasındaysa: "Fazla kilolu" Eğer VKİ 30 ile 39.9 arasındaysa: "Obez" Eğer VKİ 40 veya 
daha yüksekse: "İleri derecede obez (morbid obez)
"""

agirlik_kg = float(input("Lütfen ağırlığınızı giriniz:"))
boy_cm = int(input("Lütfen boyunuzu giriniz:"))
boy_m = boy_cm / 100

vki = agirlik_kg / (boy_m * boy_m)

if vki < 18.5:
    print("Zayıf")
# elif vki >= 18.5 and vki < 25: # Bu şekilde de yazılabilir, ama...
elif vki < 25:  # Python yukarıdan aşağı kontrol ettiği için, bu satıra geldiyse zaten 18.5'ten küçük OLMADIĞI
    # kesindir. Bu yüzden sadece üst sınırı kontrol etmek yeterlidir.
    print("Normal")
elif vki < 30:  # Bu satıra geldiyse zaten 25'ten küçük değildir.
    print("Fazla kilolu")
elif vki < 40:  # Bu satıra geldiyse zaten 30'dan küçük değildir.
    print("Obez")
else:  # Geriye kalan tek durum 40 veya daha büyük olmasıdır.
    print("İleri derecede obez (morbid obez)")
