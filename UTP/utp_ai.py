# -*- coding: utf-8 -*-
"""UTP AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HWZlWzxmqU6Oa0SHU5SpwJ997SFJdEA7

Nama : Ferli Malkan Amien <br>
NPM  : 2117051050 <br>
Kelas: C
<br>
UTP MK. Artificial Intelligence <br>
GitHub : https://github.com/FerliMalkanAmien/Kuliah-Artificial-Intelligence/tree/main/UTP
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

"""## Data Identification"""

data = pd.read_csv("https://raw.githubusercontent.com/FerliMalkanAmien/Kuliah-Artificial-Intelligence/main/UTP/ecommerce_banner_promo.csv")

data

data.head()

data.info()

data.describe()

data.shape

print("Data eksplorasi dengan mengecek korelasi dari setiap feature ")
print(data.corr())

print("Data eksplorasi dengan mengecek distribusi label")
print(data.groupby("Clicked on Ad").size())

# Seting: matplotlib and seaborn
sns.set_style('whitegrid')  
plt.style.use('fivethirtyeight')

# Data eksplorasi dengan visualisasi
# Visualisasi Jumlah user dibagi ke dalam rentang usia (Age) menggunakan histogram (hist()) plot
plt.figure(figsize=(10, 5))
plt.hist(data["Age"], bins = data.Age.nunique())
plt.xlabel("Age")
plt.tight_layout()
plt.show()

# Gunakan pairplot() dari seaborn (sns) modul untuk menggambarkan hubungan setiap feature.
plt.figure()
sns.pairplot(data)
plt.show()

"""## Preprocessing"""

print("Cek missing value")
print(data.isnull().sum().sum())

data = data.drop(['Ad Topic Line','City','Country','Timestamp'], axis = 1)
data.head()

"""## Split Data"""

X = data.drop('Clicked on Ad', axis = 1)
y = data['Clicked on Ad']

"""## Modelling / Training"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Call the classifier
logreg = LogisticRegression()
# Fit the classifier to the training data
logreg = logreg.fit(X_train, y_train)
# Prediksi model
y_pred = logreg.predict(X_test)

print("Evaluasi Model Performance:")
print("Training Accuracy :", logreg.score(X_train, y_train))
print("Testing Accuracy :", logreg.score(X_test, y_test))

#apply confusion_matrix function to y_test and y_pred
print("Confusion matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\n")
#apply classification_report function to y_test and y_pred
print("Classification report:")
cr = classification_report(y_test, y_pred)
print(cr)

"""## Kesimpulan
Berdasarkan hasil evaluasi, Model sudah sangat baik dalam memprediksi user yang akan mengklik website atau tidak, dapat dilihat dari nilai accuracy = 0.90; Dataset memiliki jumlah label yang seimbang (balance class), sehingga evaluasi performansi dapat menggunakan metrik Accuracy.

## Data Dummy
"""

dummy = pd.DataFrame(
    {
        "Daily Time Spent on Site" : pd.Series([80.30, 69.40, 74.20, 73.00, 51.48]),
        "Age" : pd.Series([32, 25, 27, 32, 50]),
        "Area Income" : pd.Series([68442.23, 59785.78, 54807.05, 71389.76, 42414.98]),
        "Daily Internet Usage" : pd.Series([194.12, 236.78, 246.21, 209.32, 119.87]),
        "Male" : pd.Series([1, 0, 1, 1, 1])
        # "Clicked on Ad" : pd.Series([0, 0, 0, 1, 1])
    }
)

dummy

features = ["Daily Time Spent on Site",	"Age", "Area Income", "Daily Internet Usage", "Male"]
X = data[features]
y = data["Clicked on Ad"]

logreg = LogisticRegression()
logreg = logreg.fit(X, y)

print(logreg.predict(dummy))