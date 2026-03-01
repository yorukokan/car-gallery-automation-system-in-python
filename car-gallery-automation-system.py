# Ad         : Okan
# Soyad      : Yoruk
# Ogrenci No : 22100011067


# FINAL PROJESİ | OTOMASYON ODEVI

# Araclar Icin Liste ve Baslangic ID'si Tanimlaniyor .
arac_liste=[]
arac_id=1

# Menu Kısmini Yazdiriliyor .
def ana_menu():
    print("\n" * 20)
    print("\n------------------------------- ")
    print("|-->       ANA  MENU       <--| ")
    print("------------------------------- ")
    print("1- Arac Kayit Ekleme                    .")
    print("2- Arac Kaydi Listeleme                 .")
    print("3- Arac Kaydi Silme                     .")
    print("4- Arac Kaydi Guncelleme                .")
    print("5- Arac Kaydi Arama                     .")
    print("6- Arac Istatistikleri                  .")
    print("7- Belirli Fiyat Araliginda Araba Bulma .")
    print("0- Cikis .\n")

    # Menuden Yapilacak İslem Seciliyor .
    try:
        fonksiyonSecim=input("Bir Secim Yapiniz :")
        fonksiyonSecim=int(fonksiyonSecim)
        return fonksiyonSecim # Secilen Islem menu() Fonksiyonuna Gonderiliyor .
    except ValueError:
        print("Hatali Secim Yapildi !.")
        print("Ana Menuye Donuluyor ...")
        return -1
# Eklenen Arac Kayitlarini Dosyaya Ekliyor ve Saklaniyor .
def aracKayitDosyalama():

    with open("22100011067.txt", "w") as dosya: # '22100011067.txt' Adinda Dosya Aciliyor ve Listede Tutulan Araclar Icine Ekleniyor .
        for arac in arac_liste:
            dosya.write(f"ID    :{arac['id']}\n")
            dosya.write(f"Marka : {arac['marka']}\n")
            dosya.write(f"Model : {arac['model']}\n")
            dosya.write(f"Renk  : {arac['renk']}\n")
            dosya.write(f"Yil   : {arac['yil']}\n")
            dosya.write(f"Fiyat : {arac['fiyat']}\n")
            dosya.write("\n")
            dosya.write("--------------------------\n")
# Arac Kayitlarinin Silinmesini Onluyor ve Programa Girildiginde Arac Kayitlarini Yukleniyor .
def aracDosyadanOkuma():
    global arac_liste,arac_id # Global Degisken Tanimlaniyor .

    try:
        # '22100011067.txt' Dosyasi Okunuyor ve Programa Isleniyor .
        with open("22100011067.txt", "r") as dosya:
            icKisim=dosya.read().strip() # Dosya Icerigindeki Bosluklar Siliniyor .

            # Dosya Bos Degilse Isleme Devam Ediliyor .
            if icKisim:
                # Kayitlar Bu Cizgiye Gore Bolunuyor .
                aracKayitlari=icKisim.split("--------------------------\n")

                # Kayitlar Satirlara Bolunuyor .
                for kayit in aracKayitlari:
                    satirBolumu=kayit.strip().split("\n")

                    # Kayitlar Esleniyor ve Arac Sozlugune Bilgiler Kaydediliyor .
                    if len(satirBolumu)>=6:
                        arac={"id": int(satirBolumu[0].split(":")[1].strip()),
                            "marka":satirBolumu[1].split(":")[1].strip(),
                            "model":satirBolumu[2].split(":")[1].strip(),
                            "renk":satirBolumu[3].split(":")[1].strip(),
                            "yil":satirBolumu[4].split(":")[1].strip(),
                            "fiyat":satirBolumu[5].split(":")[1].strip()}
                        # Arac Listesine Araclar Ekleniyor .
                        arac_liste.append(arac)

                # Yeni Eklenecek Araclar Icin ID Olusturuluyor .
                arac_id=len(arac_liste)+1

    # Eger '22100011067.txt' Dosyasi Bulunamiyorsa Hata Sistemi Calisiyor .
    except FileNotFoundError:
        print("Arac Kayit Dosyasi Bulunamadi !.")
# Otomasyona Arac Kaydi Ekleniyor .
def aracKayitEkle():

    # Global Degiskenler Tanimlaniyor .
    global arac_liste,arac_id
    print("\nArac Kayit Ekleme Bolumune Hosgeldiniz .\n")
    while True:
          # Arac Bilgileri Giriliyor .
          marka=input("Arac Markasi Giriniz  :")
          model=input("Arac Modelini Giriniz :")
          renk =input("Arac Rengini Giriniz  :")
          yil  =input("Arac Yilini Giriniz   :")
          fiyat=input("Arac Fiyatini Giriniz :")

          # Arac Bilgileri yeni_arac Sozlugune Ekleniyor .
          yeniArac={"id":arac_id,"marka":marka,"model":model,"renk":renk,"yil":yil,"fiyat":fiyat}

          # arac_liste'ye Yeni Arac Ekleniyor .
          arac_liste.append(yeniArac)
          # Arac Bilgilerini Kaydetmek Icin Fonksiyon Cagiriliyor .
          aracKayitDosyalama()
          print("Araciniz Eklendi .")
          print(f"Arac ID'si : {arac_id}\n")

          # ID artiriliyor .
          arac_id+=1

          print("\nLutfen Belirtilen Secimlerden Birini Yapiniz .")
          aSecim=(input("Yeni Arac Eklemek Icin [y] , Cikis Icin [c] :"))
          # Kullanici'ya Secim Yaptiriliyor .
          if aSecim=="y":
              # Arac Eklemek Istedigi Icin Donguye Devam Ediliyor .
              continue
          elif aSecim=="c":
              # Donguden Cikis Yapiliyor .
              print("\nArac Kayit Ekleme Bolumunden Cikis Yapildi .\n")
              print("Ana Menuye Yonlendiriliyorsunuz ...")
              break
# Arac Kayitlarini Listeliniyor .
def aracKayitListele():

    # Global Degiskenler Tanimlaniyor .
    global arac_liste
    # Arac Kaydi Yok Ise Gerekli Bilgilendirme Yapiliyor .
    if not arac_liste:
        print("Kayitli Arac Bulunamadi !.")
    # Arac Kayitlari Listeleniyor .
    else:
        print("Arac Kayitlari Listeleniyor ...")
        print("--------------------------")

        # Liste Icerisindeki Her Arac Icin Bilgiler Yaziliyor .
        for arac in arac_liste:
            print(f"ID    :{arac['id']}")
            print(f"Marka :{arac['marka']}")
            print(f"Model :{arac['model']}")
            print(f"Renk  :{arac['renk']}")
            print(f"Yil   :{arac['yil']}")
            print(f"Fiyat :{arac['fiyat']}")
            print("--------------------------\n")
# Arac Kaydini Siliniyor .
def aracKayitSil():

    # Global Degiskenler Tanimlaniyor .
    global arac_liste,arac_id
    print("Arac Kayit Silme Bolumune Hosgeldiniz .\n")
    # Arac Kaydi Yok Ise Gerekli Bilgilendirme Yapiliyor .
    if not arac_liste:
        print("Kayitli Arac Bulunamadi !.")
        return

    while True:
        # Arac Kayitlari Listeleniyor .
        aracKayitListele()

        # Kullanicidan Silinecek Arac Icin Secim Yaptiriliyor .
        try:
            sil_id=int(input("Silmek Istediginiz Arac ID'sini Giriniz :"))
            sil_arac=None
            # Listede Silinecek Arac Araniyor .
            for arac in arac_liste:
                if arac['id']==sil_id:
                    sil_arac=arac
                    break
            # Arac Bulunduysa Listeden Kaldiriliyor .
            if sil_arac!=None:
                arac_liste.remove(sil_arac)
                # Arac ID'leri Tekrar Duzenleniyor .
                for i in range(len(arac_liste)):
                    arac_liste[i]["id"]=i+1
                # Guncellenmis ID'lere Gore Son ID Belirleniyor .
                arac_id=len(arac_liste)+1
                # Arac Bilgileri Dosyaya Kaydediliyor .
                aracKayitDosyalama()
                print(f"\n{sil_arac['marka']} {sil_arac['model']} Arac Kaydi Silindi !.")
                break
            else:
                # Eger Girilen ID'ye Sahip Bir Arac Yoksa Hata Mesaji Gösteriliyor .
                print("\nHatali Arac ID'si Girildi .")
                devamSecim=input("Arac ID'sini Tekrar Girmek İster Misiniz ? [E(Evet)/H(Hayır) :")
                # Tekrar ID'yi Girmek Istedigi Soruluyor .
                if devamSecim.lower() != "e":
                    break
        except ValueError:
            # Gecersiz Deger Giris Yapilirsa Hata Mesaji Gosteriliyor .
            print("\nHatali Secim Yapildi !.")
            print("Lutfen Arac ID'sini Tekrar Giriniz .")
# Kayitli Araclarin Bilgilerini Guncelliniyor .
def aracKayitGuncelle():

    # Global Degiskenler Tanimlaniyor .
    global arac_liste
    print("Arac Kayit Guncelleme Bolumune Hosgeldiniz .\n")
    # Arac Kaydi Yok Ise Gerekli Bilgilendirme Yapiliyor .
    if not arac_liste:
        print("Kayitli Arac Bulunamadi !.")
        return
    else:
        # Arac Kayitlari Listeleniyor .
        aracKayitListele()
        while True:
            try:
                # Kullanicidan ID Secimi Yaptiriliyor .
                guncellemeId=int(input("Guncellenecek Arac ID'sini Giriniz :"))
                guncellemeArac=None
                # Girilen ID Listede Araniyor .
                for arac in arac_liste:
                    if arac["id"]==guncellemeId:
                        guncellemeArac=arac
                        break
                # Arac ID'si Bulunduysa Guncelleme Ekrani Gosteriliyor .
                if guncellemeArac!=None:
                    while True:
                        print("\nArac Guncelleme Menusu .")
                        print("1- Marka.")
                        print("2- Model.")
                        print("3- Renk .")
                        print("4- Yil  .")
                        print("5- Fiyat.")
                        print("0- Guncelle ve Kaydet .\n")

                        try:
                            # Guncellemek Istenilen Bilgi Seciliyor .
                            gSecim=int(input("Guncellemek Istediginiz Bilgiyi Seciniz :"))

                            if gSecim==1:
                                guncellemeArac["marka"] = input(f"Yeni Marka ({guncellemeArac["marka"]}): ") or guncellemeArac["marka"]
                            elif gSecim==2:
                                guncellemeArac["model"] = input(f"Yeni Model ({guncellemeArac["model"]}): ") or guncellemeArac["model"]
                            elif gSecim==3:
                                guncellemeArac["renk"] = input(f"Yeni Renk ({guncellemeArac["renk"]}): ") or guncellemeArac["renk"]
                            elif gSecim==4:
                                guncellemeArac["yil"] = input(f"Yeni Yil ({guncellemeArac["yil"]}): ") or guncellemeArac["yil"]
                            elif gSecim==5:
                                guncellemeArac["fiyat"] = input(f"Yeni Fiyat ({guncellemeArac["fiyat"]}): ") or guncellemeArac["fiyat"]
                            elif gSecim==0:
                                # Guncelleme ve Kaydetme Secilir Ise Cikis Yapiliyor .
                                break
                            else:
                                print("Hatali Secim Yapildi !.")

                        except ValueError:
                            # Gecersiz Deger Girilirse Hata Mesaji Gosteriliyor .
                            print("Hatali Secim Yapildi .")
                            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")

                    # Guncellenen Arac Dosyaya Ekleniyor .
                    aracKayitDosyalama()
                    print("\nArac Bilgileri Guncellendi .")
                    print("Ana Menuye Donuluyor ...")
                    break
                else:
                    # Tekrar ID'yi Girmek Istedigi Soruluyor .
                    print("Hatali Arac ID'si Girildi .")
                    devamSecim=input("Arac ID'sini Tekrar Girmek İster Misiniz ? [E(Evet)/H(Hayır) :")
                    if devamSecim.lower()!="e":
                        break
            except ValueError:
                # Gecersiz Deger Girildiyse Hata Mesaji Gosteriliyor .
                print("Hatali Secim Yapildi .")
# Belirli Fiyat Araliginda Araclari Bulunuyor ve Listeliniyor .
def aracFiyatAraligi():

    print("Arac Fiyat Araligina Gore Arama Bolumune Hosgeldiniz .")

    try:
        # Max ve Min Fiyat Bilgisi Aliniyor .
        minFiyat=float(input("Minimum Fiyati Giriniz :"))
        maxFiyat=float(input("Maximum Fiyati Giriniz :"))
        # Fiyat Araliginda Araclari Listeye Eklemek Icin Bos Liste Olusturuluyor .
        bulunanAraclar=[]
        # Listeden Araclar Bulunuyor .
        for arac in arac_liste:
            fiyat=float(arac["fiyat"])
            if minFiyat<=fiyat<=maxFiyat:
                # Fiyat Araligindakiler Bos Listeye Ekleniyor .
                bulunanAraclar.append(arac)

        # Arac Bulunamadiysa Mesaj Gosteriliyor .
        if not bulunanAraclar:
            print("Fiyat Araliginda Araba Bulunamadi .")
        # Arac Bulunduysa Araclar Listeleniyor .
        else:
            print("Fiyat Araligindaki Arabalar :")
            print("--------------------------\n")
            for arac in bulunanAraclar:
                print(f"ID    :{arac['id']}")
                print(f"Marka :{arac['marka']}")
                print(f"Model :{arac['model']}")
                print(f"Renk  :{arac['renk']}")
                print(f"Yil   :{arac['yil']}")
                print(f"Fiyat :{arac['fiyat']}")
                print("--------------------------\n")

    except ValueError:
        # Gecersiz Deger Girilirse Hata Mesaji Gosteriliyor .
        print("Yanlis Fiyat Girildi !.")
# Girilen Kritere Gore Araclar Araniyor .
def aracArama():

    # Arac Arama Menusu
    print("\nArac Arama Menusu .")
    print("1- Marka .")
    print("2- Model .")
    print("3- Renk  .")
    print("4- Yil   .")
    print("0- Cikis .")

    # Menuden Hangi Kritere Gore Aramak Isteniyorsa Secim Yaptiriliyor .
    while True:
        aSecim=int(input("Arama Kriterini Seciniz :"))

        if aSecim==1:
            arama="marka"
            break
        elif aSecim==2:
            arama="model"
            break
        elif aSecim==3:
            arama="renk"
            break
        elif aSecim==4:
            arama="yil"
            break
        elif aSecim==0:
            # Cikis Yapiliyor .
            print("Arac Arama Menusunden Cikis Yapildi .")
            break
        else:
            # Hatali Secim Yapiliyor ve Tekrar Secim Yaptiriliyor .
            print("Hatali Secim Yapildi .")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            continue

    # Secilen Kriterdeki Bilgi Girilmesi Isteniyor .
    aramaYap=input(f"Arama Yapmak Istediginiz {arama} Giriniz :").lower()
    bulunanAraclar=[]
    # Listede Secilen Bilgiye Sahip Araba Var Ise Bos Listeye Ekleniyor .
    for arac in arac_liste:
        if arac[arama].lower()==aramaYap:
            bulunanAraclar.append(arac)

    # Arac Yok Ise Gerekli Bilgilendirme Yapiliyor .
    if not bulunanAraclar:
        print(f"{arama} , '{aramaYap}' Arac Bulunamadi .")
    # Bulunan Arac Listeleniyor .
    else:
        print(f"{arama} , '{aramaYap}' Araclar :")
        print("--------------------------\n")
        for arac in bulunanAraclar:
            print(f"ID    :{arac['id']}")
            print(f"Marka :{arac['marka']}")
            print(f"Model :{arac['model']}")
            print(f"Renk  :{arac['renk']}")
            print(f"Yil   :{arac['yil']}")
            print(f"Fiyat :{arac['fiyat']}")
            print("--------------------------\n")
# Araclarin Belirli Kriterlere Gore Istatistikleri Hesaplaniyor .
def aracKayitIstatistik():

    # Kayitli Arac Yok Ise Gerekli Bilgilendirme Yapiliyor .
    if not arac_liste:
        print("Kayitli Arac Bulunamadi !.")
        return
    # Gerekli Degisken Tanimlamalari Yapiliyor .
    toplamFiyat=0
    enDusukArac=arac_liste[0]
    enYuksekArac=arac_liste[0]

    # Araclarin Toplam Fiyatlari Bulunuyor .
    for arac in arac_liste:
        fiyat=float(arac["fiyat"])
        toplamFiyat+=fiyat

        # En Yuksek ve En Dusuk Fiyatli Araba Bulunuyor .
        if fiyat>float(enYuksekArac["fiyat"]):
            enYuksekArac=arac
        if fiyat<float(enDusukArac["fiyat"]):
            enDusukArac=arac

    # Ortalama Arac Fiyatlari Hesaplaniyor .
    ortalamaFiyat=toplamFiyat/len(arac_liste)

    # Bazi Onemli Bilgiler Ekrana Yazdiriliyor .
    print(f"Toplam Arac Sayisi  : {len(arac_liste)}")
    print(f"Ortalama Arac Fiyat : {ortalamaFiyat}")
    print(f"En Pahali Arac : {enYuksekArac["marka"]} {enYuksekArac["model"]} , Fiyati : {enYuksekArac["fiyat"]}")
    print(f"En Ucuz Arac : {enDusukArac["marka"]} {enDusukArac["model"]} , Fiyati : {enDusukArac["fiyat"]}")
# Menu Icinde Secim Yaptiriliyor .
def menu():
    while True:
        # Ana Menuden Yapilan Secimlere Gore Gerekli Islemler Yapiliyor .
        secim=ana_menu()
        if secim==1:
            aracKayitEkle()
        elif secim==2:
            aracKayitListele()
            print("\nArac Kayit Listeleme Islemi Tamamlandi .")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            # Islem Yapildiktan Sonra Ana Menu Icin Secim Yapiliyor .
            mSecim=int(input("Ana Menuye Donmek Icin [1] , Otomasyondan Cikis Yapmak Icin [2] :"))
            if mSecim==1:
                print("\n"*20)
                continue
            elif mSecim==2:
                print("\nOtomasyondan Cikiliyor !.")
                print("Iyi Gunler Dileriz ...")
                break
            else:
                print("\nHatali Secim Yapildi !.")
                print("Ana Menuye Donuluyor ...")
                continue

        elif secim==3:
            aracKayitSil()
            print("\nArac Kayit Silme Islemi Tamamlandi .")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            # Islem Yapildiktan Sonra Ana Menu Icin Secim Yapiliyor .
            mSecim=int(input("Ana Menuye Donmek Icin [1] , Otomasyondan Cikis Yapmak Icin [2] :"))
            if mSecim==1:
                print("\n"*20)
                continue
            elif mSecim==2:
                print("\nOtomasyondan Cikiliyor !.")
                print("Iyi Gunler Dileriz ...")
                break
            else:
                print("\nHatali Secim Yapildi !.")
                print("Ana Menuye Donuluyor ...")
                continue
        elif secim==4:
            aracKayitGuncelle()
            print("\nArac Kayit Guncelleme Islemi Tamamlandi .")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            # Islem Yapildiktan Sonra Ana Menu Icin Secim Yapiliyor .
            mSecim=int(input("Ana Menuye Donmek Icin [1] , Otomasyondan Cikis Yapmak Icin [2] :"))
            if mSecim==1:
                print("\n"*20)
                continue
            elif mSecim==2:
                print("\nOtomasyondan Cikiliyor !.")
                print("Iyi Gunler Dileriz ...")
                break
            else:
                print("\nHatali Secim Yapildi !.")
                print("Ana Menuye Donuluyor ...")
                continue

        elif secim==5:
            aracArama()
            print("\nArac Arama Islemi Tamamlandi .")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            # Islem Yapildiktan Sonra Ana Menu Icin Secim Yapiliyor .
            mSecim=int(input("Ana Menuye Donmek Icin [1] , Otomasyondan Cikis Yapmak Icin [2] :"))
            if mSecim==1:
                print("\n"*20)
                continue
            elif mSecim==2:
                print("\nOtomasyondan Cikiliyor !.")
                print("Iyi Gunler Dileriz ...")
                break
            else:
                print("\nHatali Secim Yapildi !.")
                print("Ana Menuye Donuluyor ...")
                continue

        elif secim==6:
            aracKayitIstatistik()
            print("\nArac Istatistiklerini Gosterme Islemi Tamamlandi .")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            # Islem Yapildiktan Sonra Ana Menu Icin Secim Yapiliyor .
            mSecim=int(input("Ana Menuye Donmek Icin [1] , Otomasyondan Cikis Yapmak Icin [2] :"))
            if mSecim==1:
                print("\n"*20)
                continue
            elif mSecim==2:
                print("\nOtomasyondan Cikiliyor !.")
                print("Iyi Gunler Dileriz ...")
                break
            else:
                print("\nHatali Secim Yapildi !.")
                print("Ana Menuye Donuluyor ...")
                continue

        elif secim==7:
            aracFiyatAraligi()
            print("\nBelirli Fiyattaki Araclari Bulma Islemi Tamamlandi .")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            # Islem Yapildiktan Sonra Ana Menu Icin Secim Yapiliyor .
            mSecim=int(input("Ana Menuye Donmek Icin [1] , Otomasyondan Cikis Yapmak Icin [2] :"))
            if mSecim==1:
                print("\n"*20)
                continue
            elif mSecim==2:
                print("\nOtomasyondan Cikiliyor !.")
                print("Iyi Gunler Dileriz ...")
                break
            else:
                print("\nHatali Secim Yapildi !.")
                print("Ana Menuye Donuluyor ...")
                continue

        elif secim==0:
            print("Otomasyondan Cikiliyor !.")
            print("Iyi Gunler Dileriz ...")
            break
        else:
            print("Hatali Secim Yapildi !.")
            print("Lutfen Belirtilen Secimlerden Birini Yapiniz .")
            # Islem Yapildiktan Sonra Ana Menu Icin Secim Yapiliyor .
            mSecim=int(input("Cikis Yapmak Icin [1] , Ana Menu Icin [2] :"))
            if mSecim==1:
                print("Otomasyondan Cikiliyor !.")
                print("Iyi Gunler Dileriz ...")
                break
            elif mSecim==2:
                print("\n"*20)
                continue
            else:
                print("Hatali Secim Yapildi !.")
                print("Ana Menuye Donuluyor ...")

# |--> ANA KISIM (Main)

aracDosyadanOkuma() # Programdan Cikis Yapildiginda Araclarin Kayip olma durumu Engelleniyor .
menu() # Genel Islemler Calistiriliyor .
