# Alıştırma 1 (Kolay): Sinema Salonu
sinema_koltuklari = [
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0]
]
print("En ön sıranın, en sağdaki koltuğunun durumunu:")
if sinema_koltuklari[0][3] == 1:
    print("Koltuk Dolu\n")
else:
    print("Koltuk Boş\n")
print("Orta sıranınikinci koltuğunun durumunu:")

if sinema_koltuklari[1][1] == 1:
    print("Koltuk Dolu\n")
else:
    print("Koltuk Boş\n")

# orta sıranın en son koltuğu doldu.
sinema_koltuklari[1][3] = 1

print(sinema_koltuklari[0])
print(sinema_koltuklari[1])
print(sinema_koltuklari[2])

# Alıştırma 2 (Orta Zorluk): Not Ortalamaları


sinif_listesi = [[80, 90, 100], [70, 75, 80], [95, 88, 92], [60, 65, 70]]
sira = 1
for ogrenci in sinif_listesi:
    notlar_toplami = sum(ogrenci)
    not_sayisi = len(ogrenci)
    ortalama = notlar_toplami / not_sayisi
    print(f" {sira}. öğrencinin not ortalaması: {ortalama:.2f}")
    sira = sira + 1

# Alıştırma 3 (İleri Seviye): Harita üzerinde "X" Bulma


harita = [["-", "-", "-"], ["-", "X", "-"], ["-", "-", "-"]]

for satir_indeksi in range(len(harita)):
    satir = satir_indeksi + 1
    hazine_bulundu = False
    for sutun_indeksi in range(len(harita[satir_indeksi])):
        sutun = sutun_indeksi + 1
        if harita[satir_indeksi][sutun_indeksi] == "X":
            print(f"Hazine {satir}. satır, {sutun}. sütunda bulundu")
            hazine_bulundu = True
            break

    if hazine_bulundu:
        break
else:
    print("Hazine bulunamadı")
