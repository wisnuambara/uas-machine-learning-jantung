# 🫀 Prediksi Penyakit Jantung (Heart Disease Detection)

Proyek ini adalah implementasi model *Machine Learning* untuk mendeteksi indikasi penyakit jantung berdasarkan data rekam medis pasien. Proyek ini disusun untuk memenuhi **Ujian Akhir Semester Genap TA. 2025/2026 mata kuliah Pembelajaran Mesin**.

- **Link Aplikasi (Deployment):** https://uas-pm-wisnuambara.streamlit.app/
- **Video Demonstrasi:** https://www.loom.com/share/d4dfa7d6e9e04d1d890c08c27ec1ae09
- **Google Collab:** https://colab.research.google.com/drive/1nIfPgMvG3pAGsDaDgck78K93HDnLXBo_?usp=sharing
---

## 📊 Penjelasan Dataset
Dataset yang digunakan adalah **Heart Disease Dataset** publik dari UCI Machine Learning Repository (Cleveland database). Dataset ini berisi 13 fitur klinis (seperti usia, tekanan darah, kolesterol, hasil EKG, dll) dan 1 kolom target.

**Pra-pemrosesan Data yang Dilakukan:**
1. **Pembersihan Data (Handling Missing Values):** Menghapus baris data yang cacat atau kosong (ditandai dengan simbol `?` pada dataset asli).
2. **Encoding Target:** Mengubah target multikelas (0-4) menjadi klasifikasi biner, yaitu `0` (Sehat/Indikasi Negatif) dan `1` (Sakit/Indikasi Positif).
3. **Standarisasi:** Menggunakan `StandardScaler` untuk menyamakan rentang skala pada fitur numerik agar algoritma dapat belajar secara seimbang dan optimal.

## 🤖 Pembangunan dan Optimasi Model
- **Algoritma:** Random Forest Classifier.
- **Optimasi (Hyperparameter Tuning):** Menggunakan `GridSearchCV` untuk mencari kombinasi parameter terbaik (`n_estimators`, `max_depth`, `min_samples_split`).
- **Evaluasi:** Model dievaluasi menggunakan metrik **Akurasi** dan **F1-Score** pada data uji (proporsi *train-test split* 80:20). Model dan *scaler* kemudian disimpan dalam format `.pkl` menggunakan `joblib`.

## 💻 Dokumentasi Antarmuka (Aplikasi Web)
Aplikasi dibangun menggunakan *framework* **Streamlit**. 
- **Input Pengguna:** Menyediakan form interaktif (berupa *dropdown* dan *number input*) untuk memasukkan 13 parameter medis pasien. Terdapat juga menu FAQ bergaya *dropdown* akordion untuk mengedukasi pengguna mengenai definisi setiap kolom.
- **Penanganan Input:** Sebelum diprediksi, data masukan dari pengguna akan ditransformasi (standarisasi) secara *real-time* menggunakan *scaler* yang diekstrak dari file `.pkl` hasil pelatihan awal.
- **Output:** Sistem akan mengeluarkan prediksi akhir berupa **"INDIKASI POSITIF"** (Berisiko) atau **"INDIKASI NEGATIF"** (Aman).

---

## 🚀 Cara Menjalankan Proyek Secara Lokal

Jika Anda ingin menjalankan aplikasi ini di komputer lokal, ikuti langkah-langkah berikut:

1. Clone Repository ini
    git clone https://github.com/wisnuambara/uas-machine-learning-jantung.git
2. Install Dependency yang dibutuhkan
    pip install -r requirements.txt
3. Jalankan Aplikasi
    streamlit run app.py



