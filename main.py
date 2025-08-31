# Alıştırma 1 (Kolay): Kapsamları Gözlemleme

kullanici_adi = "Global Admin"


def lokal_test():
    kullanici_adi = "Lokal Kullanıcı"
    print(f"Fonksiyon içindeki kullanıcı: {kullanici_adi}")


lokal_test()
print(f"Fonksiyon dışındaki kullanıcı: {kullanici_adi}")

# ÇIKTI
# Fonksiyon içindeki kullanıcı: Lokal Kullanıcı
# Fonksiyon dışındaki kullanıcı: Global Admin

# Fonksiyon içindeki ve dışındaki çıktıların farklı olmasının sebebi local scope içerisinde 'kullanici_adi'
# değişkenin tanımlanmış olmasından kaynaklanır. Çünkü python önce fonksiyom içerisindeki tanımlamalara bakar
# eğer globalde olan bir değişken lokalde tanımlanmışsa onu kullanır.
# ama yine de kötü uygulama gölgeleme kusuru: Shadows name 'kullanici_adi' from outer scope

# Alıştırma 2

islem_sayaci = 0


def islem_yap_global():
    global islem_sayaci
    islem_sayaci += 1
    return islem_sayaci


print(f"1. sefer: {islem_yap_global()}")
print(f"2. sefer: {islem_yap_global()}")
print(f"3. sefer: {islem_yap_global()}")

islem_sayaci = 0
print("-" * 20)


def islem_yap_return(mevcut_sayac):
    mevcut_sayac += 1
    return mevcut_sayac


for i in range(3):
    islem_sayaci = islem_yap_return(islem_sayaci)
    print(islem_sayaci)

# ÇIKTI:
# 1. sefer: 1
# 2. sefer: 2
# 3. sefer: 3
# --------------------
# 1
# 2
# 3

# return yöntemi kesinlikle dah öngörülebilir. Çünkü diğer türlü daha önce fonksiyonun kaç kere çalıştığını
# bilemediğmiz durumlarda global değişkenin(islem_sayaci)' nin ne olduğu hakkında bir fikrimiz bulunmuyor.
# hataya çok açık.

CONFIG = ("production", "192.168.1.1", 8080)


def veritabani_baglan():
    print(f"{CONFIG[1]}:{CONFIG[2]} adresindeki veritabanına bağlanılıyor...")


def log_mesaji_yaz(mesaj):
    print(f"[{CONFIG[0]}] MODU: {mesaj}")


veritabani_baglan()
log_mesaji_yaz("Bağlantı başarılı!")

# global anahtar kelimesi kullanmamıza gerek kalmamasının sebebi bu tuple'saki değişkenler lokal scope da
# tanımlanmadığı için zaten fonksiyon içerisinden ulaşılabilir haldedir. Buradaki veriler tuple içerisinde
# olduğundan zaten değiştirilme imkanı da bulunmamaktadır.
