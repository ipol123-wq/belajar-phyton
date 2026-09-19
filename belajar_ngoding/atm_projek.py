#versi biasa dan simpel
saldo = 0
print('===ATM===')
print('1. Cek Saldo')
print('2. Setor Tunai')
print('3. Tarik Tunai')
print('4. Keluar')
while True:
    pilihan = input('pilih menu (1-4): ')
    if pilihan == '1':
        print(f'Total Saldo Anda Adalah :Rp {saldo}')
    elif pilihan=='2':
        jumlah = int(input('Silahkan Masukkan Jmlah Yang Akan Anda Setor; '))
        saldo += jumlah
        print(f'Rp{jumlah}, berhasil di tambahkan ke saldo')
        print(f'saldo sekarang: Rp{saldo}')

    elif pilihan=='3':
        jumlah = int(input('masukkan jumlah yang akan anda tarik: '))
        if jumlah <= saldo:
            saldo -= jumlah
            print(f'Rp{jumlah}, berhasil di tarik')
            print(f'sisa saldo Rp: {saldo}')
        else:
            print('saldo tidal bisa di tarik!!!')
    elif pilihan=='4':
        print('terima kasih telah berlayanan')
        break
    else:
        print('mohon maaf anda memasukkan kode yang salah')

#versi pakai pin
belanja = []
print('selamt datang di my toko')
print('silahkan pilih opsi di baawwah ini')
print('1. cek barang')
print('2. tambahkan barang')
print('3. kurangi barang')
print('4. keluar')
while True:
    pilihan = input('silahkan mpilih opsi')
    if pilihan =='1':
        if len(belanja) == 0:
            print('mohon maaaf anda belum memiiliki daftar belanja')
        else:
            print('daftar belanja')
            for i, barang in enumerate(belanja, start=1):
                print(f'{i}. {barang}')
    elif pilihan == '2':
        barang = input('silahkan masukkan nama barang yang ingin anda tambahkan: ')
        belanja.append(barang)
        print(f'{barang} telah berhasil di tambahkan')
    elif pilihan == '3':
        if len(belanja) == 0:
            print('mohon maaf anda belum memiliki daftar belanjaan')
        else:
            barang = input('silahkan masukkan nama barang yang ingin di hapus')
            if barang in belanja:
                belanja.remove(barang)
                print(f'{barang} berhasol di hapus')
            else:
                print('maaf belanja tidak ada di dalam daftar')
    elif pilihan == '4':
        print('teerima kasih telah berbelanja di toko kami')
        break
    else:
        print('maaf opsi yng anda masukkan tidak valid')

#panduan dalam bahasa manusia
#belanja = []
#→ Buat keranjang belanja kosong.
#while True
#→ Lakukan terus-menerus (sampai user pilih keluar).
#print(...)
#→ Tampilkan tulisan ke layar.
#input(...)
#→ Tanya ke user, lalu simpan jawabannya.
#if pilihan == "1"
#→ Jika user pilih 1, maka...
#elif pilihan == "2"
#→ Kalau bukan 1, tapi 2, maka...
#else
#→ Kalau bukan semuanya, maka...
#append
#→ Masukkan barang ke keranjang.
#remove
#→ Buang barang dari keranjang.
#for barang in belanja
#→ Untuk setiap barang yang ada di keranjang, lakukan sesuatu.
#break
#→ Berhenti mengulang.

#simulasi menghitung teman
teman = []
while True:
    print('n/===DAFTAR TEMAN===')
    print('1. Tampilkan Daftar Teman')
    print('2. Tambahkan Teman ')
    print('3. Hapus Teman ')
    print('4. keluar')
    pilihan = input('pilihan menu(1-4): ')
    if pilihan =='1':
        if len(teman)==0:
            print('mohon maaf anda belum mendaftarkan nama teman')
        else:
            print('n/ isi daftar teman ')
            for i, nama in enumerate(teman, start=1):
                print(f'{i}. {nama}')
    elif pilihan =='2':
        nama = input('masukkan nama teman: ')
        teman.append(nama)
        print(f"'{nama}, berhasil di tambahkan")
    elif pilihan =='3':
        if len(teman)==0:
            print('mohon maaf anda belum memiliki daftar teman yang bisa di hapus')
        if nama in teman:
                nama = input('masukkan nama teman yang akan di hapus: ')
                teman.remove(nama)
                print(f"'{nama}, berhasil di hapus")
        else:
            print('nama tidak di temukan')
    elif pilihan =='4':
        print('terima kasih')
        break

#versi function + parameter
def hitung_total(jumlah, harga):
    total = jumlah * harga
    return total
def tampilkan_struk(nama_barang, jumlah, harga, total):
    print('\n STRUK BELANJA')
    print(f'nama barang: {nama_barang}')
    print(f'jumlah barang: {jumlah}')
    print(f'harga barang: {harga}')
    print(f' total harga: {total}')

print('masukkan informsi')
nama_barang = input('silahkan masukkan nama barang')
jumlah = int(input('masukkan jumlah barang'))
harga = int(input('masukkan harga barang'))
total = hitung_total(jumlah, harga)
tampilkan_struk(nama_barang, jumlah, harga, total)
#\n berfungsi untuk seperti baris pemisah


#versi list
saldo = []
print('===ATM===')
print('1. cek saldo')
print('2. setor tunai')
print('3. tarik tunai')
print('4. keluar')
while True:
    pilihan = input('silahkan pilih menu: ')
    if pilihan =='1':
        if len(saldo)==0:
            print('mohon maaf saldo anda adalah 0' )
        else:
            print('isi saldo anda adalah')
            for i, jumlah in enumerate(saldo, start=1):
                print(f"'{i}. {jumlah}")

            print(f'total saldo anda adalah {sum(saldo)}')
    elif pilihan =='2':
        jumlah = int(input('silahkan masukkan jumlah yang akan anda setor: '))
        saldo.append(jumlah)
        print(f"'{jumlah}, berhasil di tambahkan ke saldo")
    elif pilihan =='3':
        jumlah = int(input('masukkan jumlah yang ingin anda tarik'))
        if jumlah <= saldo[0]:
            saldo[0] -= jumlah
            print(f'{jumlah}, berhasil di tarik')
            print(f'sisa saldo anda adalah, {saldo[0]}')
        else:
            print('maaf saldo tidak bissa di tarik')
    elif pilihan =='4':
        print('terima kasih telah berlayanan')
        break
    else:
        print('anda memasukkan kode yang salah')

#proyek pilihan list
saldo_total = [1000000, 500000]
print('SELAMAT DATANG DI APLIKASI MY ATM')
print('Silahkan pilih opsi di bawah ini')
print('1. cek saldo')
print('2. Setor tunai')
print('3. Tarik tunai')
print('4. keluar')
while True:
    pilihan = input('silahkan pilih menu: ')
    if pilihan =='1':
        print(f'saldo total anda adalah: Rp, {sum(saldo_total)}')
    elif pilihan=='2':
        jumlah = int(input('masukkan jumlah yang akan anda setor: '))
        saldo_total.append(jumlah)
        print(f'saldo total anda adalah: {sum(saldo_total)}')
    elif pilihan =='3':
        jumlah = int(input('masukkan nominal yang akan anda tarik'))
        if jumlah in saldo_total:
            saldo_total.remove(jumlah)
            print('saldo anda berhasil di tarik')
            print(f'sisa saldo anda adalah: {sum(saldo_total)}')

        else:
            print('mohon maaf pilihan nominal tidak sesuai')
    elif pilihan=='4':
        print('terima kasih telah menggunakan layanan kami')
        break
    else:
        print('maaf pilihan anda error')

#variasi
saldo_total = [1000000, 500000]
print('SELAMAT DATANG DI APLIKASI MY ATM')
print('Silahkan pilih opsi di bawah ini')
print('1. cek saldo')
print('2. Setor tunai')
print('3. Tarik tunai')
print('4. keluar')
while True:
    pilihan = input('silahkan pilih menu: ')
    if pilihan =='1':
        print(f'saldo total anda adalah: Rp, {sum(saldo_total)}')
    elif pilihan=='2':
        jumlah = int(input('masukkan jumlah yang akan anda setor: '))
        saldo_total.append(jumlah)
        print(f'saldo total anda adalah: {sum(saldo_total)}')
    elif pilihan =='3':
        jumlah = int(input('masukkan nominal yang akan anda tarik'))
        if jumlah <=0:
            print('nominal tidak valid')
        elif jumlah in saldo_total:
            saldo_total.remove(jumlah)
            print('saldo anda berhasil di tarik')
            print(f'sisa saldo anda adalah: {sum(saldo_total)}')
        else:
                print('mohon maaf pilihan tidak valid')
    elif pilihan=='4':
        print('terima kasih telah menggunakan layanan kami')
        break
    else:
        print('maaf pilihan anda error')

    #variasi
saldo_total = 0
pin_benar = 241124
kesempatan = 3
print('SELAMAT DATANG DI APLIKASI MY ATM')
print('silahkan masukkan pin anda')
while kesempatan > 0:
    pin = int(input('masukkan pin : '))
    if pin == pin_benar:
        print('pin benar')
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f'pin yang anda masukkan salah, sisa kesempatan: {kesempatan}')
        else:
            print('pin yang anda masukkan salah')
            print('kini akun anda telah terblokir')
            print('silahkan hubungi kostumer servis untuk perbaikan')
if kesempatan > 0:
    print('SELAMAT DATANG DI MY ATM')
    print('1. cek saldo')
    print('2. setor tunai')
    print('3. tarik tunai')
    print('4. keluar')
    while True:
        pilihan = int(input('silahkan pilih menu: '))
        if pilihan == 1:
            print(f'berikut adalah total saldo anda{saldo_total}')
        elif pilihan == 2:
            jumlah = int(input('masukkan nominal yang akan anda setor'))
            saldo_total += jumlah
            print(f'total yg anda setor adalah; {jumlah}')
            print(f'total saldo keseluruhan adalah: {saldo_total}')
        elif pilihan == 3:
            jumlah = int(input('masukan jumlah yang akan anda tarik'))
            if jumlah < 10000:
                print('mohon maaf nominal minimum penarikan adalah Rp10,000')
            elif jumlah >= 10000:
                saldo_total -= jumlah
                print('penarikan berhasil')
                print(f'nominal yg berhasil anda tarik adalah: {jumlah}')
                print(f'total saldo keseluruhan ; {saldo_total}')
        elif pilihan == 4:
            print('terima kasih telah menggunakan layanan kami')
        else:
            print('kode yg anda masukkan tidak valid')

#function
#Kode lebih rapi
#Tiap fitur terpisah (cek saldo, setor, tarik)
#Lebih gampang diperbaiki
#Kebiasaan bagus untuk ke depan


saldo_total = 0
pin_benar = 241124
kesempatan = 3

def cek_saldo():
    print(f'Total saldo anda adalah: Rp{saldo_total}')
def setor_tunai():
    global saldo_total
    jumlah = int(input('masukkan nominal yang akan anda setor: '))
    saldo_total += jumlah
    print(f'berhasil setor Rp {jumlah}')
    print(f'total saldo adalah Rp {saldo_total}')

def tarik_tunai():
    global saldo_total
    jumlah = int(input('masukkan nominal yang akan anda tarik: '))
    if jumlah <= saldo_total:
        saldo_total -= jumlah
        print(f'penarikan berhasil Rp {jumlah}')
        print(f'total saldo adalah Rp {saldo_total}')
    else:
        print('maaf saldo anda tidak cukup untuk melakukan penarikan')

print('SELAMAT DATANG DI MY ATM')
while kesempatan > 0:
    pin = int(input('harap masukkan pin anda: '))
    if pin == pin_benar:
        print('pin benar!')
        break
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f'pin yang anda masukkan salah, sisa kesempatan adalah: {kesempatan}')
        else:
            print('mohon maaf anda sudah tiga kali salah memasukkan pin')
            print('maka akun anda sekarang telah kami blokir!!!')
            print('hubungi kostumer servis untuk info lebih lanjut')
if kesempatan > 0:
    print('silahkan pilih menu di bawah ini')
    print('1. cek saldo')
    print('2. setor tunai')
    print('3. tarik tunai')
    print('4. keluar')
    while True:
        pilihan = input('silahkan pilih menu: ')
        if pilihan == '1':
            cek_saldo()
        elif pilihan == '2':
            setor_tunai()
        elif pilihan == '3':
            tarik_tunai()
        elif pilihan == '4':
            print('terima kasih telah menggunakan layanan kami')
            break
        else:
            print('pilihan tidak valid')

#veersi riwayawt
saldo = 0
riwayat = []
print('selamat datang di aplikasi my atm')
print('silahkan pilih opsi di bawh in')
print('1. cek saldo')
print('2. tambah pemasukan')
print('3. tambah pengeluaran')
print('4. lihaat riwayat')
print('5. keluar')
while True:
    pilihan = input('silahkan pilih opsi di aplikasi ')
    if pilihan =='1':
        print(f'total saldo anda adlah: {saldo}')
    elif pilihan == '2':
        jumlah = int(input('silahkan nominal yang akan anda tambahkan:  '))
        saldo += jumlah
        riwayat.append(f'pemasukan: Rp{jumlah}')
        print(f'{jumlah} berhasil di tambahkan')
        print(f'total saldo anda saat ini adalah {saldo}')

    elif pilihan == '3':
        jumlah = int(input('dilahkan masukkan jummllalh yag akan anda tarik: '))
        if jumlah <= saldo:
            saldo -= jumlah
            riwayat.append(f'penarikan: rp {jumlah}')
            print(f'{jumlah} berhsil di tarik')
            print(f'saldo and saaat ini addlah {saldo}')
        else:
            print('maaf saldo anda tidak mencukupia untuk melakukan penarikan')
    elif pilihan =='4':
        print('\n riwayat transaksi')
        if len(riwayat) ==0:
            print('maaf anda belum memiliki riwayat transaksi')
        else:
            for i, item in enumerate(riwayat, start=1):
                print(f'{i}. {item}')
    elif pilihan =='5':
        print('terima kasaih telah menggunakan layanan kami')
        break
    else:
        print('mohnn maaaf opsi yang anda pilih tidak valiid')

#atm dengan dictionary
saldo = 0
riwayat = []
print('\nselamat datang di apliksi my atm')
print('silahkan pilih opsi di bawah ini: ')
print('1. cek saldo')
print('2. tambah pemsukan')
print('3. tambah pengeluarran')
print('4. cek riwayat')
print('5. keluar')
while True:
    pilihan = input('silahkan masukkan osi yang anda pilih: ')
    if pilihan =='1':
        print(f'saldo anda adalah: {saldo}')
    elif pilihan =='2':
        jumlah = int(input('masukkan jumlah yang akan anda tambahakan: '))
        saldo += jumlah
        riwayat.append({
            'jenis': 'pemasukan',
            'jumlah': jumlah
        })
        print(f'{jumlah} telah berhasil di tambahkan')
        print(f'total saldo anda saat ini adalah: rp{saldo}')
    elif pilihan =='3':
        jumlah = int(input('silahkan masukkan jumlah yang akan anda taerik: '))
        if jumlah <= saldo:
            saldo -= jumlah
            riwayat.append({
                'jenis': 'pengeluaran',
                'jumlah': jumlah
            })
            print(f'{jumlah} berhaasil di tarik')
            print(f'sisa saldo anda adlah: Rp{saldo}')
        else:
            print('maaf saldo anda tidak mencukupi untuk melakukn penarikan')
    elif pilihan =='4':
        if len(riwayat)==0:
            print('mohon maaf anda belim malakukan tarnasksi')
        else:
            for i, item in enumerate(riwayat, start=1):
                print(f'{i}. {item['jenis']}, {item['jumlah']}' )
            print(f'total saldo anda adalh: Rp{saldo}')
    elif pilihan == '5':
        print('terima kasih telah menggunakan layanan kami')
        break
    else:
        print('maaf anda memasukkan opsi yang tidak valid')

