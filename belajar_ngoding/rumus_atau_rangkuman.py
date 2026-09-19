#bab 1 pengenalan tipe
nama = 'risal'#TIPE STRING'
print('risal anzay')#comentar blok program
#pagar tidak  akan di baca di programan
print('halo nama saya ' + nama)#string = nama(string) = boleh
usia = 18#tipe interger
print('halo usia saya ' + usia)#string + usia(integer) = error
inggi_badan = 183.5 #tipe flot/desimal
print('tinggi_badan saya ' + tinggi_badan)#string + tonggobadan(flot) = error
#ubah agar bisa di gabung/tidak erorr
int("10")-->>> 10#converter string to integer
str(5)>>>>>> "5" #converter angka/int to string
float(5)--------> 5.0 #converter angka to bilangan desimal
bool#ya tatau tidak. contoh
punya_pacar = True#iya
punya_pacar = False#tidak
#jika kita meperbarui suatu informasi di pemrograman maka akan terperbaru/timpa. coontoh
#di awal aku tulis iya lalu ku timpa tidak maka hasilnya tidak
nama = 'risal'
usia = 18
tinggi_badan = 180.5
punya_pacar = True#tidak
punya_pacar =  False#timpa

print(nama)
print(usia)
print(tinggi_badan)
print('nama saya adalah ' + nama)
print('usia saya adalah ' + str(usia))
print('tinggi badan saya adalah '+ str(tinggi_badan))
print('halo nama saya ' + nama + ' usia saya adalah ' + str(usia))
print('tinggi badan saya adalah ' + str(tinggi_badan) + 'cm')

#
print(input('halo siapa nama kamu?'))
#input('lalalalala')
#input bisa  mengetik di terminal
input_nama = input('halo siapa namma kamu?')
print(input_nama)

a = 10
b =20
# + - * /
c = a + b #tipe data float?berubah sesuai hasilnya
print(c)

a = input('masukkan angka pertama') #str misal 5
b = input('masukkan angka kedua') #str misal 7
c = a + b
print(c) #hasilnnya jadi 5 7. karena str = str. jadi untuk menjumlahkan-
#kita perlu merubahnya jadi interger terlebih dahulu
c = int(c) + int(b)
print(c)#hasilnya 12

print('hasilnya adalah ' + c)#erorr karena c di atas telah berubah menjadi interger
print('hasilnya adalah ' + str(c))#benar karena int telah di rubah kembali jadi str
c = int(a) / int(b). #semisal 9/2 hasilnya 4.5
c = int(a) // int(b). #semisal 9/2 hasilnya 4 (dibulatkan)

nama_saya = ('widodo armin sultan')
input(nama_saya.find('n'))# find untuk mencari huruf misal huru s. di mulai dari 0
print(len(nama_saya))#len menghitung isi suatu variabel. di mulai dari 1
print('s' in (nama_saya))#in untuk mencari suatu keberadaan benar atau tidaknya. true=ya false=tidak
print(nama_saya.upper())#upper mengubah variabel jadin huruf besar keseluruhan
print(nama_saya.capitalize())#capitalizer mengkapitalkan huruf depan
print(nama_saya.count('a'))#count menghitung jumlah huruf dalam suatu variabel, mialnya menghitung brp hiruf a

#bab 2 perkondisian

# == sama dengab
# > lebih dari
# < kurang dari
# != tidak sama dengan
# >= lebih dari sama dengN
# <=KURANG DARI SAMA DENGAN
if #artinya jika

usia = 100
if usia >= 5 and usia <= 10:
    print('halo anak anak')
elif usia > 10 and usia <= 20:
    print('halo remaja')
 elif usia > 20 and usia <= 30:
    print('bapak bapak/mamak mamak')
elif usia > 30 and usia <= 75:
    print('nenek2')
elif usia >= 75 and usia <= 100:
    print('omma udah tua')
elif usia > 0 and usia <= 4:
    print('balita')
else:
    print('yo kurang tua bro')

awal = 1

while awal <= 15:
    print(awal)
    awal += 1 #artinya sama saja dengan awal = awal + 1

#for/loop
for angka in range(1, 9):
    print(angka)
for angka in range(6):
    print(angka)

def sapa():
    print('halo')
sapa()

for i in range(4):
    sapa()

#function + parameter
def sapa(nama):
    print('halo', nama)
sapa('budi')
sapa('risal')

def sapa(nama):
    print('halo', nama)
sapa('budi')
for i in range (4):
    sapa('budi')

def sapa(nama):
    print('halo nama saya ', nama)
sapa('alif')
for i in range (10):
    sapa('alif')

#function + parameter
def tambah (a, b):
    return a + b
hasil = tambah(10,5)
print(hasil)

#function + parameter + if
def hitung_sisa(saldo, hutang):
    return saldo + hutang
hasil = hitung_sisa(6000, 5000)
print(hasil)

def cek_hutang(saldo, hutang):
    if saldo >= hutang:
        return'bisa bayar hutang'
    else:
        return'saldo loe gak cukup woiii'
hasil = cek_hutang(6000, 5000)
print (hasil)

def hitung_diskon(harga):
    if harga >= 100000:
        return 'selamat anda mendapatkan diskon 20%'
    elif harga < 100000:
        return 'mohon maaf anda tidakmendapatkan diskon'
hasil = hitung_diskon(150000)
print (hasil)

#hitung diskon
def hitung_diskon(harga):
    if harga >= 100000:
        diskon = harga * 20 / 100
        harga_akhir = harga - diskon
        return harga_akhir
    else:
        return harga
hasil = hitung_diskon(150000)
print(hasil)

#hitung diskon
def hitung_diskon(harga):
    if harga >= 500000:
        diskon = harga * 20 / 100
        harga_akhir = harga - diskon
        print('selamat anda mendapatkan potongan harga 20%')
        print('total harga adalah')
        return harga_akhir
    else:
        print('mohon maaf anda tidak mebdapatkan diskon')
        print('total harga adalah')
        return harga
hasil= hitung_diskon(500000)
print(hasil)

def hitung_diskon(harga, diskon):
    return harga - (harga * diskon / 100)
harga_akhir = hitung_diskon(100000, 20)
print(harga_akhir)


#contoh belanja
def hitung_belanja(harga, jumlah):
    total = harga * jumlah
    if total >= 100000:
        diskon = total * 20 / 100
        total_bayar = total - diskon
        print('selamat anda mendapatkan potongan diskon sebesar 20%')
        print('total belanja adalah Rp', total)
        print('total bayar adalah Rp', total_bayar)
    else:
        print('mohon maaf anda tidak mebdaptakan diskon karena belanja anda kurang dari 100000')
hitung_belanja(90000, 3)

#bermain game demgan komputer
import random
angka_rahasia = random.randint(1,10)
print(angka_rahasia)
tebakan = int(input('masukkan tebakan'))
if tebakan < angka_rahasia:
    print('terlalu kecil')
elif tebakan > angka_rahasia:
    print('terlalu besar')
else:
    print('benar')

hewan = []
hewan.append('kucing')
hewan.append('anjing')
hewan.append('harimau')
print(hewan)
hewan.insert(1, 'burung')
print('setelah insert', hewan)
hewan.remove('anjing')
print('setelah remove', hewan)
terhapus = hewan.pop()
print('setelah pop', hewan)
print('yang terhapus', terhapus)

#for
nama_makanan = ['nasgor goreng', 'ayam goreng rebus', 'sapi panggang']
for i in nama_makanan:
    print(i)
for i in range(len(nama_makanan)):
    print(i + 1, nama_makanan[i])

#MENTAHAN BELANJA
belanja = []
while True:
    print('/n===Daftar Belanja===')
    print('1. Lihat daftar')
    print('2. Tambah barang')
    print('3. Hapus barang')
    print('4. Keluar')

    pilihan = input('pilih menur(1-4): ')

    if pilihan == '1':
        pass
    elif pilihan == '2':
        pass
    elif pilihan == '3':
        pass
    elif pilihan == '4':
        print('Terim kasih')
        break
    else:
        print('Pilihan tidak valid')


