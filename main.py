#alıştırma 1
meyveler = ["elma", "muz", "karpuz", "kiraz"]
for meyve in meyveler:
    print(meyve)

for meyve in meyveler:
    print(f"Sepetteki meyve: {meyve}")

#alıştırma 2
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = []
for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print(f"Listedeki çift sayılar: {cift_sayilar}")

#alıştırma 3
secilen_sayi = int(input("1 ile 10 arasında bir sayı giriniz:\n"))
print(f"{secilen_sayi} için çarpım tablosu:")

for dongu_sayisi in range(1,11):
    sonuc = secilen_sayi * dongu_sayisi
    print(f"{secilen_sayi} x {dongu_sayisi} = {sonuc}")
