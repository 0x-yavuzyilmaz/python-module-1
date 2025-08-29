# Döngüyü sonlandırmak için kullanılan bayrak (None/1)
sonlandirici = None

# Yapılacaklar listesi: her eleman [görev_metni, tamamlandı_mı]
# tamamlandı_mı: False -> yapılmadı, True -> yapıldı
yapilacaklar = [
    ["Pazar alışverişi yap", False],
    ["Projeyi tamamla", True],
    ["E-postaları cevapla", False]
]

# Kullanıcı çıkış seçeneğini seçene kadar menüyü göstermeye devam et
while not sonlandirici:
    # Menü metni
    print(""" 
    --- YAPILACAKLAR LİSTESİ ---
1. Görevleri Göster
2. Görev Ekle
3. Görev Tamamla
4. Görev Sil
5. Çıkış
---------------------------""")

    # Kullanıcıdan seçim al
    secim = input("Lütfen bir seçim yapınız:\n")

    # Seçim "1" (Görevleri Göster):
    if secim == '1':
        # Eğer liste boşsa bilgi verip döngüyü tekrar başlat

        if not yapilacaklar:
            print("Listenizde hiç görev yok.")
            continue

        # Liste doluysa görevleri sırayla yazdır
        if yapilacaklar:
            sayac = 1  # ekrana sıra numarası için sayaç
            for gorev in yapilacaklar:
                # gorev[1] True ise tamamlandı, False ise tamamlanmadı
                if not gorev[1]:
                    tik = "[ ]"
                elif gorev[1]:
                    tik = "[X]"
                # Görevi tik işareti ve sıra no ile yazdır
                print(f"{tik} {sayac}. {str(gorev[0])}")
                sayac += 1

    # Seçim "2" (Görev Ekle):
    elif secim == '2':
        # Kullanıcıdan yeni görev metnini al
        yeni_gorev = input("Lütfen eklemek isteyeceğiniz görevi giriniz: ")
        # Yeni görev varsayılan olarak tamamlanmadı (False)
        yapilacaklar.append([yeni_gorev, False])
        print("Görev başarıyla eklendi.")

    # Seçim "3" (Görev Tamamla):
    elif secim == '3':
        # Tamamlanacak görevin sıra numarasını al
        # Not: int dönüşümü hatalı girişte ValueError fırlatabilir.
        sira_no = int(input("Lütfen tamamlamak istediğiniz görevin sıra numarasını giriniz: "))
        gorev_indeks = sira_no - 1  # liste indeksi = sıra no - 1

        # Geçersiz üst sınır kontrolü ve negatif indeks kontrolü
        if gorev_indeks >= len(yapilacaklar) or gorev_indeks < 0:
            print("Hatalı görev no girdiniz")
        else:
            # Eğer zaten tamamlandıysa uyar, değilse tamamlandı olarak işaretle
            if yapilacaklar[gorev_indeks][1]:
                print("Görev zaten tamamlanmış gözüküyor!")
            else:
                yapilacaklar[gorev_indeks][1] = True
                print(f"{sira_no}. görev tamamlandı olarak işaretlendi.")

    # Seçim "4" (Görev Sil):
    elif secim == '4':
        # Silinecek görevin sıra numarasını al

        sira_no = int(input("Lütfen silmek istediğiniz görevin sıra numarasını giriniz: "))
        gorev_indeks = sira_no - 1  # liste indeksi = sıra no - 1

        # Geçersiz üst sınır kontrolü ve negatif indeks kontrolü
        if gorev_indeks >= len(yapilacaklar) or gorev_indeks < 0:
            print("Hatalı görev no girdiniz")
        else:
            # İlgili görevi listeden çıkar
            yapilacaklar.pop(gorev_indeks)
            print(f"{sira_no}. görev başarıyla silindi")

    # Seçim "5"(Çıkış):
    elif secim == '5':
        # Döngü koşulunu false yapacak şekilde bayrağı değiştir
        print("Çıkış Yapılıyor")
        sonlandirici = 1

    # Geçersiz seçimler için uyarı
    else:
        print("Yanlış seçim yaptınız. Tekrar deneyiniz...")
