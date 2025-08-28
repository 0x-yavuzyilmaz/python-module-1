for sayi in range(5):
    print(sayi)

for sayi in range(1,5):
    print(sayi)

for _ in range(3):
    print("Merhaba!")

notlar = [85, 92, 78, 65, 100]
toplam = 0
for not_degeri in notlar:
    toplam= toplam + not_degeri
    print(f"Şu anki not: {not_degeri}, Toplam: {toplam}")

ortalama = toplam / len(notlar)
print(f"Notların toplamı: {toplam}")
print(f"Notların ortalaması: {ortalama}")

gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

for gun in gunler:
    print(f"Bugün günlerden {gun}")

print("Hafta içi bitti!")
