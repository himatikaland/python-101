# PYTHON 101 BY HIMATIKA

## Dalam Python, ada bermacam-macam tipe data, berikut adalah penjelasan mengenai tipe data yang umum digunakan dalam Python

1. Bilangan (Numbers): Python menyediakan tiga jenis bilangan, yaitu bilangan bulat (integer), bilangan pecahan (float), dan bilangan kompleks (complex).

2. Bilangan bulat (integer): Bilangan bulat adalah angka tanpa desimal. Contoh: 5, -3, 0.

3. Bilangan pecahan (float): Bilangan pecahan adalah angka dengan desimal. Contoh: 3.14, -0.5, 1.0.

4. Bilangan kompleks (complex): Bilangan kompleks memiliki bagian real dan imajiner. Contoh: 3+4j, -1+2.5j, 1-1j.

5. Teks (Text): Python menggunakan tipe data string (str) untuk menampung teks. String dapat diapit oleh tanda kutip tunggal atau ganda. Contoh: 'Halo, Dunia!', "Python", '1234'.

6. Boolean (bool): Tipe data boolean memiliki dua nilai: True dan False. Boolean digunakan dalam operasi logika dan perbandingan. Contoh: 5 > 3 akan menghasilkan True, sementara 2 == 4 akan menghasilkan False.

7. NoneType (None): None adalah nilai khusus dalam Python yang menunjukkan ketiadaan nilai atau variabel. Contoh penggunaan None: x = None untuk menetapkan nilai awal variabel x.

8. List (list): List adalah koleksi berurutan yang dapat menyimpan berbagai jenis data. List dapat diubah (mutable) dan menggunakan tanda kurung siku []. Contoh: [1, 'dua', 3.14, True].

9. Tuple (tuple): Tuple mirip dengan list, tetapi tidak dapat diubah (immutable). Tuple menggunakan tanda kurung (). Contoh: (1, 'dua', 3.14, True).

10. Range (range): Range adalah urutan angka yang tidak dapat diubah (immutable). Range sering digunakan dalam perulangan. Contoh: range(5) akan menghasilkan urutan angka 0, 1, 2, 3, dan 4.

11. Set (set): Set adalah koleksi tidak berurutan yang tidak mengizinkan duplikat. Set menggunakan tanda kurung kurawal {}. Contoh: {1, 2, 3, 4}.

12. Frozenset (frozenset): Frozenset mirip dengan set, tetapi tidak dapat diubah (immutable). Contoh: frozenset([1, 2, 3, 4]).

13. Dictionary (dict): Dictionary adalah koleksi berpasangan kunci-nilai yang tidak berurutan. Dictionary menggunakan tanda kurung kurawal {} dan tanda titik dua : untuk memisahkan kunci dan nilai. Contoh: `{'nama': 'Budi', 'umur': 25, 'pekerjaan': 'Programmer'}`.

### dibawah ini jarang digunakan

- Array (array.array): Array adalah koleksi berurutan dari elemen dengan tipe data yang sama. Array lebih efisien dalam hal penggunaan memori daripada list. Untuk menggunakan array, kamu perlu mengimpor modul array. Contoh: from array import array; a = array('i', [1, 2, 3, 4]).

- Byte (bytes): Byte adalah urutan bilangan bulat dalam rentang 0-255, yang tidak dapat diubah (immutable). Byte digunakan untuk data biner seperti gambar atau file audio. Contoh: b = b'Halo Dunia'.

- Bytearray (bytearray): Bytearray mirip dengan byte, tetapi dapat diubah (mutable). Contoh: ba = bytearray(b'Halo Dunia').

- Memoryview (memoryview): Memoryview adalah objek yang memungkinkan kamu mengakses memori dari objek lain tanpa menggandakan data tersebut. Memoryview berguna untuk pengolahan data yang efisien dalam struktur data besar. Contoh: mv = memoryview(bytearray(b'Halo Dunia')).

beberapa contoh berikut:

```python
angka_bulat = 42 # number
angka_float = 3.14 #float
angka_kompleks = 3+4j #complex
teks_string = "Halo, Dunia!" #string
boolean = True #boolean
none = None #NoneType
data_list = [1, 2, 3, 4] #list atau array
data_tuple = (1, 2, 3, 4) #tuple
range_angka = range(5) #range
set_angka = {1, 2, 3, 4} #set
frozenset_angka = frozenset([1, 2, 3, 4]) #frozenset
dictionary = {'nama': 'Budi', 'umur': 25, 'pekerjaan': 'Programmer'} #dictionary
array_angka = array('i', [1, 2, 3, 4]) #array
byte_angka = b'Halo Dunia' #byte
bytearray_angka = bytearray(b'Halo Dunia') #bytearray
memoryview_angka = memoryview(bytearray(b'Halo Dunia')) #memoryview
```

referensi:

[website](https://realpython.com/python-data-types/)
