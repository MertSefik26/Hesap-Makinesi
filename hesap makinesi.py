i=6
while(i<10):
    birincisayi=int(input("sayiyi giriniz:"))
    ikincisayi=float(input("sayiyi giriniz:"))



    islem=input("""Ne yapmak istiyorsunuz.\nÇıkmak için X\ntoplama için +\n çıkarma için -\n bölme için /\n çarpma için *\n:""")

    if islem == "+":
        print("sonuç="+str(birincisayi+ikincisayi))

    elif islem=="-":
        print("sonuç="+str(birincisayi-ikincisayi))

    elif islem=="/":
        if birincisayi==0:
            print("0 bir sayıaya bölünmemez.")
        elif ikincisayi==0:
            print("Sonuç. tanımsız. Çünkü ikinci sayı 0 olamaz")
        else:
            print("sonuç="+str(birincisayi/ikincisayi))
        
    elif islem=="*":
        print("sonuç="+str(birincisayi*ikincisayi))

    elif  islem=="X" or islem=="x":
        i=88
print("hoşçakal")
