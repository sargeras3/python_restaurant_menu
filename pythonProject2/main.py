""""
birinciSayi=50
ikinciSayi=60
toplam=birinciSayi+ikinciSayi

print(toplam)

cagatay=45   int
ayse="kelime"   string
ali='A'    string
fatma=0.5   float

"""
"""
+-*/
"""
""""
birinci=50
ikinci=60   
isim="ayse"

print(isim,(birinci+ikinci))


bir=80
iki=20
toplam="toplama sonucu"

print("toplam",(bir+iki))
bir=80
iki=20
cikar="cikarma sonucu"

print("cikar",(bir-iki))


birinci=int(input("lütfen birinci sayıyı gir"))
ikinci=int(input("lütfen ikinci sayıyı gir"))
print(birinci+ikinci)
"""

"""
soru: bir evde 3 kardeş vardır bu 3 kardeşin yaşları klavyeden girilecek
klavyeden girilen yaşların ortalaması ekrana yazdırılsın

expl: kardeşlerin yaşlarının ortalaması : 50 gibi..





birinciKardes=int(input("lütfen birinci kardeşin yaşını girin"))
ikinciKardes=int(input("lütfen ikinci kardeşin yaşını girin"))
ucuncuKardes=int(input("lütfen üçüncü kardeşin yaşını girin"))
toplam="kardeşlerin yasları ortalaması"
print(toplam,((birinciKardes+ikinciKardes+ucuncuKardes)/3))


bir evde 3 kardes var bunların boyları klavyeden alınacakmıs boylar ondalıklı
 olarak girlecek boylarının ortalaması ekrana yazdırılsın


birinciKardes=float(input("lütfen birinci kardeşin boy girin"))
ikinciKardes=float(input("lütfen ikinci kardeşin boy girin"))
ucuncuKardes=float(input("lütfen üçüncü kardeşin boy girin"))
toplam="kardeşlerin boyları ortalaması"
print(toplam,((birinciKardes+ikinciKardes+ucuncuKardes)/3))



aysenin bana 750 tl borcu var...
ayse klavyesden sayıda klavyeden gelecek

isim=input("isim girin: ")
para=int(input("parayı girin: "))



print(isim,"nin bana",para,"tl borcu var")


print("{0} nin bana {1} tl borcu var".format(isim,para))

isim=input("isim girin: ")
para=int(input("parayı girin: "))


ahmedin bana 12.ayda verecegi 500 tl yerine 7.ayda 200 tl verdi
isim - ay sayıları-para sayıları


isim=input("isim girin: ")
ay=int(input("ay girin: "))
para=int(input("para girin: "))
ayiki=int(input("ay girin: "))
paraiki=int(input("paraiki girin: "))

print("{0} bana {1}.ayda vereceği{2} tl yerine {3} .ayda {4} tl verdi".format(isim,ay,para,ayiki,paraiki))



bir=int(input("lütfen birinci sayı girin"))
iki=int(input("lütfen birinci sayı girin"))
uc=int(input("lütfen birinci sayı girin"))
toplam=(bir+iki+uc)

print(toplam)

"""
"""
storyboard
if
// tek şarta göre tek sonuc
// tek şarta göre birden fazla sonuc
// birden fazla şarta göre tek sonuc
// birden fazla şarta göre birden fazla sonuc



yas=int(input("ltfn sayı gir"))

if yas<20:
    print("baby")
else:
    print("adult")


sayi=int(input("ltfn sayı gir"))

if sayi<50:
    print("kaldı")
else:
    print("gecti")



islem=int(input("islem secin\n 1-toplama"))

sayi1=int(input("birincisayi gir:"))
sayi2=int(input("ikincisayi gir:"))

if islem==1:
    print(sayi1+sayi2)
else:
    print(sayi1*sayi2)
    
    
    takim=input("takımınızı seciniz")

if takim=="fenerbahçe":
    print("güzel takım")
else:
    print(":D")



puan=int(input("notunuzu giriniz"))

if puan<0:
    print("HATALI GİRİŞ")
elif puan<30:
    print("ff")
elif puan<40:
    print("dd")
elif puan<50:
    print("cd")
elif puan<60:
    print("cc")
elif puan<70:
    print("cb")
elif puan<80:
    print("bb")
elif puan<90:
    print("ba")
elif puan<100:
    print("aa")
else:
    print("0 ile 100 arasında bir değer girmelisiniz")

klavyeden bir sayı al bu asyı 1 olursa 2 sayı klavyeden alınacak ve bu iki sayı toplanacak
klavyeden alınan sayı 2 olursa bu iki sayıyı


islem=int(input("islem secin\n 1-toplama\n 2-çıkarma\n 3-çarpma\n 4-bölme\n"))

if islem==1:
    birincisayi=int(input("birinci sayı girin"))
    ikincisayi=int(input("ikinci sayı girin"))
    print(birincisayi+ikincisayi)

elif islem==2:
    birincisayi = int(input("birinci sayı girin"))
    ikincisayi = int(input("ikinci sayı girin"))
    print(birincisayi - ikincisayi)

elif islem==3:
    birincisayi = int(input("birinci sayı girin"))
    ikincisayi = int(input("ikinci sayı girin"))
    print(birincisayi * ikincisayi)

elif islem==4:
    birincisayi = int(input("birinci sayı girin"))
    ikincisayi = int(input("ikinci sayı girin"))
    print(birincisayi / ikincisayi)
else:
    print("hatalı giriş")
    
    
    sart1 kullanıcı adı==admin
    sart2 sifre==1234
    
    
kullaniciAdi=input("kullanıcı adınızı giriniz")
sifre=input("şifrenizi giriniz")

if kullaniciAdi=="admin" and sifre=="1234":
    print("giris başarılıdır")
else:
    print("hatalı giriş")


işe alma programı
kullanıcılardan 2 kriter istendi yaşı>30 ve adresi kepez oanlar işe alındı
aksi halde biz sizi ararız

yas=int(input("ltfn yasınızı giriniz"))
adres=input("ltfn adresinizi giriniz")

if yas>30 and adres=="kepez":
    print("ise alındınız")
else:
    print("bsa")
    
  """
"""
    --or-- iki şarttan biri gerçekleşmesi yeterli
  
    yas=int(input("ltfn yasınızı giriniz"))
adres=input("ltfn adresinizi giriniz")

if yas>30 or adres=="kepez":
    print("ise alındınız")
else:
    print("bsa")
"""

"""
--------döngüler--------
1-for     // sayısı belli olan dönüler
2-foreach  // listelerde kolay kullanım
3-while     // sonsuz ve sayısı belli olmayan
4-do while   //şartlı


for ayse in range(10):
    print(ayse,"-merhaba")


"""
"""
puan=int(input("notunuzu giriniz"))

if puan>50:
    print("geçti")
else:
    print("kaldı")
   
   klavyeden sayı aldık 50den büyükse 5 defa geçti aksi halde 5 defa kaldı yazsın
   """
"""
sayi=int(input("sayı giriniz"))

if sayi>50:
    for a in range(5):
        print("geçti")
else:
    for a in range(5):
        print("kaldı")
        klaveyeden 2 deger al yas>30 ve adrs kepez eşit olursa işe alındı yazacak 15 kere aksi halde 5 defa bsa
"""
"""
yas=int(input("ltfn yasınızı giriniz"))
adres=input("ltfn adresinizi giriniz")

if yas>30 and adres=="kepez":
    for a in range(15):
        print("ise alındınız")
else:
    for a in range(5):
         print("bsa")
 """
"""
klavyeden girilen 2 sayı arasındaki tek sayıları listeleyen program

"""
"""

birinciSayi=int(input("birinci sayı gir"))
ikinciSayi=int(input("ikinci sayi gir"))

for a in range(birinciSayi,ikinciSayi):
    print(a)
    
"""
"""
mod alma:
birinciSayi=int(input("birinci sayı gir"))

if birinciSayi%2==1:
    print("tektir")

else:
    print("çifttir")
    
    birinciSayi=int(input("birinci sayı gir"))
ikinciSayi=int(input("ikinci sayi gir"))

for a in range(birinciSayi,ikinciSayi):
    if a%2==1:
        print(a)
"""

"""
klavyeden 2 sayı çifteri listele
"""

"""
birinciSayi=int(input("birinci sayı gir"))
ikinciSayi=int(input("ikinci sayi gir"))

for a in range(birinciSayi,ikinciSayi):
    if a%2==0:
        print(a)
"""
"""
while 3 şey ister
-başlangıç  sayısı
-şart
-dönme biçimi

"""

"""
yazdir=0

while yazdir<20:
    print("merhaba")
    yazdir+=1

"""

"""
klavyeden sayi alacagız bu sayı 50 den büyük olursa geçti yazacak 5 defa for ile aksi halde 10 defa kaldı while ile
"""
"""
sayi=int(input("sayi giriniz"))

if sayi>50:
    for a in range(5):
        print("geçti")
else:
    sayi=0
    while sayi < 5:
        print("kaldı")
        sayi+=1
"""
"""
birinciSayi=int(input("ltfn birinci sayi giriniz"))
ikinciSayi=int(input("ltfn ikinci sayi giriniz"))

while birinciSayi<ikinciSayi:
    if birinciSayi%2==0:
        print(birinciSayi)
    birinciSayi+=1
"""

"""
array - diz - liste - arraylist

"""

"""
klavyeden sayı al 1 olursa meyvelr farklı sayı olursa sebzeler
"""

"""
meyveler=["elma","armut","muz","çilek"]
sebzeler=["pırasa","kabak","ıspanak","patlıcan"]

sayi=int(input("bir sayi giriniz"))

if sayi==1:
    for m in meyveler:
        print(m)
else:
    for s in sebzeler:
        print(s)

"""
"""
klavyeden bir harf al e yazılırsa erkekler k yazılırsa kadınlar listesi farkl bi harf girerse hatal giriş
"""

"""
erkekler=["ali","veli","ahmet","mehmet"]
kadinlar=["ayse","fatma","merve","nur"]

harf=input("bir harf giriniz")
if harf=="e":
    for e in erkekler:
        print(e)
elif harf=="k":
    for k in kadinlar:
        print(k)
else:
    print("hatalı giriş")
"""



"""
arabalar=["bmw","opel","mercedes"]
motorlar=["honda","kavasaki"]

sayi=int(input("bir sayi giriniz"))

if sayi==1:
    for a in arabalar:
        print(a)
else:
    print(motorlar)
   """

"""
antalyaIlce=["kepez","muratpasa"]
afyonIlce=["dinar","sandıklı"]

kelime=input("şehir giriniz")

if kelime=="antalya":
    for a in antalyaIlce:
        print(a)
elif kelime=="afyon":
    for af in afyonIlce:
        print(af)
else:
    print("hatalı giriş")
"""

"""
birinciSayi=int(input("birinci sayı gir"))
ikinciSayi=int(input("ikinci sayi gir"))

for a in range(birinciSayi,ikinciSayi):
    if a%2==1:
        print(a)
"""
"""
birinciSayi=int(input("birinci sayı gir"))
ikinciSayi=int(input("ikinci sayi gir"))


while birinciSayi<ikinciSayi:
    if birinciSayi%2==1:
        print(birinciSayi)
    birinciSayi+=1
"""



"""
syntax   bir programlama dilinin yazım kuralları demektir
"""
"""meyveler=["elma","armut","muz","çilek"]

sayı=int(input("bir sayı giriniz"))

if sayı==1:
    print(meyveler)
else:
    print("meyve yok")"""
"""
restorana hoşgeldin
lütfen seçiminizi yapınız
1-menu
0-çıkış


bir dizi içinde 4 scenek 1 yemekler 2 çorbala 3 tatlılar 4 salatalar
"""
hesap=0
birinciDeger=int(input("Restorantımıza Hoşgeldiniz\n 1-Menü\n 2-Çıkış \n Lütfen Seçiminizi Yapınız\n"))

while True:
    if birinciDeger == 1:
        menu = ["1-Yemekler", "2-Çorbalar", "3-Tatlılar", "4-Salatalar"]
        for m in menu:
            print(m)
        ikinciDeger = int(input("Lütfen Seçiminizi Yapınız\n"))
        if ikinciDeger == 1:
            print("yemekler")
            yemekler = ["1-Pide: 30 Tl", "2-Mantı:50 TL", "3-Sarma:40 TL", "4-Ciğer:50 TL", "5-Köfte:45 TL"]
            for y in yemekler:
                print(y)
            ucuncuDeger = int(input("Lütfen Seçiminizi Yapınız\n"))
            if ucuncuDeger == 1:
                print("Seçiminiz:", yemekler[0])
                hesap = hesap + 30
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 2:
                print("Seçiminiz:", yemekler[1])
                hesap = hesap + 50
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 3:
                print("Seçiminiz:", yemekler[2])
                hesap = hesap + 40
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 4:
                print("Seçiminiz:", yemekler[3])
                hesap = hesap + 50
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 5:
                print("Seçiminiz:", yemekler[4])
                hesap = hesap + 45
                print("Toplam Hesabınız:", hesap)
            else:
                print("Hatalı Giriş")
        elif ikinciDeger == 2:
            corbalar = ["1-Mercimek:30 TL", "2-Paça:30 TL", "3-Yayla:30 TL", "4-Mantar:30 TL", "5-Tarhana:30 TL"]
            for c in corbalar:
                print(c)
            ucuncuDeger = int(input("Lütfen Seçiminizi Yapınız\n"))
            if ucuncuDeger == 1:
                print("Seçiminiz:", corbalar[0])
                hesap = hesap + 30
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 2:
                print("Seçiminiz:", corbalar[1])
                hesap = hesap + 30
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 3:
                print("Seçiminiz:", corbalar[2])
                hesap = hesap + 30
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 4:
                print("Seçiminiz:", corbalar[3])
                hesap = hesap + 30
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 5:
                print("Seçiminiz:", corbalar[4])
                hesap = hesap + 30
                print("Toplam Hesabınız:", hesap)
            else:
                print("Hatalı Giriş")

        elif ikinciDeger == 3:
            tatlilar = ["1-Baklava:40 TL", "2-Sütlaç:20 TL", "3-Kazandibi:25 TL", "4-Künefe:40 TL", "5-Kabak:20 TL"]
            for t in tatlilar:
                print(t)
            ucuncuDeger = int(input("Lütfen Seçiminizi Yapınız\n"))
            if ucuncuDeger == 1:
                print("Seçiminiz:", tatlilar[0])
                hesap = hesap + 40
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 2:
                print("Seçiminiz:", tatlilar[1])
                hesap = hesap + 20
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 3:
                print("Seçiminiz:", tatlilar[2])
                hesap = hesap + 25
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 4:
                print("Seçiminiz:", tatlilar[3])
                hesap = hesap + 40
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 5:
                print("Seçiminiz:", tatlilar[4])
                hesap = hesap + 20
                print("Toplam Hesabınız:", hesap)
            else:
                print("Hatalı Giriş")
        elif ikinciDeger == 4:
            salatalar = ["1-Çoban:25 TL", "2-Mevsim:25 TL", "3-Rus:30 TL", "4-Sezar:35 TL", "5-Gavudağı:25 TL"]
            for s in salatalar:
                print(s)
            ucuncuDeger = int(input("Lütfen Seçiminizi Yapınız\n"))
            if ucuncuDeger == 1:
                print("Seçiminiz:", salatalar[0])
                hesap = hesap + 25
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 2:
                print("Seçiminiz:", salatalar[1])
                hesap = hesap + 25
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 3:
                print("Seçiminiz:", salatalar[2])
                hesap = hesap + 30
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 4:
                print("Seçiminiz:", salatalar[3])
                hesap = hesap + 35
                print("Toplam Hesabınız:", hesap)
            elif ucuncuDeger == 5:
                print("Seçiminiz:", salatalar[4])
                hesap = hesap + 25
                print("Toplam Hesabınız:", hesap)
            else:
                print("Hatalı Giriş")

        else:
            print("Hatalı Giriş")


    elif birinciDeger == 0:
        print("Çıkış yaptınız tekrar bekleriz...")
    else:
        print("Hatalı Giriş")


        """
        ÖDEV: BUNU GİTHUBA YÜKLE 
        """
