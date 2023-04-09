#Dalam bahasa pemrograman python, syntax atau statement yang digunakan untuk melakukan percabangan adalah: if, elif, dan else
#Di mana if merupakan kondisi utama, sedangkan elif adalah kondisi kedua atau ketiga hingga ke-x, sedangkan else adalah kondisi terakhir di mana semua kondisi sebelumnya tidak ada yang terpenuhi

#Blok if

if True:
  print('Kode program ini akan dieksekusi')

if False:
  print('Kode program ini tidak akan dieksekusi')

print('Kode program ini akan selalu dieksekusi karena tidak termasuk pada percabangan')

#Blok if.. else

nilai = 50

print('Nilai anda adalah:', nilai, '\n')

if nilai >= 70:
  print('Selamat, anda lulus!')
else:
  print('Maaf, anda tidak lulus.')

#atau bisa juga

nilai = int(input('Masukkan nilai anda: '))
print('Nilai anda adalah:', nilai, '\n')

if nilai >= 70:
  print('Selamat, anda lulus!')
else:
  print('Maaf, anda tidak lulus.')

#Blok if.. elif.. else

nilai = int(input('Masukkan nilai: '))

if nilai >= 90:
  print('Predikat A')
elif nilai >= 80:
  print('Predikat B')
elif nilai >= 60:
  print('Predikat C')
elif nilai >= 40:
  print('Predikat D')
else:
  print('Predikat E')

