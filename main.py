from typing import List, Tuple, Union


# Alıştırma 1
def dikdortgen_alani_hesapla(kisa_kenar: float, uzun_kenar: float) -> float:
    """Kenarları verilen bir dikdörtgenin alanını hesaplar.

    Kısa ve uzun kenarları float, cinsinden verilen dikdörgenin alanını return ile döndürür.

    Args:
        kisa_kenar ( float): Dikdörtgenin kısa kenarı
        uzun_kenar (float): Dikdörtgenin uzun kenarı

    Returns:
        float: dikdörtgenin alanını döndürür.

    """
    return kisa_kenar * uzun_kenar


print(dikdortgen_alani_hesapla(5, 5))
# çıktı:25
print(dikdortgen_alani_hesapla("beş", 10))  # uyarı: Expected type 'float', got 'str' instead


# çıktı:beşbeşbeşbeşbeşbeşbeşbeşbeşbeş

# Alıştırma 2

def liste_analiz_et(sayi_listesi: List[int]) -> Tuple[int, int]:
    """Verilen listedeki sayıların en küçük ve en büyük olanını döndürür.

    Verilen listedeki verilerin en küçük ve en büyük olanlarını sırasıyla döndürür.Eğer liste boş ise 0 ve 0
    değerlerini döndürür.

    Args:
        sayi_listesi(List[int]): En küçük ve en büyüğün bulunacağı sayıs listesi.Veriler int olmalıdır.

    Returns:
        Tuple[int,int]: En küçük ve en büyük veriyi sırasıyla int olarak döndürüt. Liste boş ise 0 ve 0 döndürür.

    """
    if not sayi_listesi:
        return 0, 0
    else:
        return min(sayi_listesi), max(sayi_listesi)


liste: List[int] = [10, 2, 88, -5]

minimum, maximum = liste_analiz_et(liste)
print(f"Listedeki en küçük sayı: {minimum}, en büyük sayı: {maximum}")

help(liste_analiz_et)


# Alıştırma 3


# Orijinal Hali
def gorevi_tamamla(gorevler_listesi: List[List[Union[str, bool]]], gorev_numarasi: int) -> Union[bool, None]:
    """Liste şeklinde tamamlancak görevler ve görev numarası verildiğinde verilen görevleri tamamlar.

    Liste şeklinde, bu listeninde string ve bool şeklinde bir listeden oluştuğunu göze alarak belirtilen görevi
    tamamlar ve True olarak döndürür. Eğer görev numarası yanlışsa None değeri döndürür.

    Args:
        gorevler_listesi(List[List[Union[str, bool]]]): Görev listesi bir listeden, bu listede Görev ve Görevin
        tamamlanıp tamamlanmadığını belirten True veya False değerlerinden oluşur.
        gorev_numarasi: Görev numarası tamsayıdan oluşur.

    Returns:
        bool veya None: Görev tamamlandıysa True, görev numarası hatalıysa None değeri

    """
    indeks = gorev_numarasi - 1
    if 0 <= indeks < len(gorevler_listesi):
        gorevler_listesi[indeks][1] = True
        return True
    else:
        return None  # Hata durumunda None döndürelim


yapilacaklar = [["Ekmek al", False], ["Sütü ısıt", False]]
print(gorevi_tamamla(yapilacaklar, 1))
