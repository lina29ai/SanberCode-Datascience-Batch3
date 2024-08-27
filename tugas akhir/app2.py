import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix

# Set page title
st.set_page_config(page_title="Dashboard Klasifikasi", layout="wide")

# Title and description
st.title("Dashboard Klasifikasi")
st.markdown("""
Aplikasi ini menampilkan hasil klasifikasi pada dataset Iris. 
Anda bisa melihat metrik evaluasi seperti precision, recall, F1-score, serta visualisasi confusion matrix dan distribusi data.
""")

# Sidebar for user controls
st.sidebar.header("Pengaturan")
model_type = st.sidebar.selectbox("Pilih Model Klasifikasi:", ["Random Forest", "Decision Tree", "KNN"])
n_estimators = st.sidebar.slider("Jumlah Estimators (untuk Random Forest):", 10, 100, 50)
test_size = st.sidebar.slider("Ukuran Data Testing (%):", 10, 50, 20) / 100

# Load dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="species")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

# Train model
if model_type == "Random Forest":
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
elif model_type == "Decision Tree":
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(random_state=42)
else:
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Display classification report
st.subheader("Tabel Hasil Klasifikasi:")
report = classification_report(y_test, y_pred, target_names=iris.target_names, output_dict=True)
report_df = pd.DataFrame(report).transpose()
st.table(report_df)

# Confusion Matrix
st.subheader("Confusion Matrix:")
fig, ax = plt.subplots()
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names, ax=ax)
st.pyplot(fig)

# Feature importance (for Random Forest)
if model_type == "Random Forest":
    st.subheader("Feature Importance:")
    fig, ax = plt.subplots()
    feature_importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    feature_importance.plot(kind='barh', ax=ax)
    st.pyplot(fig)

# Data distribution
st.subheader("Visualisasi Distribusi Fitur:")
fig, ax = plt.subplots()
sns.pairplot(pd.concat([X, y], axis=1), hue="species", markers=["o", "s", "D"], palette="Set1", diag_kind="kde")
st.pyplot(fig)

# Additional model interpretation and insights
st.subheader("Penjelasan Model")
st.markdown("""
Model ini menggunakan algoritma Random Forest untuk memprediksi kelas bunga iris (setosa, versicolor, virginica). 
Dataset Iris memiliki 4 fitur utama:
- **Sepal Length** (Panjang kelopak)
- **Sepal Width** (Lebar kelopak)
- **Petal Length** (Panjang petal)
- **Petal Width** (Lebar petal)

Algoritma Random Forest bekerja dengan membuat beberapa decision trees yang kemudian digabungkan untuk memberikan prediksi akhir. 
Keunggulan Random Forest adalah kemampuannya untuk menangani variabilitas dalam data dan memberikan hasil yang stabil.

Setelah model dilatih dengan data training, hasil prediksi dievaluasi menggunakan metrik berikut:
- **Precision**: Mengukur proporsi prediksi yang benar dari keseluruhan prediksi positif.
- **Recall**: Mengukur proporsi sampel positif yang berhasil diprediksi dengan benar.
- **F1-Score**: Kombinasi dari precision dan recall yang memberikan keseimbangan di antara keduanya.
- **Support**: Jumlah sampel yang ada di setiap kelas.

Confusion matrix digunakan untuk melihat di mana kesalahan prediksi terjadi pada setiap kelas.
""")


# Allow user to upload custom data
st.sidebar.subheader("Unggah Data CSV Anda")
uploaded_file = st.sidebar.file_uploader("Unggah file CSV untuk diklasifikasikan", type=["csv"])

if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)
    st.write("Data yang diunggah:")
    st.write(user_data.head())
    
    if st.sidebar.button("Lakukan Klasifikasi"):
        user_predictions = model.predict(user_data)
        st.write("Hasil Prediksi:")
        st.write(pd.DataFrame(user_predictions, columns=["Prediksi Kelas"]).replace({0: "setosa", 1: "versicolor", 2: "virginica"}))

# Footer
st.sidebar.markdown("Roma Ulina")
