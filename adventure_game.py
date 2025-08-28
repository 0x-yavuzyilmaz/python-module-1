# oyunun başlangıç kısmı
print("Macera Oyunumuza Hoşgeldin!\n")
print("""Gizemli bir odada uyanıyorsun.
Odada eski bir ahşap kapı ve üzerinde parlayan bir sandık var.
Kuzey duvarında ise küçük bir pencere asılı...
""")

eylem = input("Ne yapmak istersin? Hangi eşya ile başlayalım? Kapı, sandık, pencere?\n").lower()

# oyundaki if-elif-else karar yapısı
if eylem == "kapı":
    print("Kapı kilitli görünüyor. Belki bir anahtara ihtiyacın vardır.")
elif eylem == "sandık":
    print("Sandık da kilitli. Üzerinde küçük, paslı bir kilit var. Belki onu açacak bir şey bulabilirsin.")
elif eylem == "pencere":
    print("Pencereden dışarı baktığında sık bir orman görüyorsun. Pencerenin pervazında ise küçük, parlak bir anahtar "
          "duruyor!\n")
    anahtar_alindi_mi = input("Evet doğru yoldasın, sandığı açman için ne gerekiyor?\n").lower()
    if anahtar_alindi_mi == "anahtar":
        print("Anahtarı kullanarak sandığı açtın ve içinden bir levye çıktı!")
    else:
        print("Hayır.Sandık hala kilitli:(")
else:
    print(
        f"{eylem} ile ne yapacağımı bilmiyorum.Lütfen 'kapı', 'sandık' veya 'pencere' gibi nesnelerle etkileşime geç. ")
