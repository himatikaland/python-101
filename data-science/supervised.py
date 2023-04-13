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

# Ekstraksi fitur menggunakan CountVectorizer
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
