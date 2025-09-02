# yardimci_fonksiyonlar.py

"""
Bu modül, ana program için çeşitli yardımcı ve yeniden kullanılabilir
fonksiyonları barındırır.
"""

from typing import List

def menuyu_goster() -> None:
    """
    Kullanıcıya yapılacaklar listesi için ana menüyü gösterir.

    Bu fonksiyon bir şey döndürmez, sadece menüyü ekrana yazdırır.
    """
    print("""
    --- YAPILACAKLAR LİSTESİ ---
    1. Görevleri Göster
    2. Görev Ekle
    3. Görev Tamamla
    4. Görev Sil
    5. Çıkış
    ---------------------------""")

def ortalama_hesapla(notlar: List[int]) -> float:
    """
    Bir tamsayı listesi alır ve elemanlarının aritmetik ortalamasını döndürür.

    Eğer liste boşsa, 0.0 değerini döndürerek ZeroDivisionError hatasını önler.

    Args:
        notlar (List[int]): Ortalaması alınacak tamsayıların listesi.

    Returns:
        float: Notların hesaplanan ortalaması.
    """
    if not notlar:
        return 0.0
    return sum(notlar) / len(notlar)