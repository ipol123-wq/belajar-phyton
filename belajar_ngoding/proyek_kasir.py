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


tugas= []
print('silahkan masukkan opsi di bawah ini')
print('1. cek saldo')
print('2. tambah daftar tugas')
print('3. kurangi daftar tugas')
print('4. keluar')
while True:
    pilihan = input('silahkan mmasukkan opsi: ')
    if pilihan == '1':
        if len(tugas)==0:
            print('mohon maaf anda belum memilikil daftar tugas')
        else:
            print('\n DAFTAR TUGAS')
            for i, makan in enumerate(tugas, start=1):
                print(f'{i}. {makan}')
    elif pilihan == '2':
        daftar = input('silahkan masukkann tugas yang ingn anda tambahkan')
        tugas.append(daftar)
        print(f'{daftar} berhasil di tambahkan')
    elif pilihan =='3':
        if len(tugas)==0:
            print('mohon maaf anda belum memilki daftar tugas')
        else:
            daftar = input('silahkan masukkan tugas yang akan anda hapus')
            tugas.remove(daftar)
            print(f'{daftar} berhasil di hapus dari tugas')
    elif pilihan =='4':
        print('terima kasih telah menggunakan layana kami')
        break
    else:
        print('mohon maaf opsi yyang anda masukkan salah')

#variasi
belanja = []
riwayat = []
print('selamat datang di my atm')
print('dilahkan pilih opsi di bawah ini')
print('1. cek total barang')
print('2. tambahkan barang')
print('3. kurangi barang')
print('4, cek riwayat ')
print('5. keluar')
while True:
    pilihan = input('slahkan pilih opsi: ')
    if pilihan =='1':
        if len(belanja)==0:
            print('mohon maaf anda belum memilki daftar belanja')
        else:
            print('\nberikut daftar belanja anda')
            for i, barang in enumerate(belanja, start=1):
                print(f'{i}. {barang}')
    elif pilihan =='2':
        barang = input('silahkan masukkan belanja yang akan anda tambahkan')
        belanja.append(barang)
        riwayat.append(f'penambahan: {barang}')
        print(f'{barang} berhasil di tambahkan')
    elif pilihan =='3':
        if len(belanja)==0:
            print('maaf anda beluum memiliki daftar belanja untuk di hapus')
        else:
            barang = input('silahkan masukkan daftar belanja yang akan anda hapua')
            if barang in belanja:
                belanja.remove(barang)
                riwayat.append(f' pengurangan: {barang}')
                print(f'{barang} berhasil di ghapus dari daftar')
            else:
                print('maaf barang tidak termasuk dalam daftar')
    elif pilihan =='4':
        print('\nriwayat transaksi')
        if len(belanja)==0:
            print('maaf anda belum memiliki transaksi')
        else:
            for i, barang in enumerate(riwayat, start=1):
                print(f'{i}. {barang}')
    elif pilihan =='5':
        print('terima  kasih telah menggunakan layanan kami')
    else:
        print('mohon maaf opsi yang anda masukkan salah')
