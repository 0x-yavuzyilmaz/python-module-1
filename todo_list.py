sonlandirici = None
yapilacaklar = [
    ["Pazar alışverişi yap", False],
    ["Projeyi tamamla", True],
    ["E-postaları cevapla", False]
]
"""
[ ] 1. Pazar alışverişi yap
[X] 2. Projeyi tamamla
[ ] 3. E-postaları cevapla
"""

while not sonlandirici:
    print(""" 
    --- YAPILACAKLAR LİSTESİ ---
1. Görevleri Göster
2. Görev Ekle
3. Görev Tamamla
4. Görev Sil
5. Çıkış
---------------------------""")

    secim = input("Lütfen bir seçim yapınız:\n")

    # Seçim "1" (Görevleri Göster):
    if secim == '1':
        if not yapilacaklar:
            print("Listenizde hiç görev yok.")
            break
        if yapilacaklar:
            sayac = 1
            for gorev in yapilacaklar:
                if gorev[1] == False:
                    tik = "[ ]"
                elif gorev[1] == True:
                    tik = "[X]"
                print(f"{tik} {sayac}. {str(gorev[0])}")
                sayac += 1

    # Seçim "2" (Görev Ekle):
    elif secim == '2':
        yeni_gorev = input("Lütfen eklemek isteyeceğiniz görevi giriniz: ")
        yapilacaklar.append([yeni_gorev, False])
        print("Görev başarıyla eklendi.")

    # Seçim "3" (Görev Tamamla):
    elif secim == '3':
        sira_no = int(input("Lütfen tamamlamak istediğiniz görecin sıra numarasını giriniz: "))
        gorev_indeks = sira_no - 1
        if gorev_indeks >= len(yapilacaklar):
            print("Hatalı görev no girdiniz")
        else:
            if yapilacaklar[gorev_indeks][1] == True:
                print("Görev zaten tamamlanmış gözüküyor!")
            else:
                yapilacaklar[gorev_indeks][1] = True

