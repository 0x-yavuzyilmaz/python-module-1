# alıştırma 1
gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

print(f"Hafta içinde {len(gunler)} gün vardır.")

gunler.append("Cumartesi")
gunler.append("Pazar")

print(f"Haftada {len(gunler)} gün vardır.")

# alıştırma 2
favori_filmler = []

favori_filmler.append(input("Favori filmlerinizden birini yazın: "))
favori_filmler.append(input("Favori filmlerinizden birini yazın: "))
favori_filmler.append(input("Favori filmlerinizden birini yazın: "))
print(f"Favori film listeniz oluşturuldu:\n {favori_filmler}")
print(f"Listenizde toplam {len(favori_filmler)} tane film bulunmaktadır.")

# alıştırma 3

karisik_iste = []
karisik_iste.append(701)
karisik_iste.append("Liste çalışması")
karisik_iste.append("2.53")
karisik_iste.append(False)
karisik_iste.append(["fenerbahçe", "galatasaray"])

print(karisik_iste)
# listenin eleman sayısı 5 olmalı. çünkü listenin kendisi 1 elemandır. listenin içerisinde kaç eleman olduğu önemsizdir
print(f"Listedeki eleman sayısı: {len(karisik_iste)}")
