import os
import time
import sys
from colorama import Fore

while True:
        os.system("clear")
        print(Fore.MAGENTA + """

---------------------------------------------------------------------
 ███████████    █████████   ██████   █████ █████   ████   █████████
░░███░░░░░███  ███░░░░░███ ░░██████ ░░███ ░░███   ███░   ███░░░░░███
 ░███    ░███ ░███    ░███  ░███░███ ░███  ░███  ███    ░███    ░███
 ░██████████  ░███████████  ░███░░███░███  ░███████     ░███████████
 ░███░░░░░███ ░███░░░░░███  ░███ ░░██████  ░███░░███    ░███░░░░░███
 ░███    ░███ ░███    ░███  ░███  ░░█████  ░███ ░░███   ░███    ░███
 ███████████  █████   █████ █████  ░░█████ █████ ░░████ █████   ████
░░░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░   ░░░░ ░░░░░   ░░░░░
---------------------------------------------------------------------

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
1) BANKAYA PARA YATIR
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2) BANKADAN PARA ÇEK
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
3) ARAÇ KİLOMETRESİ HESAPLA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
4) TOPLAMA İŞLEMİ YAP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
5) ÇIKARMA İŞLEMİ YAP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
6) ÇARPMA İŞLEMİ YAP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
7) BÖLME İŞLEMİ YAP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
8) MANAVDAN ALINACAK LİSTESİNİ HESAPLA
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
9) PROGRAMDAN ÇIK


""")

        secim = input("seç: ")
        def banka():
                os.system("clear")
                time.sleep(3)
                os.system("figlet BANKA")
                bakiye = 1000
                print(Fore.YELLOW + "GÜNCEL BAKİYE: " ,bakiye)
                time.sleep(0.5)
                print(Fore.RED + " BANKAYA PARA YATIR ")
                time.sleep(0.5)
                secim = int(input(Fore.YELLOW + "Bankaya ne kadar para yatırmak istersin: "))
                time.sleep(0.5)
                print(Fore.YELLOW + "Yatırılan para: " ,secim)
                time.sleep(0.5)
                toplam = bakiye + secim
                print(Fore.RED + "OLUŞAN BAKİYE DURUMU: " ,toplam)
                print(Fore.CYAN + "PROGRAMDAN 5 SANİYE İÇİNDE ÇIKILIYOR")
                time.sleep(5)
                os.system("clear")
        def banka1():
                os.system("clear")
                time.sleep(3)
                os.system("figlet BANKA")
                bakiye = 1000
                print(Fore.YELLOW + "GÜNCEL BAKİYE" ,bakiye)
                time.sleep(0.5)
                print(Fore.RED + "BANKADAN PARA ÇEK")
                time.sleep(0.5)
                secim = int(input(Fore.YELLOW + "Bankadan ne kadar para çekmek istersin: "))
                time.sleep(0.5)
                print(Fore.YELLOW + "Çekilen para: " ,secim)
                time.sleep(0.5)
                toplam = bakiye - secim
                print(Fore.RED + "OLUŞAN BAKİYE DURUMU: " ,toplam)
                time.sleep(0.5)
                print(Fore.CYAN + "PROGRAMDAN 5 SANİYE İÇİNDE ÇIKILIYOR" )
                time.sleep(5)
                os.system("clear")
        def km():
                os.system("clear")
                time.sleep(3)
                os.system("figlet KM")

                print(Fore.MAGENTA + """
                >İZMİR İÇİN YAKIT FİYATLARI<
                        V/Max Kurşunsuz 95 = 55 TL
                        Gazyağı = 46 TL
                        %1 Kükürtlü Fual Oil = 30 TL
                        V/Max Diesel = 55 TL
                        Kalorifer Yakıtı = 35 Tl
                        Otogaz = 27 TL""")
          
                secim1 = input(Fore.RED +"HANGİ ŞEHİRE GİDECEKSİN: ")
                time.sleep(2)
                secim2 = int(input(Fore.CYAN + "ARACINIZIN YOL ALDIĞI KİLOMETRE: "))
                time.sleep(2)
                secim3 = int(input(Fore.YELLOW + "ARACINIZ 100 KM DE KAÇ LİTRE YAKIYOR: "))
                time.sleep(2)
                secim4 = int(input(Fore.RED + "ARACINIZ HANGİ YAKIT TÜRÜNÜN FİYATI: "))
                time.sleep(2)

                print(Fore.RED + "GİDİLEN ŞEHİR: " ,secim1)
                time.sleep(1)
                print(Fore.CYAN + "YOL ALDIĞI KİLOMETRE:  " ,secim2)
                time.sleep(1)
                print(Fore.YELLOW + "100 KM DE YAKILAN LİTRE: " ,secim3)
                time.sleep(1)
                print(Fore.RED + "KULLANILAN YAKIT FİYATI")
                time.sleep(0.5)
                toplam = (secim2 // secim3) * secim4
                print(Fore.YELLOW + "OLUŞAN MASRAF > " ,toplam)
                time.sleep(0.5)
                print(Fore.RED + "PROGRAM KAPATILIYOR - 5 SANİYE İÇİNCE MENÜYE YÖNLENDİRİLECEKSİN...")
                time.sleep(5)

        def toplama():
                os.system("clear")
                time.sleep(0.5)
                os.system("figlet TOPLAMA")
                toplama = int(input(Fore.RED + "TOPLAYACAĞINIZ 1. SAYIYI GİRİN: " ))
                time.sleep(0.5)
                print(Fore.CYAN + "TOPLANAN 1. SAYI > " ,toplama)
                time.sleep(0.5)
                toplama1 = int(input(Fore.YELLOW + "TOPLAYACAĞINIZ 2. SAYIYI GİRİN: "))
                time.sleep(0.5)
                print(Fore.CYAN + "TOPLANAN 2. SAYI > " ,toplama1)
                islem = toplama + toplama1
                time.sleep(2)
                print(Fore.RED + "İŞLEMİN SONUCU" ,islem)
                print(Fore.MAGENTA + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                time.sleep(5)

        def cıkarma():
                os.system("clear")
                time.sleep(0.5)
                os.system("figlet CIKARMA")
                çıkarma = int(input(Fore.RED + "ÇIKARACAĞINIZ 1. SAYIYI GİRİN: "))
                time.sleep(0.5)
                print(Fore.CYAN + "ÇIKARILAN 1. SAYI > " ,çıkarma)
                time.sleep(0.5)
                çıkarma1 = int(input(Fore.YELLOW + "ÇIKARACAĞINIZ 2. SAYIYI GİRİN: "))
                time.sleep(0.5)
                print(Fore.CYAN + "ÇIKARILAN 2. SAYI > " ,çıkarma1)
                islem = çıkarma - çıkarma1
                time.sleep(2)
                print(Fore.RED + "İŞLEMİN SONUCU " ,islem)
                print(Fore.MAGENTA + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                time.sleep(5)

        def carpma():
                os.system("clear")
                time.sleep(0.5)
                os.system("figlet CARPMA")
                çarpma = int(input(Fore.RED + "ÇARPACAĞINIZ 1. SAYIYI GİRİN: "))
                time.sleep(0.5)
                print(Fore.CYAN + "ÇARPILAN 1. SAYI > " ,çarpma )
                time.sleep(0.5)
                çarpma1 = int(input(Fore.YELLOW + "ÇARPACAĞINIZ 2. SAYIYI GİRİN: "))
                time.sleep(0.5)
                print(Fore.CYAN + "ÇARPILAN 2. SAYI" ,çarpma1)
                islem = çarpma * çarpma1
                time.sleep(2)
                print(Fore.RED + "İŞLEMİN SONUCU " ,islem)
                print(Fore.MAGENTA + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                time.sleep(5)
          
        def bolme():
                os.system("clear")
                time.sleep(0.5)
                os.system("figlet BOLME")
                bölme = int(input(Fore.RED + "BÖLECEĞİNİZ 1. SAYIYI GİRİN : "))
                time.sleep(0.5)
                print(Fore.CYAN + "BÖLÜNEN 1. SAYI > " ,bölme)
                time.sleep(0.5)
                bölme1 = int(input(Fore.YELLOW + "BÖLÜNECEK 2. SAYIYI GİRİN: "))
                time.sleep(0.5)
                print(Fore.CYAN + "BÖLÜNEN 2. SAYI > " ,bölme1)
                islem = bölme // bölme1
                time.sleep(2)
                print(Fore.RED + "İŞLEMİN SONUCU " ,islem)
                print(Fore.MAGENTA + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                time.sleep(5)
          
        def manav_liste():
                os.system("clear")
                os.system("figlet MANAV")
                print(Fore.CYAN + """
                      1) PATATES > KİLOSU 30 TL
                      2) SOĞAN  > KİLOSU 20 TL
                      3) DOMATES > 25
                      4) PATLICAN > 15
                        """)
                secim_manav = input(Fore.YELLOW + "HANGİ ÜRÜNÜ ALMAK İSTERSİN: ")

                if secim_manav=="1":
                        time.sleep(0.5)
                        manav = int(input(Fore.YELLOW + "KAÇ KİLO PATATES ALMAK İSTERSİN: "))
                        time.sleep(0.5)
                        print(Fore.RED + "KİLO BAZINDA ALINAN PATATES > " ,manav)
                        toplam = 30 * manav
                        time.sleep(0.5)
                        print(Fore.MAGENTA + "OLUŞAN MASRAF > " ,toplam)
                        time.sleep(0.5)
                        print(Fore.CYAN + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                        time.sleep(5)
                elif secim_manav=="2":
                        time.sleep(0.5)
                        manav = int(input(Fore.YELLOW + "KAÇ KİLO SOĞAN ALMAK İSTİYORSUN: "))
                        time.sleep(0.5)
                        print(Fore.RED + "KİLO BAZINDA ALINAN SOĞAN > " ,manav)
                        time.sleep(0.5)
                        toplam = 20 * manav
                        print(Fore.MAGENTA + "OLUŞAN MASRAF > " ,toplam)
                        time.sleep(0.5)
                        print(Fore.CYAN + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                        time.sleep(5)

                elif secim_manav=="3":
                        time.sleep(0.5)
                        manav = int(input(Fore.YELLOW + "KAÇ KİLO DOMATES ALMAK İSTİYORSUN: "))
                        time.sleep(0.5)
                        print(Fore.RED + "KİLO BAZINDA ALINAN DOMATES > " ,manav)
                        time.sleep(0.5)
                        toplam = 25 * manav
                        print(Fore.MAGENTA + "OLUŞAN MASRAF > " ,toplam)
                        time.sleep(0.5)
                        print(Fore.CYAN + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                        time.sleep(5)

                elif secim_manav=="4":
                        time.sleep(0.5)
                        manav = int(input(Fore.YELLOW + "KAÇ KİLO PATLICAN ALMAK İSTİYORSUN: "))
                        time.sleep(0.5)
                        print(Fore.RED + "KİLO BAZINDA ALINAN PATLICAN > " ,manav)
                        time.sleep(0.5)
                        toplam = 15 * manav
                        print(Fore.MAGENTA + "OLUŞAN MASRAF > " ,toplam)
                        time.sleep(0.5)
                        print(Fore.CYAN + "İŞLEMİN BİTTİ 5 SANİYE İÇİNDE MENÜYE YÖNLENDİRİLECEKSİN...")
                        time.sleep(5)
                else:
                     print(Fore.RED + "YANLIŞ İŞLEM")

        def exit():
                sys.exit()

        if secim=="1":
                banka()
        elif secim=="2":
                banka1()
        elif secim=="3":
                km()
        elif secim=="4":
                toplama()
        elif secim=="5":
                cıkarma()
        elif secim=="6":
                carpma()
        elif secim=="7":
                bolme()
        elif secim=="8":
                manav_liste()
        elif secim=="9":
                exit()
