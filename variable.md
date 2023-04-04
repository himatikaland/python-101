# PYTHON 101 BY HIMATIKA

## Dalam Python ada banyak cara variable dapat didefinisikan. Berikut adalah penjelasan mengenai cara-cara tersebut

1. Pengenalan variable: variable dalam Python adalah label yang merujuk pada suatu nilai dalam memori komputer. variable memungkinkan kita untuk menyimpan, mengakses, dan mengubah nilai dalam kode kita.

2. Membuat variable: Dalam Python, kamu dapat membuat variable dengan menetapkan nilai ke suatu nama menggunakan tanda sama dengan =. Contoh: x = 5, di mana x adalah nama variable dan 5 adalah nilai yang ditugaskan ke variable tersebut.

3. Mengganti Nilai variable: Kamu dapat mengganti nilai variable dengan menetapkan nilai baru ke nama variable yang sama. Contoh: x = 5 kemudian x = 7, di mana nilai variable x telah diubah dari 5 menjadi 7.

4. Menggunakan variable: variable dapat digunakan dalam berbagai operasi dan ekspresi. Contoh: x = 5, y = 7, dan z = x + y, di mana nilai z akan menjadi 12.

5. Menghapus variable: Kamu dapat menghapus variable menggunakan perintah del. Contoh: del x, yang akan menghapus variable x dari memori.

6. Jenis Data dan variable: Setiap variable dalam Python memiliki jenis data yang berkaitan dengan nilai yang disimpan. Beberapa jenis data bawaan Python meliputi int, float, str, bool, dan list. Python bersifat dinamis, yang berarti kamu dapat mengubah jenis data variable dengan menetapkan nilai baru dengan jenis data yang berbeda.

7. Aturan Penamaan variable: variable dalam Python harus diawali dengan huruf atau garis bawah \_, diikuti oleh huruf, angka, atau garis bawah. variable juga harus bersifat deskriptif dan menggunakan gaya snake_case (huruf kecil dengan garis bawah antar kata).

8. Konstanta: Konstanta adalah variable yang nilai dan jenis datanya tidak berubah sepanjang waktu. Python tidak memiliki dukungan bawaan untuk konstanta, tetapi konvensi yang umum digunakan adalah menulis nama variable konstanta dengan huruf kapital dan garis bawah sebagai pemisah kata.

9. variable Global dan Lokal: variable dalam Python dapat berupa global (tersedia di seluruh program) atau lokal (hanya tersedia dalam ruang lingkup tertentu, seperti fungsi). Gunakan kata kunci global untuk mengakses atau mengubah variable global dari dalam suatu fungsi.

berikut contohnya:

```python
# variable global
panjang_kotak = 10
lebar_kotak = 5
luas = panjang_kotak * lebar_kotak
print(luas)
# hasilnya 50

# mengubah variable global
panjang_kotak = 20
luas = panjang_kotak * lebar_kotak
print(luas)
# hasilnya 100

# Menghapus variable panjang_kotak, lebar_kotak, dan luas
del panjang_kotak
del lebar_kotak
del luas

# Mencoba mencetak variable yang telah dihapus akan menyebabkan NameError
# print(panjang_kotak)  # Jangan jalankan baris ini, akan menyebabkan NameError

# membuat variable lokal
def luas_segitiga(panjang_segitiga, lebar_segitiga):
    # variable lokal
    luas = panjang_segitiga * lebar_segitiga / 2
    print("Luas segitiga (di dalam fungsi):", luas)

panjang = 5
lebar = 10

# Memanggil fungsi untuk menghitung dan mencetak luas segitiga
luas_segitiga(panjang, lebar)

# Mencoba mengakses variable lokal 'luas' di luar fungsi akan menyebabkan NameError
# print("Luas segitiga (di luar fungsi):", luas)  # Jangan jalankan baris ini, akan menyebabkan NameError
```
