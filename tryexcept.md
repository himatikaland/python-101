# PYTHON 101 BY HIMATIKA

## pengecualian dan kesalahan atau try and except

Try dan except adalah konstruksi dalam bahasa pemrograman Python yang digunakan untuk menangani kesalahan atau exception saat menjalankan program. Dalam try dan except, blok kode yang mungkin menyebabkan kesalahan ditempatkan dalam blok try, sementara blok kode yang akan dijalankan jika terjadi kesalahan ditempatkan dalam blok except. Contoh penggunaan try dan except adalah sebagai berikut:

```python
try:
    # blok kode yang mungkin menyebabkan kesalahan
    x = int(input("Masukkan angka: "))
    y = 10 / x
    print("Hasil pembagian adalah:", y)
except:
    # blok kode yang dijalankan jika terjadi kesalahan
    print("Terjadi kesalahan! Pastikan Anda memasukkan angka yang benar.")
```

Dalam contoh di atas, kita mencoba membagi 10 dengan angka yang dimasukkan oleh pengguna. Jika pengguna memasukkan angka yang benar, program akan berjalan tanpa masalah dan menampilkan hasil pembagian. Namun, jika pengguna memasukkan angka 0 atau angka yang tidak valid, program akan mengalami kesalahan. Dalam hal ini, blok kode dalam blok except akan dijalankan dan program akan menampilkan pesan kesalahan.

Anda juga dapat menentukan tipe exception tertentu yang ingin ditangani dan menampilkan pesan error yang spesifik. Contoh penggunaannya adalah sebagai berikut:

```python
try:
    # blok kode yang mungkin menyebabkan kesalahan
    x = int(input("Masukkan angka: "))
    y = 10 / x
    print("Hasil pembagian adalah:", y)
except ZeroDivisionError:
    # blok kode yang dijalankan jika terjadi ZeroDivisionError
    print("Terjadi kesalahan pembagian dengan nol!")
except ValueError:
    # blok kode yang dijalankan jika terjadi ValueError
    print("Terjadi kesalahan! Pastikan Anda memasukkan angka yang benar.")
except:
    # blok kode yang dijalankan jika terjadi kesalahan lainnya
    print("Terjadi kesalahan yang tidak diketahui!")
```

Dalam contoh di atas, kita menambahkan dua blok except tambahan untuk menangani dua jenis kesalahan yang berbeda: ZeroDivisionError dan ValueError. Dengan menentukan tipe exception tertentu yang ingin ditangani, kita dapat menampilkan pesan error yang lebih spesifik dan memudahkan debugging program.
