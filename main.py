# Üzerinde çalışacağımız örnek liste
harfler = ['a', 'b', 'c', 'd', 'e', 'f']
# İndeksler: 0    1    2    3    4    5

ilk_harf = harfler[0]
print(f" ilk harf: {ilk_harf}")

ucuncu_harf = harfler[2]
print(f" ilk harf: {ucuncu_harf}")

orta_kisim = harfler[1:4]
print("1. ve 4. indeks arası:", orta_kisim)

bastaki_ve_sondaki_haric = harfler[1:5]
print(f"ilk ve son eleman hariç: {bastaki_ve_sondaki_haric}")

ilk_uc_eleman = harfler[:3]
print(f"ilk uc eleman: {ilk_uc_eleman}")

sondan_uc_eleman = harfler[3:]
print(f"sondan uc eleman: {sondan_uc_eleman}")

tum_elemanlar= harfler[:]
print(f"tum elemanlar: {tum_elemanlar}")

negatif_indeks_calisma = harfler[-3:-4]
print(f"negatif çalışma: {negatif_indeks_calisma}")

sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cift_sayilar = sayilar[::2]
print(f"cift sayilar: {cift_sayilar}")

tek_sayilar = sayilar[1::2]
print(f"tek sayilar: {tek_sayilar}")

tersten_sayilar = sayilar[::-1]
print(f"tersten sayilar: {tersten_sayilar}")

