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
