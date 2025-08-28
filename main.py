# alıştırma 1
puanlar = [55, 67, 88, 75, 99, 45, 83]
print(f"ilk puan: {puanlar[0]}")
print(f"son puan: {puanlar[-1]}")
# print(f"11. eleman puan: {puanlar[10]}") IndexError: list index out of range hatası alırız. çünkü 10. indeks yok.


# alıştırma 2

yarismacilar = ["Ali", "Veli", "Ayşe", "Fatma", "Can", "Buse", "Zeynep"]

ilk_uc = yarismacilar[:3]
print(f"Yarışmayı ilk üç sırada bitirenler: {ilk_uc}")
son_uc = yarismacilar[-3:]
print(f"Yarışmayı son üç sırada bitirenler: {son_uc}")

print(f"Ayşe ve Fatma hariç diğer yarismacilar {yarismacilar[:2] + yarismacilar[-3:]}")

# alıştırma 3
karisik_veri = ["sensör_A", 2025, "ağustos", 28, 16, 45, 30.5, True, "OK"]

tarih_bilgisi = karisik_veri[1:4]
print(f"Tarih bilgisi: {tarih_bilgisi}")
saat_bilgisi = karisik_veri[-5:-3]
print(f"Saat bilgisi: {saat_bilgisi}")
karisik_veri_ters = karisik_veri[::-1]
print(f"Tersten liste: {karisik_veri_ters}")
bir_atlayarak_liste = karisik_veri[::2]
print(f"Listede bir atlayarak yazma: {bir_atlayarak_liste}")
