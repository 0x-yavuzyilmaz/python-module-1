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

print("Dosyayı değiştirdim.")