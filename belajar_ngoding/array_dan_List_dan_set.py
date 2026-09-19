#array adalah tempat menyimpan sebuah data, yang mana bisa berupa list, tuple aatau set
#list[]  bisa di ubah isinya, bisa di duplikat, dan bisa pakai indeks/angka
#tuple() tidak bisa di ubah, bisa di duplikat dan bisa pakai indeks
#set{} bisa di ubah, tapi tidak bisa di duplikat dan tidak bisa pakai indeks

#list
ganjil= [1,3,4,5,6]
print(ganjil)
print(ganjil[2])
ganjil.append(21)
print(ganjil)
ganjil[2]=21#insert/ untuk menyidsipkan nilai pada posisi tertentuu
print(ganjil)
ganjil.remove(3)
print(ganjil)
ganjil.pop(1)
print(ganjil)
ganjil.append(24)
ganjil.append(24)
print(ganjil)
print(ganjil.count(24))#untuk melihat beraopa kali suaatu nilai keluar
ganjil.sort()#menngurutkan angka secaara asccending/dari nilai terkecil
print(ganjil)
ganjil.reverse()#mengurutkan angka secaraa descending/kebalikan dari ascending
print(ganjil)
print(len(ganjil))#menjumlahkan isi yang ada di list

variabel_baru=[6,8,7]
ganjil.extend(variabel_baru)#dignakan untuk mneanmbahkan beberapa elemen sekalligus ke akhir list
print(ganjil)

#set
#set adalah kumpulan data yang tidak menyimpan duplikat
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)

#contoh lain
nama = ['budi', 'andi', 'budi', 'citra', 'andi']
unik = set(nama)#otomatis berubah jadi set
print(unik)
unik = list(set(nama))#balik lagi jadi list
print(unik)

