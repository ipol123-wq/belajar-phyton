data = {
    'nama': 'risal',
    'umur': 25,
    'kota': 'bantaeng'
}
data['jurusan']= 'ilmu falak'#menambahkan data
data['umur'] = 23#merubah data
del data['kota']#menghapus key dan value di data
ilmu = data.pop('jurusan')#menghaous key danvalue di data tapi meniympannya dalam sebuah variabel(ilmu)
print(data)

#keys()    → key  print(data.keys())     dict_keys(['nama', 'umur', 'kota'])
#values()  → value   print(data.values())    dict_values(['Risal', 25, 'Bantaeng'])
#items()   → key + value   print(data.items())    menampilkan keseluruhan

#loop key
data = {
    'nama': 'risal',
    'umur': 23,
    'kota': 'bantaeng'
}
for key in data:
    print(key)

#loop values
data = {
    'nama': 'risal',
    'umur': 23,
    'kota': 'bantaeng'
}
for values in data.values():
    print(values)

#menampilkan keseluruhan
data = {
    'nama': 'risal',
    'umur': 23,
    'kota': 'bantaeng'
}
for key, value in data.items():
    print(key, ':', value)

#versi rapi [akai f string
data = {
    'nama': 'risal',
    'umur': 23,
    'kota': 'bantaeng'
}
for key, value in data.items():
    print(f'{key} : {value}')

#list dalam dictionary
siswa = {
    'nama': 'Risal',
    'nilai': [80, 85, 90, 78]
}

print(siswa['nilai'])        # [80, 85, 90, 78]
print(siswa['nilai'][0])     # 80
print(siswa['nilai'][2])     # 90

#dictionary di dalam list
mahasiswa = [
    {'nama': 'Risal', 'umur': 23, 'jurusan': 'Ilmu Falak'},
    {'nama': 'Ayu', 'umur': 22, 'jurusan': 'IPA'},
    {'nama': 'Budi', 'umur': 24, 'jurusan': 'IPS'}
]
# Mengakses data
print(mahasiswa[0])                  # dictionary pertama
print(mahasiswa[0]['nama'])          # Risal
print(mahasiswa[1]['jurusan'])       # IPA

#looping list of dictionary
mahasiswa = [
    {'nama': 'Risal', 'umur': 23},
    {'nama': 'Ayu', 'umur': 22},
    {'nama': 'Budi', 'umur': 24}
]                                            #hasil risal-23
for mhs in mahasiswa:                               #ayu-22
    print(mhs['nama'], "-", mhs['umur'])            #budi-24

#variasi
mahasiswa = [
    {'nama': 'risal', 'kota': 'bantaeng'},
    {'nama': 'ayu', 'kota': 'makassar'},
    {'nama': 'budi', 'kota': 'gowa'}
]
for mhs in mahasiswa:
    print(mhs['nama'])#menampilkan nama saja

#variasi
mahasiswa = [
    {'nama': 'riril', 'nilai': 34},
    {'nama': 'rehan', 'nilai': 43},
    {'nama': 'aldi', 'nilai': 18}
]
for mhs in mahasiswa:
    print(mhs['nama'], 'mendapatkan nilai', mhs['nilai'])

#versi sederhana
mahasiswa = [
    {'nama': 'risal', 'kota': 'bantaeng'},
    {'nama': 'ayu', 'kota': 'makassar'},
    {'nama': 'budi', 'kota': 'gowa'}
]
for mhs in mahasiswa:
    print(mhs['nama'], "tinggal di", mhs['kota'])

#versi f string
mahasiswa = [
    {'nama': 'risal', 'kota': 'bantaeng'},
    {'nama': 'ayu', 'kota': 'makassar'},
    {'nama': 'budi', 'kota': 'gowa'}
]
for mhs in mahasiswa:
    print(f'{mhs['nama']} tinggal di {mhs['kota']}')

#versi terarah dan sederhana, ke risal misalnya
mahasiswa = [
    {'nama': 'risal', 'kota': 'bantaeng'},
    {'nama': 'ayu', 'kota': 'makassar'},
    {'nama': 'budi', 'kota': 'gowa'}
]
print(mahasiswa[0]['nama'], 'tinggal di', mahasiswa[0]['kota'])

#cari berdasarkan nama
mahasiswa = [
    {'nama': 'risal', 'kota': 'bantaeng'},
    {'nama': 'ayu', 'kota': 'makassar'},
    {'nama': 'budi', 'kota': 'gowa'}
]
for mhs in mahasiswa:
    if mhs['nama'] =='risal':
        print(mhs['nama'], 'tinggal di', mhs['kota'])
        #atau bisa juga menggunakan f string
        print(f'{mhs['nama']} tinggal di {mhs['kota']}')

#
mahasiswa = [
    {'nama': 'Risal', 'nilai': 85},
    {'nama': 'Ayu', 'nilai': 90},
    {'nama': 'Budi', 'nilai': 78}
]
print(mahasiswa[1]['nama'], '-', mahasiswa[1]['nilai'])

#penjelasan lopp. loop adalah untuk menampilkan semua yang ada di list, kalau tidak maka akan eror.
#kalau gak pakek loop bisa jika yg hanya mau di tampilkan 1 isi saja di dalam list

riwayat = [
    {'jenis': 'pemasukan', 'jumlah': 50000},
    {'jenis': 'pengelluaran', 'jumlah': 20000}
]
for i, item in enumerate(riwayat, start=1):
    print(f'{i}. {item['jenis']}-Rp{item['jumlah']}')

