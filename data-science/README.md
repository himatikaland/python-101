# Data Science

## Apa itu Data Science?

Pendeknya, Data science adalah cara untuk mengekstraksi informasi dan pengetahuan dari data dengan menggunakan metode ilmiah. Pada dasarnya, data science mencoba untuk menjawab pertanyaan-pertanyaan yang timbul dari data, seperti "apa yang terjadi?" atau "mengapa hal itu terjadi?" atau "apa yang mungkin terjadi selanjutnya?".

## Lalu apa itu Machine Learning?

Sedangkan Machine learning adalah suatu teknik dalam data science yang menggunakan algoritma dan model statistik untuk membuat komputer dapat belajar dari data dan melakukan tugas-tugas tertentu tanpa perlu diberi instruksi secara eksplisit. Dengan kata lain, machine learning adalah salah satu cara untuk menerapkan data science dalam praktik.

Dalam konteks data science, machine learning digunakan untuk memprediksi atau mengklasifikasikan suatu data berdasarkan pola yang ditemukan dalam data itu sendiri. Machine learning dapat digunakan untuk memperkirakan harga rumah berdasarkan ukurannya, mengklasifikasikan email sebagai spam atau bukan, atau bahkan untuk memprediksi hasil pemilihan umum berdasarkan data polling.

Jadi, data science dan machine learning sangat berkaitan erat karena machine learning adalah bagian penting dari data science, yang membantu kita memanfaatkan informasi dari data dengan cara yang lebih efektif dan efisien.

## Sejarah Machine Learning

Alan Turing adalah seorang matematikawan dan ahli komputer asal Inggris yang hidup pada abad ke-20. Ia dikenal sebagai "bapak ilmu komputer" karena kontribusinya pada pengembangan komputer modern dan penyelesaian Enigma, mesin sandi yang digunakan oleh Jerman selama Perang Dunia II. Kontribusi utamanya dalam machine learning adalah melalui konsep yang disebut "Turing Learning" dan ide dasar yang mendasari "Turing Test."

1. Turing Learning: Turing Learning merupakan suatu metode yang dikembangkan berdasarkan konsep yang diajukan oleh Alan Turing. Dalam metode ini, sistem pembelajaran mesin diberi tugas untuk membedakan antara dua jenis data yang diberikan. Sistem ini kemudian mempelajari karakteristik masing-masing data dan mengembangkan suatu model yang dapat membedakan kedua jenis data tersebut. Proses ini menekankan pada pembelajaran tak berawak atau unsupervised learning. Konsep Turing Learning menjadi dasar bagi pengembangan teknik-teknik machine learning yang lebih canggih.

2. Turing Test: Turing Test merupakan salah satu kontribusi terpenting Turing dalam bidang kecerdasan buatan. Turing Test dirancang untuk mengevaluasi apakah suatu sistem kecerdasan buatan memiliki kemampuan berpikir yang setara dengan manusia atau tidak. Meskipun bukan secara langsung berhubungan dengan machine learning, Turing Test mempengaruhi perkembangan kecerdasan buatan, termasuk machine learning, dengan memberikan kerangka evaluasi yang penting.

Turing juga dikenal sebagai bapak ilmu komputer, dan kontribusinya dalam bidang komputasi, kriptografi, dan logika matematika telah membentuk dasar bagi pengembangan teknologi informasi dan machine learning seperti yang kita kenal sekarang.
Enigma adalah mesin sandi elektromekanik yang digunakan oleh Jerman untuk mengenkripsi pesan-pesan rahasia selama Perang Dunia II. Pesan-pesan ini dianggap tidak mungkin dipecahkan oleh pasukan Sekutu, yang membuat komunikasi Jerman terlindungi dari penyadapan.

Turing dikenal karena berhasil memecahkan Enigma, sebuah pencapaian yang dianggap krusial dalam perang melawan Jerman. Turing dan timnya di Bletchley Park, Inggris, berhasil membuat mesin yang dapat memecahkan kode-kode Enigma. Mereka melakukannya dengan menganalisis pola-pola dalam pesan-pesan sandi yang diterima, dan kemudian mencoba berbagai kombinasi kunci sandi sampai mereka menemukan yang tepat.

Kontribusi Turing dalam memecahkan Enigma dan pengembangan komputer modern sangat penting, karyanya terus dihormati dan diapresiasi oleh para ilmuwan dan teknologi informasi hingga saat ini.

!["Ilustrai Alan Turing dari film "The Imitation Game""](https://api.time.com/wp-content/uploads/2014/11/the-imitation-game.jpg)
_Ilustrai Alan Turing dari film "The Imitation Game"_

## Pentingnya Machine Learning

Machine learning atau Pembelajaran Mesin adalah teknologi yang memungkinkan mesin atau komputer untuk belajar dari data dan memprediksi hasil yang diinginkan tanpa perlu diprogram secara eksplisit. Dalam era digital saat ini, data menjadi sangat banyak dan kompleks, sehingga membuat manusia kesulitan untuk mengambil keputusan yang tepat dan cepat. Dalam hal ini, mesin atau komputer dapat membantu memproses data dan memberikan hasil prediksi yang akurat dan cepat.

## Mengapa Python menjadi pilihan populer untuk melakukan Pembelajaran Mesin?

1. Mudah dipelajari dan digunakan:
   Python dirancang untuk mudah dipelajari dan digunakan, sehingga cocok untuk pemula dalam pembelajaran mesin.

2. Open-source dan komunitas besar:
   Python bersifat open-source, yang berarti dapat digunakan secara gratis dan bebas diunduh. Selain itu, Python juga memiliki komunitas pengguna yang besar dan aktif yang terus mengembangkan library dan tools untuk mendukung pengembangan model pembelajaran mesin.

3. Library Pembelajaran Mesin yang Luas:
   Python memiliki library Pembelajaran Mesin yang sangat luas, seperti scikit-learn, TensorFlow, Keras, dan PyTorch, yang memungkinkan para pengguna untuk memilih algoritma dan teknik yang sesuai dengan kebutuhan mereka.

4. Kode yang Mudah Dibaca:
   Kode Python cenderung lebih mudah dibaca dan dimengerti daripada bahasa pemrograman lainnya, sehingga memudahkan kolaborasi dan pemeliharaan kode.

Dengan kombinasi mudahnya penggunaan Python dan kaya akan library Pembelajaran Mesin, banyak pengembang dan perusahaan menggunakan Python untuk membuat model Pembelajaran Mesin yang dapat memproses data besar dan menghasilkan hasil prediksi yang akurat. Oleh karena itu, Pembelajaran Mesin menjadi penting dan Python menjadi pilihan populer untuk melakukan Pembelajaran Mesin dalam era digital saat ini.

## Apa itu Scikit-Learn?

### Open-source ML library untuk Python. Dibuat dengan NumPy, SciPy, dan Matplotlib.

Scikit-learn adalah sebuah perpustakaan di Python yang menyediakan banyak algoritma pembelajaran yang tidak terawasi dan terawasi. Ini dibangun di atas beberapa teknologi yang mungkin sudah Anda kenal, seperti NumPy, pandas, dan Matplotlib!

Fungsi yang disediakan oleh scikit-learn termasuk:

- Regresi, termasuk Regresi Linier dan Logistik
- Klasifikasi, termasuk K-Nearest Neighbors
- _Clustering_, termasuk K-Means dan K-Means++
- Seleksi model
- Pra-pemrosesan, termasuk Min-Max

contoh bentuk kecilnya ialah:

```python
sklearn.linear_model.LinearRegression()
```

adalah model Regresi Linier di dalam modul linear_model dari sklearn.

Kekuatan scikit-learn akan sangat membantu dalam membuat program Machine Learning yang tangguh.

## Lalu apa itu Training data, validation, testing, dan evaluasi model?

Training data adalah data yang digunakan untuk melatih model machine learning. Model machine learning akan belajar dari training data ini dan mencoba menemukan pola dalam data tersebut. Training data terdiri dari input dan output yang sudah diketahui atau yang sudah dilabeli.

Validation adalah proses untuk mengevaluasi performa model machine learning pada data yang tidak digunakan untuk training. Validation data biasanya digunakan untuk melakukan tuning parameter pada model seperti learning rate, jumlah iterasi, dan lain-lain.

Testing data adalah data yang digunakan untuk menguji performa model setelah model telah dilatih pada training data dan telah di-validasi pada validation data. Testing data harus berbeda dengan training dan validation data, sehingga dapat memberikan gambaran yang akurat tentang performa model pada data yang belum pernah dilihat oleh model sebelumnya.

Evaluasi model adalah proses untuk menentukan seberapa baik model machine learning dalam memprediksi output dari input yang belum pernah dilihat sebelumnya. Evaluasi model dapat dilakukan dengan menggunakan berbagai metrik seperti akurasi, presisi, recall, F1-score, dan lain-lain. Evaluasi model dapat membantu kita menentukan apakah model sudah cukup baik atau perlu ditingkatkan kualitasnya.

contoh kodingnya:

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Membuat data
X = np.random.rand(100, 1)
y = 2 + 3 * X + np.random.rand(100, 1)

# Membagi data menjadi training, validation, dan testing data dengan rasio 60:20:20
X_train, X_valtest, y_train, y_valtest = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_valtest, y_valtest, test_size=0.5, random_state=42)

# Melatih model Linear Regression pada training data
model = LinearRegression()
model.fit(X_train, y_train)

# Mean squared error (MSE) pada validation data dan testing data adalah metrik evaluasi untuk mengevaluasi performa model machine learning
# dalam memprediksi output dari input yang belum pernah dilihat sebelumnya pada data yang berbeda.

# Mengevaluasi model pada validation data
y_pred = model.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
print("Mean squared error pada validasi data:", mse)

# Menguji performa model pada testing data
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error pada testing data:", mse)

# Semakin kecil nilai MSE pada validation data dan testing data,
# semakin baik performa model dalam memprediksi output pada data yang belum pernah dilihat sebelumnya.
```

## Machine Learning dibagi menjadi 2 jenis, yaitu:

- Supervised Learning (Pembelajaran Terpandu)
- Unsupervised Learning (Pembelajaran Tanpa Pengawasan)

### Supervised Learning

Supervised Learning adalah di mana data diberi label dan program belajar untuk memprediksi output dari data input. Sebagai contoh, algoritma pembelajaran terpandu untuk mendeteksi penipuan kartu kredit akan mengambil sejumlah transaksi yang direkam sebagai input. Untuk setiap transaksi, program akan memprediksi apakah itu penipuan atau tidak.

Masalah pembelajaran terpandu dapat dikelompokkan lebih lanjut menjadi masalah regresi dan klasifikasi.

**Regresi**:
Dalam masalah regresi, kita mencoba untuk memprediksi output yang bernilai kontinu. Contohnya adalah:

Berapa harga perumahan di Jakarta?
Berapa nilai dari cryptocurrency?

**Klasifikasi**:
Dalam masalah klasifikasi, kita mencoba untuk memprediksi sejumlah nilai diskrit. Contohnya adalah:

Apakah ini gambar manusia atau gambar AI?
Apakah email ini spam?

contoh koding berikut untuk klasifikasi

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Membuat DataFrame dengan kalimat tentang nasi goreng
data = pd.DataFrame({
    'kalimat': [
        'Nasi goreng ini enak sekali',
        'Saya suka nasi goreng pedas',
        'Nasi goreng itu makanan favoritku',
        'Kemarin saya makan nasi goreng di warung dekat kantor',
        'Nasi goreng biasanya dijadikan menu sarapan',
        'Nasi goreng kampung memiliki rasa yang khas',
        'Nasi goreng menjadi makanan yang populer di seluruh dunia',
        'Saat ini saya sedang belajar membuat nasi goreng yang enak',
        'Banyak orang memilih nasi goreng sebagai makanan cepat saji',
        'Tadi pagi saya makan nasi goreng spesial',
        'Nasi gorengnya hambar',
        'Nasi goreng yang saya pesan terlalu asin',
        'Saya tidak suka nasi goreng dengan telur ceplok'
    ],
    'label': [
        'positif',
        'positif',
        'positif',
        'positif',
        'positif',
        'positif',
        'positif',
        'positif',
        'positif',
        'positif',
        'negatif',
        'negatif',
        'negatif'
    ]
})

# Ekstraksi feature menggunakan CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['kalimat'])

# Inisialisasi model Naive Bayes
model = MultinomialNB()

# Melatih model menggunakan dataset dan label
model.fit(X, data['label'])

# Prediksi sentimen kalimat baru
new_sentence = "nasi goreng ini spesial sekali"
X_new = vectorizer.transform([new_sentence])
predicted_label = model.predict(X_new)

if predicted_label == "positif":
    print("Teks diatas positif")
else:
    print("Teks diatas negatif")
```

### Unsupervised Learning

Unsupervised Learning adalah jenis machine learning di mana program belajar struktur bawaan dari data berdasarkan contoh yang tidak diberi label.

Clustering adalah pendekatan unsupervised machine learning yang umum digunakan untuk menemukan pola dan struktur dalam data yang tidak diberi label dengan mengelompokkannya menjadi beberapa cluster.

Beberapa contoh penggunaan dari unsupervised learning dan clustering antara lain:

- Sosial media mengelompokkan topik-topik dalam berita untuk feed pengguna
- Situs belanja online mengelompokkan pengguna untuk memberikan rekomendasi
- Mesin pencari mengelompokkan objek yang serupa dalam satu cluster
- Untuk memberikan gambaran cepat, kami akan menunjukkan contoh dari unsupervised learning.

contoh koding berikut untuk algoritma K-Means Clustering

```python
# Impor modul 'KMeans' dari paket 'sklearn.cluster', modul 'make_blobs' dari paket 'sklearn.datasets',
# dan modul 'pyplot' dari paket 'matplotlib' yang akan digunakan untuk memvisualisasikan hasil clustering.

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Membuat dataset
# Buat dataset dengan 600 sample data dengan 6 pusat dan deviasi standar 0.6 menggunakan fungsi 'make_blobs' dari modul 'sklearn.datasets'.
# Variabel '_ (underscore)' digunakan untuk menampung nilai yang tidak digunakan,
# karena fungsi 'make_blobs' mengembalikan 2 nilai yaitu data dan label.

X, _ = make_blobs(n_samples=600, centers=6, cluster_std=0.6, random_state=0)

# Inisialisasi objek 'kmeans' dengan parameter 'n_clusters=6' dan
# lakukan training model dengan memanggil fungsi 'fit' pada objek 'kmeans' dengan parameter 'X'.
kmeans = KMeans(n_clusters=6)
kmeans.fit(X)

# Prediksi kelompok data menggunakan model 'kmeans' dengan memanggil fungsi 'predict' pada objek 'kmeans' dengan parameter 'X'.
y_kmeans = kmeans.predict(X)

# Menampilkan hasil clustering
# Visualisasikan hasil clustering dengan scatter plot menggunakan fungsi 'scatter' pada objek 'pyplot'
# dengan parameter 'X[:, 0]' dan 'X[:, 1]' sebagai sumbu x dan y, 'c=y_kmeans' untuk menentukan warna
# masing-masing titik berdasarkan kelompok yang dihasilkan oleh model, 's=50' untuk ukuran titik,
# dan 'cmap='hsv'' untuk memilih skema warna.
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='hsv')

#Buat variabel 'centers' untuk menampung nilai koordinat dari pusat-pusat kelompok yang dihasilkan oleh model 'kmeans'
# menggunakan atribut 'cluster_centers_' dari objek 'kmeans'.
centers = kmeans.cluster_centers_

# Visualisasikan pusat-pusat kelompok dengan scatter plot menggunakan fungsi 'scatter' pada objek 'pyplot'
# dengan parameter 'centers[:, 0]' dan 'centers[:, 1]' sebagai koordinat titik pusat, 'c='black'' untuk warna titik pusat,
# 's=200' untuk ukuran titik pusat, dan 'alpha=0.5' untuk tingkat transparansi.
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=600, alpha=0.6)

# ambahkan judul pada gambar dengan menggunakan fungsi 'title' pada objek 'pyplot' dengan parameter 'Contoh K-Means Clustering'
plt.title('Contoh K-Means Clustering')

# tampilkan hasil clustering dengan memanggil fungsi 'show' pada objek 'pyplot'.
plt.show()
```

Ringkasan

Kita telah membahas perbedaan antara pembelajaran terawasi (supervised learning) dan pembelajaran tanpa pengawasan (unsupervised learning):

Pembelajaran terawasi (supervised learning): data diberi label dan program belajar untuk memprediksi keluaran dari data masukan.
Pembelajaran tanpa pengawasan (unsupervised learning): data tidak diberi label dan program belajar untuk mengenali struktur bawaan dalam data masukan.

## Proses Machine Learning

1. Mengumpulkan Data
   Langkah pertama dalam membangun model pembelajaran mesin adalah mengumpulkan data yang relevan dan berkualitas. Data yang baik akan mencakup berbagai contoh yang mencerminkan situasi dunia nyata yang ingin Anda modelkan. Anda mungkin perlu mengumpulkan data dari sumber yang berbeda, seperti basis data, API, atau web scraping. Pastikan untuk mematuhi aturan dan peraturan saat mengumpulkan data.

2. Eksplorasi Data
   Setelah mengumpulkan data, Anda perlu memahami karakteristik dan struktur data. Ini melibatkan visualisasi data, mengidentifikasi tren, menghitung statistik deskriptif, dan mencari hubungan antara fitur. Eksplorasi data membantu Anda mendapatkan intuisi tentang data dan membantu dalam pengambilan keputusan tentang pemilihan fitur dan model yang tepat.

3. Pra-pemrosesan Data
   Data mentah seringkali perlu dibersihkan dan diproses sebelum digunakan untuk melatih model. Beberapa langkah pra-pemrosesan yang umum termasuk:

   - Mengatasi nilai yang hilang: Anda dapat mengisi nilai yang hilang dengan statistik seperti rata-rata atau median, atau menggunakan metode imputasi yang lebih canggih.
   - Transformasi data: Beberapa algoritma bekerja lebih baik dengan data yang diskala dengan cara tertentu. Anda mungkin perlu menerapkan transformasi logaritmik, kuadrat, atau normalisasi pada data Anda.
   - Pengkodean variabel kategori: Mengonversi variabel kategorikal (misalnya, warna atau jenis) menjadi bentuk numerik yang dapat diterima oleh algoritma pembelajaran mesin.

4. Pemilihan Fitur
   Fitur yang baik sangat penting untuk keberhasilan model pembelajaran mesin. Anda perlu memilih fitur yang informatif dan relevan dengan masalah yang Anda coba selesaikan. Beberapa teknik pemilihan fitur meliputi:

   - Korelasi fitur dengan target: Pilih fitur yang memiliki korelasi yang kuat dengan variabel target.
   - Pengurangan dimensi: Gunakan teknik seperti analisis komponen utama (PCA) atau t-Distributed Stochastic Neighbor Embedding (t-SNE) untuk mengurangi jumlah fitur sambil mempertahankan informasi penting.
   - Metode berbasis model: Gunakan model pembelajaran mesin, seperti pohon keputusan atau regresi Lasso, untuk menentukan fitur yang penting.

5. Membagi Data
   Untuk melatih dan mengevaluasi model, Anda perlu membagi data Anda menjadi set pelatihan dan set pengujian. Set pelatihan digunakan untuk melatih model, sedangkan set pengujian digunakan untuk mengevaluasi kinerja model. Umumnya, 70-80% data digunakan untuk pelatihan, dan sisanya digunakan untuk pengujian.

6. Pelatihan Model
   Setelah memilih algoritma yang tepat dan fitur yang relevan, Anda dapat melatih model pembelajaran mesin Anda menggunakan set pelatihan. Pelatihan model melibatkan menyesuaikan parameter model untuk meminimalkan kesalahan antara prediksi model dan nilai sebenarnya dari variabel target. Beberapa algoritma populer meliputi regresi linier, pohon keputusan, random forest, dan jaringan saraf.

7. Evaluasi Model
   Setelah melatih model, Anda perlu mengevaluasi kinerjanya menggunakan set pengujian. Evaluasi melibatkan perbandingan antara prediksi model dan nilai sebenarnya dari variabel target. Metrik evaluasi yang umum meliputi akurasi, presisi, recall, dan F1-score untuk masalah klasifikasi, serta kesalahan kuadrat rata-rata (RMSE) dan koefisien determinasi (R^2) untuk masalah regresi.

8. Penyempurnaan Model
   Berdasarkan hasil evaluasi, Anda mungkin perlu menyempurnakan model Anda. Ini dapat melibatkan pemilihan fitur ulang, penyetelan parameter model (misalnya, menggunakan pencarian grid atau pencarian acak), atau mencoba algoritma yang berbeda. Proses ini seringkali iteratif dan mungkin memerlukan beberapa putaran penyesuaian sebelum mencapai kinerja yang optimal.

9. Implementasi Model
   Setelah Anda puas dengan kinerja model Anda, Anda dapat mengimplementasikannya dalam aplikasi atau sistem produksi. Ini melibatkan mengintegrasikan model ke dalam kode, menyiapkan infrastruktur untuk menjalankan model, dan memantau kinerja model secara berkala untuk memastikan keberlanjutan kinerja yang baik.

## Cara membuat Machine Learning Model

### Apa saja yang dibutuhkan?

Untuk membangun model pembelajaran mesin menggunakan Python, berikut adalah beberapa langkah umum yang dapat diikuti:

1. Mengumpulkan data yang relevan dan sesuai dengan tujuan dari proyek pembelajaran mesin.

2. Membersihkan dan memproses data. Hal ini meliputi penghapusan data yang hilang, mengatasi nilai yang hilang, dan menormalisasi data.

3. Memilih algoritma pembelajaran mesin yang tepat. Pilih algoritma yang sesuai dengan tujuan dari proyek pembelajaran mesin. Beberapa algoritma yang umum digunakan adalah Regresi Linear, Naive Bayes, Decision Trees, Random Forests, Neural Networks, dan lainnya.

4. Memisahkan data menjadi data pelatihan dan data pengujian. Data pelatihan digunakan untuk melatih model sedangkan data pengujian digunakan untuk menguji dan mengevaluasi kinerja model.

5. Melatih model menggunakan data pelatihan.

6. Mengevaluasi kinerja model menggunakan data pengujian. Evaluasi model dapat dilakukan dengan menghitung akurasi, presisi, recall, F1-score, dan lainnya.

7. Menyesuaikan parameter model untuk meningkatkan kinerja model.

8. Menggunakan model untuk memprediksi atau klasifikasi data baru.

Beberapa pustaka populer di Python untuk pembelajaran mesin adalah Scikit-learn, TensorFlow, Keras, PyTorch, dan lainnya. Selain itu, ada banyak sumber daya online yang tersedia untuk belajar tentang pembelajaran mesin menggunakan Python, seperti tutorial online, kursus daring, dan buku.

### Pilihan algoritma pembelajaran mesin dan mengapa memilih algoritma tertentu.

Pilihan algoritma pembelajaran mesin tergantung pada tujuan dan karakteristik data yang akan dipelajari. Berikut adalah beberapa algoritma pembelajaran mesin dan penjelasan mengapa kita memilih algoritma tertentu:

1. Regresi Linear: digunakan untuk memprediksi variabel kontinu berdasarkan variabel independen. Cocok untuk analisis data yang bersifat linear, dan dapat membantu memahami hubungan antara dua variabel.

2. Naive Bayes: digunakan untuk klasifikasi dan pengelompokan. Cocok untuk data yang memiliki banyak atribut dan distribusi normal.

3. Decision Trees: digunakan untuk klasifikasi dan pengelompokan. Cocok untuk data yang memiliki banyak atribut dan kemampuan untuk membuat keputusan berdasarkan pohon keputusan.

4. Random Forests: digunakan untuk klasifikasi dan pengelompokan. Cocok untuk data yang memiliki banyak atribut dan dapat menghasilkan model yang lebih akurat dan stabil daripada decision tree.

5. Support Vector Machines (SVM): digunakan untuk klasifikasi dan pengelompokan. Cocok untuk data yang memiliki banyak atribut dan memisahkan data dengan jelas.

6. K-Nearest Neighbors (KNN): digunakan untuk klasifikasi dan pengelompokan. Cocok untuk data yang memiliki banyak atribut dan dapat mengelompokkan data berdasarkan jarak dengan tetangga terdekat.

7. Neural Networks: digunakan untuk klasifikasi, pengelompokan, dan prediksi. Cocok untuk data yang kompleks dan memiliki banyak atribut, dan dapat mempelajari pola dari data yang kompleks.

Pemilihan algoritma yang tepat akan membantu memastikan keberhasilan dalam pembelajaran mesin. Penting untuk menganalisis karakteristik data dengan seksama dan memilih algoritma yang cocok untuk tujuan pembelajaran mesin.

## Feature engineering

Feature engineering merupakan bagian integral dalam membangun dan mengimplementasikan model pembelajaran mesin. Dalam artikel ini, Anda akan belajar tentang apa itu feature engineering, mengapa kita memerlukannya, dan di mana posisinya dalam alur kerja machine learning. Selain itu, Anda akan memperoleh gambaran singkat tentang banyaknya alat ilmu data yang terlibat dalam feature engineering dan bagaimana alat-alat tersebut membantu ilmuwan data dalam diagnosa model.

### Apa itu feature engineering?

Sebelum kita bisa berbicara tentang feature engineering, kita harus mendefinisikan apa yang dimaksud dengan 'feature'. feature adalah properti yang dapat diukur dalam dataset, dan feature dapat digunakan sebagai input untuk model pembelajaran mesin. Satu cara untuk memikirkan feature adalah sebagai variabel prediktor yang masuk ke dalam model untuk memprediksi variabel hasil. Misalnya, jika kita ingin sebuah model yang memprediksi curah hujan pada tempat dan waktu tertentu, kita mungkin akan menggunakan suhu, kelembaban, bulan, ketinggian, dan sebagainya sebagai input. Ini adalah feature kami.

Seringkali, ketika diberikan sebuah dataset, mungkin tidak jelas fitur apa yang harus kita gunakan untuk model tertentu (misalnya, apakah kita harus menggunakan 'kerapatan pohon' sebagai input untuk model curah hujan kami?). Demikian pula, pada dataset besar, mungkin terlalu banyak fitur untuk memutuskan secara manual fitur mana yang akan digunakan. Beberapa fitur mungkin sangat berkorelasi satu sama lain, beberapa mungkin tidak bervariasi banyak dengan variabel hasil, dan beberapa mungkin berada dalam bentuk yang salah untuk menjadi input model dan sebagainya. Tidak jarang seorang ilmuwan data mungkin tidak menyadari hal ini sampai mereka mulai mendiagnosis model yang berkinerja buruk.

Feature engineering adalah cara untuk mengatasi tantangan-tantangan ini. Ini adalah istilah payung untuk teknik-teknik yang kami gunakan untuk membantu kami membuat keputusan tentang fitur dalam implementasi model pembelajaran mesi

### Mengapa kita memerlukan feature engineering?

Untuk memparafrase Tolstoy, "Semua implementasi model yang fungsional menyerupai satu sama lain tetapi setiap implementasi model yang disfungsional adalah disfungsional dengan caranya sendiri."

Ada banyak cara berbeda bagi implementasi model untuk menjadi disfungsional. Jadi pertanyaannya adalah: Apa yang akan membuat implementasi model fungsional atau disfungsional? Pertimbangkan empat atribut berikut:

1. Kinerja:
   Kita ingin model pembelajaran mesin kita berkinerja "baik" pada data kita. Jika model tidak mampu memprediksi variabel hasil (dengan tingkat akurasi yang wajar) pada data yang diketahui, tidak bijaksana untuk menggunakannya untuk memprediksi hasil pada data yang tidak diketahui.

2. Waktu Eksekusi:
   Misalkan model memiliki kinerja yang sangat baik tetapi memakan waktu yang sangat lama untuk dijalankan. Bagi seorang ilmuwan data, tergantung pada sumber daya komputasi yang tersedia, model seperti itu mungkin tidak praktis untuk produksi.

3. Interpretasi:
   Model hanya sebaik wawasan yang membantu kita memahami data. Ilmuwan data sering ditugaskan untuk mencari faktor apa yang mendorong hasil yang berbeda. Model yang berkinerja baik tidak akan banyak membantu jika model tersebut tidak transparan dan tidak dapat diinterpretasikan.

4. Generalisabilitas:
   Kita ingin model kami dapat digeneralisasikan dengan baik untuk data yang tidak dikenal. Seringkali ilmuwan data bekerja dengan data streaming dan membutuhkan model mereka untuk fleksibel dengan data baru dan tidak diketahui.

Feature engineering dapat dianggap sebagai kumpulan teknik yang digunakan ketika model kurang memiliki satu atau lebih atribut di atas. Jika kita membayangkan mesin diagnostik model (seperti versi modern dari mesin diagnostik), yang merepresentasikan atribut tersebut, maka feature engineering akan menjadi seperti memutar tombol dan menekan tombol hingga kita mencapai model yang memenuhi semua atribut kita secara memuaskan.

## Regresi dan Klasifikasi dengan ML

### Apa itu Regresi dan Klasifikasi dalam ML?

#### Regresi

Regresi digunakan untuk memprediksi output yang bersifat kontinu. Output adalah kuantitas yang dapat ditentukan secara fleksibel berdasarkan input model, daripada terbatas pada sejumlah label yang mungkin.

Contohnya:

Memprediksi tinggi tanaman pot dari jumlah curah hujan
Memprediksi gaji berdasarkan usia seseorang dan ketersediaan internet cepat
Memprediksi MPG (mil per galon) mobil berdasarkan ukuran dan tahun model

Regresi linier adalah algoritma regresi paling populer. Algoritma ini sering dianggap sepele karena relatif sederhana. Dalam konteks bisnis, regresi linier dapat digunakan untuk memprediksi kemungkinan pelanggan akan berhenti atau pendapatan yang akan dihasilkan oleh pelanggan tersebut. Model yang lebih kompleks mungkin cocok dengan data tersebut dengan lebih baik, namun dengan biaya kehilangan kesederhanaan.

#### Klasifikasi

Klasifikasi digunakan untuk memprediksi label diskrit. Outputnya termasuk dalam kumpulan hasil yang mungkin. Banyak situasi hanya memiliki dua hasil yang mungkin. Ini disebut klasifikasi biner (Benar/Salah, 0 atau 1, Hotdog/bukan Hotdog).

Contohnya:

Memprediksi apakah sebuah email adalah spam atau tidak
Memprediksi apakah akan hujan atau tidak
Memprediksi apakah pengguna adalah pengguna power atau pengguna biasa
Ada juga dua jenis klasifikasi umum lainnya: klasifikasi multi-kelas dan klasifikasi multi-label.

Klasifikasi multi-kelas memiliki ide yang sama dengan klasifikasi biner, tetapi daripada dua hasil yang mungkin, ada tiga atau lebih.

Contohnya:

Memprediksi apakah sebuah foto berisi pir, apel, atau persik
Memprediksi huruf apa dari alfabet yang ditulis tangan
Memprediksi apakah sebuah buah kecil, sedang, atau besar

Catatan penting tentang klasifikasi biner dan multi-kelas adalah bahwa pada kedua jenis klasifikasi tersebut, setiap hasil memiliki satu label tertentu. Namun, pada klasifikasi multi-label, terdapat beberapa label yang mungkin untuk setiap hasil. Ini berguna untuk segmentasi pelanggan, kategorisasi gambar, dan analisis sentimen untuk memahami teks. Untuk melakukan klasifikasi ini, kita menggunakan model seperti Naive Bayes, K-Nearest Neighbors, SVM, serta berbagai model deep learning.

### Bagaimana membangun model Regresi dan Klasifikasi menggunakan Python.

[berikut adalah contoh membuat regresi dan klasifikasi](./membangun_ml_model.py) atau [disini](https://colab.research.google.com/drive/11OvGI33TD3ze73veKkOF5bGBTrfr5J9q?usp=sharing)

## Apa itu deep learning?

Pernahkah Anda bertanya-tanya apa yang menggerakkan Siri? Teknologi apa yang digunakan oleh pengembang untuk membuat mobil self-driving? Bagaimana telepon Anda bisa mengenali wajah? Mengapa sepertinya aplikasi foto Anda lebih baik dalam mengenali wajah teman Anda daripada Anda sendiri? Apa yang ada di balik semua ini? Apakah itu sihir? Nah, tidak tepatnya; itu adalah teknologi canggih yang disebut deep learning (DL). Mari kita lihat apa ini semua tentang!

### Deep Learning vs. Machine Learning

Pertama, mari fokus pada pembelajaran. Jika Anda pernah mendengar tentang machine learning sebelumnya, Anda mungkin sudah familiar dengan konsep model pembelajaran. Pembelajaran menggambarkan proses di mana model menganalisis data dan menemukan pola. Algoritma machine learning kita belajar dari pola-pola ini untuk menemukan representasi terbaik dari data ini, yang kemudian digunakan untuk membuat prediksi tentang data baru yang belum pernah dilihat sebelumnya.

Deep learning adalah sub-bidang dari machine learning, dan konsep pembelajaran hampir sama.

- Kita membuat model dengan hati-hati
- Berikan data yang relevan
- Latih dengan datanya
- Minta untuk membuat prediksi untuk data yang belum pernah dilihat

Model deep learning digunakan dengan banyak jenis data yang berbeda, seperti teks, gambar, audio, dan lainnya, membuatnya dapat diterapkan di banyak domain yang berbeda.

### Apa arti dari "deep"?

Ini menimbulkan pertanyaan: apa itu aspek "deep" dari deep learning ini? Ini membedakan deep learning dari model machine learning biasa dan mengapa ini adalah alat yang kuat yang semakin umum digunakan dalam masyarakat saat ini.

Bagian "deep" dari deep learning merujuk pada banyak "lapisan" yang mengubah data. Arsitektur ini meniru struktur otak, di mana setiap lapisan berikutnya mencoba untuk belajar pola yang semakin kompleks dari data yang dimasukkan ke dalam model. Ini mungkin terdengar agak abstrak, jadi mari kita lihat contoh konkret, seperti pengenalan wajah. Dengan pengenalan wajah, model deep learning mengambil foto sebagai input, dan banyak lapisan melakukan langkah-langkah tertentu untuk mengidentifikasi siapa yang ada dalam gambar. Langkah-langkah yang dilakukan oleh setiap lapisan mungkin seperti berikut:

1. Cari wajah dalam gambar menggunakan deteksi tepi.
2. Analisis fitur wajah (mata, hidung, mulut, dll.).
3. Bandingkan dengan wajah dalam repositori.
4. Output prediksi!

Struktur dari banyak lapisan abstrak ini membuat deep learning sangat kuat. Memberi makan data dalam jumlah besar ke model membuat koneksi antar lapisan lebih rumit. Model deep learning cenderung berperforma lebih baik dengan lebih banyak data daripada algoritma pembelajaran lainnya.

### Konsep Dasar Deep Learning

Deep learning adalah subbidang dari machine learning yang menggunakan model berbasis jaringan saraf tiruan (artificial neural networks) dengan banyak lapisan (deep) untuk menemukan pola dan representasi yang lebih kompleks dari data. Dalam deep learning, model dilatih menggunakan algoritma backpropagation untuk meminimalkan kesalahan antara prediksi model dan data aktual. Deep learning telah menunjukkan keberhasilan yang luar biasa dalam berbagai aplikasi, seperti pengenalan gambar, pengenalan suara, dan pemrosesan bahasa alami.

### Penerapan Deep Learning

Beberapa contoh penerapan deep learning dalam dunia nyata meliputi:

- Pengenalan wajah: teknologi ini digunakan dalam berbagai sistem keamanan dan pengenalan wajah pada perangkat smartphone.
- Kendaraan otonom: mobil self-driving menggunakan deep learning untuk menginterpretasikan data dari sensor dan membuat keputusan yang aman mengenai pengendalian kendaraan.
- Generasi teks: model deep learning seperti GPT dapat digunakan untuk menghasilkan teks yang masuk akal dan koheren.
- Analisis sentimen: deep learning digunakan untuk menganalisis sentimen teks dalam ulasan produk atau komentar media sosial.

### Proses Pelatihan Model Deep Learning

Proses pelatihan model deep learning melibatkan beberapa langkah:

- Data masukan diolah melalui jaringan saraf tiruan, dan setiap lapisan menghasilkan representasi yang lebih abstrak dan kompleks dari data.
- Setelah melewati semua lapisan, model menghasilkan prediksi.
- Prediksi ini kemudian dibandingkan dengan data aktual, dan kesalahan dihitung.
- Algoritma backpropagation digunakan untuk menghitung gradien kesalahan dan menyesuaikan bobot dalam jaringan secara proporsional.
- Proses ini diulang untuk banyak iterasi sampai model memiliki kesalahan yang minimal.

### contoh proses deep learning

Misalkan kita memiliki model deep learning untuk mengenali tulisan tangan. Data masukan adalah gambar angka tulisan tangan. Ketika gambar melewati lapisan pertama, model mungkin belajar untuk mendeteksi tepi dan garis. Pada lapisan berikutnya, model mungkin mulai mengenali bentuk seperti lingkaran atau garis diagonal. Pada lapisan lebih dalam, model mulai menggabungkan bentuk-bentuk ini untuk mengenali angka secara keseluruhan. Setelah melalui semua lapisan, model menghasilkan prediksi angka yang ditulis. Kesalahan antara prediksi dan angka sebenarnya dihitung, dan algoritma backpropagation digunakan untuk mengoptimalkan bobot dalam model.

### Jumlah Data yang Tinggi

![gambar](https://www.researchgate.net/publication/331540139/figure/fig3/AS:733273504378885@1551837435876/The-performance-of-deep-learning-with-respect-to-the-amount-of-data.ppm)

Perhatikan bahwa tanpa jumlah data yang besar, model deep learning tidak lebih kuat (dan mungkin bahkan kurang akurat) daripada model pembelajaran yang lebih sederhana. Namun, dengan jumlah data yang besar, model deep learning dapat meningkatkan performanya sampai ke titik di mana mereka dapat mengungguli manusia dalam tugas-tugas seperti mengklasifikasikan objek atau wajah dalam gambar atau mengemudi. Deep learning pada dasarnya adalah sistem pembelajaran masa depan (juga dikenal sebagai representasi pembelajaran). Ia belajar dari data mentah tanpa intervensi manusia. Oleh karena itu, dengan jumlah data yang besar, sistem deep learning akan berperforma lebih baik daripada sistem machine learning tradisional yang bergantung pada ekstraksi fitur dari pengembang.

Kendaraan otonom, seperti Tesla, harus memproses ribuan, bahkan jutaan tanda stop, untuk memahami bahwa mobil harus berhenti ketika melihat heksagon merah dengan tulisan "Stop" (dan ini hanya untuk tanda stop di AS!). Bayangkan jumlah situasi yang harus dilatih oleh kendaraan self-driving untuk memastikan keselamatan.

### Dengan Deep Learning Datang Tanggung Jawab yang Mendalam

Bahkan di luar mengidentifikasi objek, model deep learning dapat menghasilkan konten audio dan visual yang tampak sangat nyata. Mereka dapat memodifikasi gambar yang sudah ada, seperti dalam aplikasi yang keren ini yang memungkinkan Anda untuk menambahkan pohon atau mengubah bangunan dalam serangkaian foto. Namun, mereka dapat memiliki sisi yang lebih gelap. Model DL dapat menghasilkan media buatan di mana identitas seseorang dalam gambar, video, atau audio diganti dengan orang lain. Ini dikenal sebagai deepfakes, dan mereka dapat memiliki implikasi yang menakutkan, seperti penipuan keuangan dan penyebaran berita palsu dan hoaks.

<iframe width="560" height="315" src="https://www.youtube.com/embed/F4G6GNFz0O8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Graphics Processing Units

Satu hal terakhir yang perlu dicatat tentang deep learning adalah bahwa dengan jumlah data yang besar dan lapisan kompleksitas, Anda mungkin membayangkan bahwa ini membutuhkan banyak waktu dan daya pemrosesan. Intuisi itu akan benar. Model ini sering memerlukan GPU (unit pemrosesan grafis) kinerja tinggi untuk dijalankan dalam waktu yang wajar. Processor ini memiliki bandwidth memori yang besar dan dapat memproses beberapa komputasi secara simultan. CPU juga dapat menjalankan model deep learning; Namun, mereka akan jauh lebih lambat.

Pembangunan GPU telah menjadi kunci kesuksesan deep learning. Menarik untuk dicatat bahwa salah satu faktor pendorong untuk pengembangan ini bukan kebutuhan akan alat deep learning yang lebih baik, tetapi permintaan untuk grafis video game yang lebih baik. Ternyata GPU sangat cocok untuk memproses kumpulan data besar. Ini membuatnya menjadi alat yang sempurna untuk model pembelajaran dan telah menempatkan deep learning khususnya di garis depan percakapan machine learning.

## Pengantar TensorFlow

TensorFlow adalah library open source untuk pembelajaran mesin dan kecerdasan buatan yang dikembangkan oleh Google. TensorFlow dapat digunakan untuk membangun dan melatih model pembelajaran mesin, serta mengembangkan aplikasi yang berbasis kecerdasan buatan.

TensorFlow memiliki beberapa fitur utama seperti:

1. Arsitektur fleksibel: TensorFlow memiliki arsitektur yang fleksibel dan dapat digunakan untuk membangun berbagai jenis model pembelajaran mesin, termasuk model Deep Learning.

2. Otomatisasi yang baik: TensorFlow dapat melakukan otomatisasi pada proses seperti optimasi dan peningkatan model. Hal ini memungkinkan pengguna untuk fokus pada pengembangan model tanpa perlu memperhatikan detail teknis.

3. Scalability: TensorFlow dirancang untuk skalabilitas dan dapat digunakan pada berbagai platform dan perangkat, mulai dari ponsel hingga cluster komputasi besar.

4. Visualisasi: TensorFlow menyediakan alat visualisasi yang memudahkan pengguna dalam memahami dan menganalisis model yang dibuat.

Beberapa aplikasi yang dapat dibangun menggunakan TensorFlow adalah image recognition, speech recognition, natural language processing, dan banyak lagi.

Untuk memulai dengan TensorFlow, ada beberapa hal yang harus dipelajari seperti instalasi, penggunaan API, membangun model, dan mengevaluasi model. TensorFlow juga memiliki dokumentasi resmi dan banyak tutorial online yang tersedia untuk membantu pengguna mempelajari lebih lanjut.

## Pengantar Keras

Keras adalah library open source untuk pembelajaran mesin dan kecerdasan buatan yang dirancang untuk memudahkan pembuatan dan pelatihan model neural networks. Keras menyediakan API tingkat tinggi yang memudahkan pengguna dalam membuat dan mengevaluasi model, serta menyediakan banyak fitur yang dapat digunakan untuk mengoptimalkan model.

Beberapa fitur Keras yang dapat digunakan adalah:

1. Modularitas: Keras dirancang dengan modularitas yang tinggi, sehingga pengguna dapat dengan mudah menggabungkan berbagai jenis lapisan neural networks untuk membangun model yang lebih kompleks.

2. API Tingkat Tinggi: Keras menyediakan API tingkat tinggi yang memudahkan pengguna dalam membuat dan mengevaluasi model neural networks. API ini mencakup berbagai jenis model seperti Sequential, Functional, dan Subclassing.

3. Kemudahan dalam Pelatihan Model: Keras menyediakan berbagai algoritma optimasi dan fungsi aktivasi yang dapat digunakan untuk melatih model neural networks dengan lebih mudah.

4. Portable: Keras dapat berjalan pada berbagai platform dan perangkat, termasuk CPU, GPU, dan TPU.

Beberapa aplikasi yang dapat dibangun menggunakan Keras adalah image recognition, speech recognition, natural language processing, dan banyak lagi.

Untuk memulai dengan Keras, ada beberapa hal yang harus dipelajari seperti instalasi, penggunaan API, membangun model, dan mengevaluasi model. Keras juga memiliki dokumentasi resmi dan banyak tutorial online yang tersedia untuk membantu pengguna mempelajari lebih lanjut.

## Bagaimana membangun model menggunakan TensorFlow

[berikut adalah contoh membuat regresi dan klasifikasi](./membangun_dl_model_dengan_tensorflow.py) atau [disini](https://colab.research.google.com/drive/1gFIft4AhfPI-eEqWPFPv-JJ6CmPdCi7M?usp=sharing)

## resources

- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [tensorflow](https://www.tensorflow.org/)
- [keras](https://keras.io/api/)
- [sci-kit learn](https://scikit-learn.org/stable/)
- [kaggle](https://www.kaggle.com/)
- Buku: Pattern Recognition and Machine Learning, Christopher M. Bishop
- Buku: Deep Learning with Python, François Chollet
- Buku: Algorithms of Oppression: How Search Engines Reinforce Racism, Safiya Umoja Noble
- Buku: Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy, Cathy O’Neil
