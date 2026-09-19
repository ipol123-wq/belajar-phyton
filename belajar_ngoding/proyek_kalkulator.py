print('1.penjumlahan')
print('2.pengurangan')
print('3.perkalian')
print('4.pembagian')
option=int(input('masukkan angka pilihan untuk mulai menghitung:' ))
int1=eval(input('masukkan angka pertama: '))
int2=eval(input('masukkan angka kedua: '))
if option==1:
    hasil = int1+int2
    print('hasil dari',int1,'+',int2,'=',hasil)
elif option==2:
    hasil = int1-int2
    print('hasil dari',int1,'-',int2,'=',hasil)
elif option==3:
    hasil = int1*int2
    print('hasil dari',int1,'*',int2,'=',hasil)
elif option==4:
    hasil = int1/int2
    print('hasil dari',int1,':',int2,'=',hasil)
else:
    print('option tidak valid')






