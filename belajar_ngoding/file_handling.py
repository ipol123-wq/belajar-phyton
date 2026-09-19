#jika file.open itu perlu di tutup denga file.close
#jika menggunakan with otomatis tertutup saat tidak di gunakan

#membuat file
with open('belajar handling.txt', 'w') as file:
    file.write('woy lu lagi ngapain')
#menimpa file cukup ulangi lagi 'w'

#menambahkan data
with open('belajar handling.txt', 'a') as file:
    file.write('\ngua gak ngapa ngapain anjay')

#membaca file
with open('belajar handling.txt', 'r') as file:
    isi = file.read()
    print(isi)

#menhapus file
import os
os.remove('nama file.txt')

#menyimpan variabel ke file
saldo = 15000
with open('belajar handling.txt', 'w') as file:
    file.write(str(saldo))#merubah saldo dari int menjadi str
#membaca file

    data = file.read()
    saldo_baru = int(data)
    print('saldo dari file', saldo_baru)

#simpan dan baca di program yang sama
#saldo awal di file 150000
import os
#baca saldo
if os.path.exists('saldo.txt'):
    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())
else:
    saldo = 0
print('saldo awal:', saldo)
#tambah saldo
tambah = int(input('maasukkan pemasukan: '))
saldo += tambah
print('saldo sekarang:', saldo)
#simpan lagi
with open('saldo.txt', 'w') as file:
    file.write(str(saldo))

#mengurangi atau menambah saldo di file
import os
if os.path.exists('saldo.txt'):
    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())
jumlah = int(input('masukkan nnominal: '))
if jumlah <= saldo:
    saldo -= jumlah
    print(f'{jumlah} berhsil di tarik')
    print(f'saldo sekrang: {saldo}')
else:
    print('maaf saldo and tidak mencukupi')
with open ('saldo.txt', 'w') as file:
    file.write(str(saldo))

#reset saldo
with open ('saldo.txt', 'w') as file:
    file.write('0')

#variasi
import os
saldo = 0
pin_benar = 241124
kesempatan = 3
if os.path.exists('saldo.txt'):
    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())
while kesempatan > 0:
    pin = int(input('silahkam masukkan pin anda: '))
    if pin == pin_benar:
        print('pin yang anda masukkan benar')
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f'mohon maaf pin yang anda maukkan salah, ssa kesempatan: {kesempatan}')
        else:
            print('mohon  maaf anda telah salah memasukkan pin 3 kali')
            print('kini akuna anda telah kami blokir')
            print('silahkan hubngi kodtumer servis untuk info lebih lanjut')
if kesempatan > 0:
    print('\nselamat datang di aplikssi my atm')
    print('silahkann pilih menu di bawah ini')
    print('1. cek saldo')
    print('2. setor tunai')
    print('3. tarik tunai')
    print('4. keluar')
    while True:
        pilihan = input('silahkan masukkan menu yang anda pilih: ')
        if pilihan == '1':
            print(f'total saldo anda adlah: {saldo}')
        elif pilihan == '2':
            jumlah = int(input('silahkan masukkan nominal yang akan anda setor: '))
            saldo += jumlah
            print(f'{jumlah} telah berhasil di tambahkna ke saldo')
            print(f'total saldo adalah: {saldo}')
        elif pilihan == '3':
            jumlah = int(input('silahkan masukkannominal yang akan anda tarik: '))
            if jumlah <= saldo:
                saldo -= jumlah
                print(f'{jumlah} berhasil di tarik')
                print(f'sisa saldo anda adlah: {saldo}')
            else:
                print('mohon maaf saldo anda tdak mencukupi untuk melakukan penarikan')
        elif pilihan == '4':
            with open ('saldo.txt', 'w') as file:
                file.write(str(saldo))
            print('terima kasih telah menggunakan layanan kami')
            break
        else:
            print('mohon maaf kode yang anda masukkan tidak valid')

#buat file json
with open ('riwayat.json', 'w') as file:
    json.dump(riwayat, file)#ubah data Python → tulisan, lalu simpan

#baca file json
with open ('riwayat.json', 'r') as file:
    riwayat = json.load(file)#baca tulisan → kembalikan jadi data Python

#variasi
import json
riwayat = [
    {'jenis': 'pemasukan', 'jumlah': 5000},
    {'jenis': 'pengeluaran', 'jumlah': 20000}
]
#simpan
with open ('riwayat.json', 'w') as file:
    json.dump(riwayat, file)
    #baca
with open ('riwayat.json', 'r') as file:
    data = json.load(file)
print(data)
print(data[0]['jenis'])
print(data[0]['jumlah'])

import os
import json
saldo = 0
riwayat = []
pin_benar = 241124
kesempatan = 3
if os.path.exists('saldo.txt'):
    with open ('saldo.txt', 'r') as file:
        saldo = int(file.read())
if os.path.exists('rawayat.json'):
    with open('riwayat.json', 'r') as file:
        riwayat = json.load(file)
else:
    riwayat = []

while kesempatan > 0:
    pin = int(input('silahkan masuskkan pin anda: '))
    if pin == pin_benar:
        print('pin yang anda masukkan benar')
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f'pin yang anda masukkan salah, sia kesempatan {kesempatan}')
        else:
            print('anda telah salah memasukkan pin 3 kali')
            print('akun anda telah di blokir')
            print('silahkan hubungi kostumer sevis untuk info lebih lanjut')
            break
if kesempatan > 0:
    print('\nselamat datang di aplikasi my atm')
    print('siahkan pilih opsi di bawah ini')
    print('1. cek saldo')
    print('2. tambah pemasukan')
    print('3. tambah pengeluaran')
    print('4. cek riwayat'  )
    print('5. keluar')
    while True:
        pilihan = input('suilahkan masukkan opdi pilihan anda: ')
        if pilihan =='1':
            print(f'salddo anda adalah: Rp{saldo}')
        elif pilihan =='2':
            jumlah = int(input('maukkan nominal yang akan anda tambahakn: '))
            saldo += jumlah
            riwayat.append({
                'jenis': 'pemasukan',
                'jumlah': jumlah,
            })
            print(f'RP{jumlah} berhasil di tambahkan ke saldo')
            print(f'total saldo anda adalah: Rp{saldo}')
        elif pilihan =='3':
            jumlah = int(input('silahkan masukkan nominaml penarikan: '))
            if jumlah <= saldo:
                saldo -= jumlah
                riwayat.append({
                    'jenis': 'pengeluaran',
                    'jumlah': jumlah
                })
            else:
                print('mohon maaf saldo anda tidak mencukupi untuk melaskukan penarikan')
        elif pilihan =='4':
            if len(riwayat)==0:
                print('mohon maaf anda belu memilki riwayat transkasi')
            else:
                print('\nRIWAYAT TRRANSAKSI')
                for i, item in enumerate(riwayat, start=1):
                    print(f'{i}. {item['jenis']} - Rp{item['jumlah']}')
        elif pilihan =='5':
            print('terima kasih telah menggunakan layanan kami')
            with open('saldo.txt', 'w') as file:
                file.write(str(saldo))
            with open('riwayat.json', 'w') as file:
                json.dump(riwayat, file)
                break
        else:
            print('mohon maaf kode yang anda masukkan tidak valid ')
#try except, untuk mencegah terjadinya crash/erorr
try:
    angka = int(input('masukkan angka'))
    print ('angka kamu:', angka)
except:
    print('masukkan angka yang valid')

#variasi dengan try expert json
import os
import json
saldo = 0
riwayat = []
kesempatan = 3
pin_benar = 241124
if os.path.exists('saldo.txt'):
    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())
if os.path.exists('riwayat.json'):
    with open ('riwayat.json', 'r') as file:
        riwayat = json.load(file)
else:
    riwayat = []
while kesempatan > 0:
    pin = int(input('silahkan masukkan pin anda terlebih dahulu: '))
    if pin == pin_benar:
        print('pin yang anda masukkan benar')
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f'pin yang anda masukkan salah, sisa kesempatan: {kesempatan}')
        else:
            print('anda sudah salah memasukkan pin 3 kali')
            print('kini akun anda telah di blokir')
            print('silahkan hubungi kostuner servis untuk info lebih lanjut')
            break
if kesempatan > 0:
    print('selamat datang ssi aplikasi my atm')
    print('silahkan pilih opsi di bawah ini')
    print('1. cek saldo')
    print('2. setor tunai')
    print('3. tarik tunai')
    print('4. cek riwayat')
    print('5. kelaur')
    while True:
        pilihan = input('silahkan masukkan opsi yang anda pilih')
        if pilihan =='1':
            print(f'saldo anda adalah: Rp{saldo}')
        elif pilihan == '2':
            try:
                jumlah = int(input('silahkan masukkan nominal yang akan anda setor: '))
                saldo += jumlah
                riwayat.append({
                    'jenis': 'pemasukan',
                    'jumlah': jumlah
                })
                print(f'{jumlah} berhasil di setor')
                print(f'total saldo anda adalah: Rp{saldo}')
            except:
                print('masukkan angka coy jangan malah huruf!!!')
        elif pilihan =='3':
            try:
                jumlah = int(input('silahka amasukkan nominal yang akan anda tarik: '))
                if jumlah <= saldo:
                    saldo -= jumlah
                    riwayat.append({
                    'jenis': 'pengeluaran',
                    'jumlah': jumlah
                    })
                    print(f'{jumlah} berhasil di tarik')
                    print(f'total saldo anda saat ini adlah: Rp{saldo}')
                else:
                    print('mohon maaf saldo anda tidak mencukupi untuk melakukan penarikan')
            except:
                print('maukkan angka woiilah cik')
        elif pilihan =='4':
            if len(riwayat) ==0:
                print('mohon maaf anda belum memilki riwayat transaksi')
            else:
                print('\nRIWAYAT TRANSAKSI')
                for i, item in enumerate(riwayat, start=1):
                    print(f'{i}. {item['jenis']} - Rp{item['jumlah']}')
        elif pilihan =='5':
            print('terima kasih telah menggunakan layanan kami')
            with open ('saldo.txt', 'w') as file:
                file.write(str(saldo))
            with open('riwayat.json', 'w') as file:
                json.dump(riwayat, file)
                break
        else:
            print('opsi yang anda masukkan salah')

#function + file handling
import os
import json
if os.path.exists('saldo.txt'):
    with open('saldo.txt', 'r') as file:
        saldo = int(file.read())
if os.path.exists('riwayat.json'):
    with open ('riwayat.json', 'r') as file:
        riwayat = json.load(file)
else:
    riwayat = []
pin_benar = 241124
kesempatan = 3
def cek_saldo():
    print(f'saldo anda adalah {saldo}')
def setor_tunai():
    global saldo
    try:
        jumlah = int(input('silahkan masukkan nominal yang akan anda setor: '))
        saldo += jumlah
        riwayat.append({
            'jenis': 'pemasukan',
            'jumlah': jumlah
        })
        print(f'{jumlah} telah berhasil di tambahkan ke saldo')
        print(f'total saldo anda saat ini adalah: {saldo}')
    except:
        print('woi masukin angka')
def tarik_tunai():
    global saldo
    try:
        jumlah = int(input('silahkan masukkan nominal yang akan anda tarik; '))
        if jumlah <= saldo:
            saldo -= jumlah
            riwayat.append({
                'jenis': 'pengeluaran',
                'jumlah': jumlah
            })
            print(f'{jumlah} telah berhasil di tarik')
            print(f'total saldo anda saat ini adlah: {saldo}')
        else:
            print('mohon maaf saldo anda tidak mencukupi untuk melakkan penarikan')
    except:
        print('woi masukin angka')
def cek_riwayat():
    global riwayat
    if len(riwayat)==0:
        print('mohon maaf anda belum memiliki riwayat transaksi')
    else:
        print('\nRIWAYAAT TRAMNSAKSI')
        for i, item in enumerate(riwayat, start=1):
            print(f'{i}. {item['jenis']} - Rp{item['jumlah']}')
def keluar():
    with open('saldo.txt', 'w') as file:
        file.write(str(saldo))
    with open('riwayat.json', 'w') as file:
        json.dump(riwayat, file)
    print('teerima kasih telah menggunakan layanan kami')
while kesempatan > 0:
    pin = int(input('silahkan masukkan pin anda teelebih dahulu: '))
    if pin == pin_benar:
        print('pin yang anda masukkan benar')
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f'pin yang anda masukkan salah, sisa kesempatan {kesempatan}')
        else:
            print('anda sudah salah memasukkan pin 3 kali')
            print('saat inii akun anda telah di blokir')
            print('hubungi kostumer seervis untuk info lebih lanjut')
            break
if kesempatan > 0:
    print('selamat datang ssi aplikasi my atm')
    print('silahkan pilih opsi di bawah ini')
    print('1. cek saldo')
    print('2. setor tunai')
    print('3. tarik tunai')
    print('4. cek riwayat')
    print('5. kelaur')
    while True:
        pilihan = input('silahkan piilih opsi: ')
        if pilihan =='1':
            cek_saldo()
        elif pilihan =='2':
            setor_tunai()
        elif pilihan =='3':
            tarik_tunai()
        elif pilihan =='4':
            cek_riwayat()
        elif pilihan =='5':
            keluar()
            break
        else:
            print('opsi anda tidak vallid')

#to do list + file handling
import os
import json
if os.path.exists('tugas.json'):
    with open('tugas.json', 'r') as file:
        tugas = json.load(file)
else:
    tugas = []
print('\ndaftar tugas')
print('1. tampilkan tugas')
print('2. tambah tugas')
print('3. kurangi tugas')
print('4. keluar')
while True:
    pilihan =input('silahkan masukkan pilihan anda: ')
    if pilihan == '1':
        if len(tugas)==0:
            print('mohon maaf anda belum memiki daftar tugas')
        else:
            for i, item in enumerate(tugas, start=1):
                print(f'{i}. {item}')
    elif pilihan == '2':
        tambah = input('masukkan nama tugas yang akan anda daftarkan: ')
        tugas.append(tambah)
        print(f'{tambah} telah berhasil di tambahkan')
    elif pilihan =='3':
        if len(tugas)==0:
            print('mohon maaf anda tidak memilki daftar tugas')
        else:
            tambah = input('masukkan nama tugas yang akan anda hanpus: ')
            if tambah in tugas:
                tugas.remove(tambah)
                print(f'{tambah} berhasil di hapus')
            else:
                print('mohon maaf barang tidak ada di daftar tugas')
    elif pilihan =='4':
        with open('tugas.json', 'w') as file:
            json.dump(tugas, file)
            break
