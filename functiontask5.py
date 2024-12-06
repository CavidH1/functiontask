def metndeki_herfler(metin):
    kicik_herfler = 0
    boyuk_herfler = 0
    for i in metin:
        if i.isupper():
            boyuk_herfler +=1
        elif i.islower():
            kicik_herfler +=1
    return kicik_herfler, boyuk_herfler
metin = input("metin daxil edi: ")
a, b = metndeki_herfler(metin)
# burda a kicik, b boyuk herflerdi. Cunki yuxarida funksiyanin deyisenlerini bildirende ve altda onu cagiranda positiona uygun yerlesdirir
print("kicik herflerin sayi: ",a )
print("boyuk herflerin sayi: ",b )
