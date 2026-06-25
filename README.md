# Aplikasi Prediksi Penyakit Jantung 🫀

Proyek ini adalah implementasi model Machine Learning untuk memprediksi indikasi penyakit jantung berdasarkan data rekam medis pasien. Proyek ini disusun untuk memenuhi Ujian Akhir Semester Genap TA. 2025/2026 mata kuliah Pembelajaran Mesin.

## Penjelasan Dataset dan Pemrosesan
Dataset yang digunakan adalah **Heart Disease Dataset** publik dari UCI Machine Learning Repository (Cleveland database). 
Langkah pra-pemrosesan yang dilakukan meliputi:
- **Pembersihan Data (Data Cleaning):** Menghapus baris yang memiliki missing values (simbol `?`) pada atribut `ca` dan `thal`.
- **Encoding:** Mengubah variabel target yang memiliki 5 kelas (0-4) menjadi klasifikasi biner (0 = Sehat, 1 = Sakit).
- **Standarisasi:** Menggunakan `StandardScaler` untuk menyamakan rentang skala pada fitur numerik seperti tekanan darah (`trestbps`) dan kolesterol (`chol`) agar model dilatih lebih optimal.

## Dokumentasi Antarmuka (Interface)
Aplikasi dibangun menggunakan **Streamlit**. Pengguna dapat memasukkan 13 parameter klinis pasien melalui antarmuka formulir interaktif (Dropdown dan Number Input).
Sistem akan memproses masukan pengguna melewati tahapan standarisasi yang sama dengan saat pelatihan, kemudian memprediksi hasilnya menggunakan model `Random Forest Classifier` yang telah dioptimasi via Hyperparameter Tuning, lalu menampilkan peringatan medis yang sesuai.

## Cara Menjalankan Proyek Secara Lokal
1. Pastikan Python sudah terinstal.
2. Buka terminal/command prompt, arahkan ke folder proyek ini.
3. Instal dependensi dengan perintah: `pip install -r requirements.txt`
4. Jalankan aplikasi Streamlit dengan perintah: `streamlit run app.py`