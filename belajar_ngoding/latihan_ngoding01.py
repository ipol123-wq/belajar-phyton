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


