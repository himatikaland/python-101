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