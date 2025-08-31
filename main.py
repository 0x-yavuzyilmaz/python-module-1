# Alıştırma 1
def kullanici_selamla(isim):
    mesaj = "Hoş geldin, "
    print(mesaj + ad)  # Dikkatli bak!


kullanici_selamla("Yavuz")

"""
Hatanın Tipi Nedir?
NameError:

--Hatanın Açıklaması Ne Diyor?
-name 'ad' is not defined
--Hata Tam Olarak Hangi Dosyanın Hangi Satırında Oluşuyor?
-line 3, in kullanici_selamla
--Sorunun Kök Nedeni Nedir? (Koddaki mantık hatası veya yazım hatası nedir?)
-Sorunun nedeni tanımlanmamış değişkeni kullanmak yani parametre olarak 'isim' değişkeni kullanmışken,
 fonksiyon içerisinde 'ad' değişkeni kullandık.
--Nasıl Düzeltilir?
- Fonksiyon içerindeki 'ad' değişkenini 'isim' olarak değiştireceğiz.
"""


# Alıştırma 2
def son_elemani_getir(liste):
    # Bu fonksiyon listenin son elemanını getirmeyi amaçlıyor
    # ama listenin uzunluğunu indeks olarak kullanıyor.
    return liste[len(liste) - 1]


harfler = ['a', 'b', 'c']
son_harf = son_elemani_getir(harfler)
print(son_harf)

"""
--Hatanın Tipi Nedir?
- IndexError:list index out of range
--Hata Tam Olarak Hangi Satırda Oluşuyor?
- line 27, in son_elemani_getir
--Sorunun Kök Nedeni Nedir? (Sıfır tabanlı indeksleme ile len() fonksiyonunun ilişkisini düşün.
  harfler listesinin uzunluğu 3 ise, geçerli en son indeks kaçtır?)
- Sorunun kök nedeni liste uzunluğu listenin son elemanı değildir. Onun 1 eksiğidir. Yani 22dir
--Nasıl Düzeltilir? (Doğru indeksi nasıl hesaplarız?)
- return liste[len(liste)-1] yaparak
"""


# Alıştırma 3:

def listeye_ekle(veri_listesi, eleman):
    # Fonksiyonu yazan kişi, listeye ekleme metodunun
    # 'add' olduğunu düşünmüş olabilir.
    veri_listesi.append(eleman)
    return veri_listesi


rakamlar = [1, 2, 3]
yeni_liste = listeye_ekle(rakamlar, 4)
print(yeni_liste)

"""
--Hatanın Tipi Nedir?
- AttributeError:
--Hatanın Açıklaması Ne Diyor? (Özellikle 'list' object has no attribute 'add' kısmı ne anlama geliyor?)
- 'list' object has no attribute 'add': yani 'list' nesnesinin .add adında bir özelliği/metodu olmadığını söylüyor
--Sorunun Kök Nedeni Nedir?
  veri_listesi.add(eleman) kısmı sorunun nedenidir.
--Doğru Metot Nedir ve Kod Nasıl Düzeltilir?
- doğru metod .append(eleman) olmalıdır.
"""
