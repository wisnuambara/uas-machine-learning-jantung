import streamlit as st
import pandas as pd
import joblib

# 1. Memuat model, scaler, dan daftar fitur
model_data = joblib.load('model_jantung.pkl')
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']

# 2. Pengaturan Halaman Antarmuka
st.set_page_config(page_title="Deteksi Penyakit Jantung", page_icon="🫀", layout="wide")
st.title("🫀 Prediksi Penyakit Jantung (Heart Disease UCI)")
st.write("Aplikasi ini menggunakan model Machine Learning untuk memprediksi indikasi penyakit jantung berdasarkan data rekam medis pasien.")

# 3. Form Input Pengguna
with st.form("input_form"):
    st.subheader("Masukkan Data Medis Pasien")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Umur", min_value=1, max_value=120, value=65)
        sex = st.selectbox("Jenis Kelamin", options=[1, 0], format_func=lambda x: "Pria" if x == 1 else "Wanita")
        cp = st.selectbox("Tipe Nyeri Dada (cp)", options=[1, 2, 3, 4], help="Lihat panduan di bawah untuk arti angka ini")
        trestbps = st.number_input("Tekanan Darah Istirahat (mmHg)", min_value=50, max_value=250, value=160)
        kolesterol = st.number_input("Kolesterol Serum (mg/dl)", min_value=100, max_value=600, value=280)
        
    with col2:
        fbs = st.selectbox("Gula Darah Puasa > 120 mg/dl", options=[1, 0], format_func=lambda x: "Ya (Benar)" if x == 1 else "Tidak (Salah)")
        restecg = st.selectbox("Hasil EKG Istirahat", options=[0, 1, 2], help="Lihat panduan di bawah untuk arti angka ini")
        thalach = st.number_input("Detak Jantung Maksimal (thalach)", min_value=50, max_value=250, value=110)
        exang = st.selectbox("Angina Akibat Olahraga (exang)", options=[1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        
    with col3:
        oldpeak = st.number_input("Depresi ST (oldpeak)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
        slope = st.selectbox("Kemiringan Segmen ST (slope)", options=[1, 2, 3], help="Lihat panduan di bawah untuk arti angka ini")
        ca = st.selectbox("Jumlah Pembuluh Darah Utama (ca)", options=[0, 1, 2, 3])
        thal = st.selectbox("Hasil Thallium Scan (thal)", options=[3, 6, 7], help="Lihat panduan di bawah untuk arti angka ini")

    submit_button = st.form_submit_button(label="Lakukan Prediksi Medis")

# 4. Logika Penanganan Input dan Prediksi
if submit_button:
    input_df = pd.DataFrame([[age, sex, cp, trestbps, kolesterol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]], columns=features)
    input_scaled = scaler.transform(input_df)
    prediksi = model.predict(input_scaled)
    
    st.markdown("---")
    st.subheader("🩺 Hasil Analisis:")
    
    if prediksi[0] == 1:
        st.error("⚠️ **INDIKASI POSITIF:** Berdasarkan data yang dimasukkan, pasien memiliki **indikasi penyakit jantung**. Segera lakukan pemeriksaan medis lanjutan secara komprehensif.")
    else:
        st.success("✅ **INDIKASI NEGATIF:** Berdasarkan data yang dimasukkan, pasien **tidak menunjukkan indikasi penyakit jantung** pada tingkat yang berisiko. Tetap jaga pola hidup sehat.")

# 5. Panduan / FAQ bergaya Akordion
st.markdown("---")
st.subheader("📖 Panduan Pengisian Data (FAQ)")
st.caption("Klik pada masing-masing pertanyaan untuk melihat penjelasan detail dari kolom yang harus diisi.")

with st.expander("Kenapa perlu Umur?"):
    st.markdown("""
    **Definisi:** Usia pasien dalam hitungan tahun.
    
    **Kenapa penting?** Penyakit jantung sangat dipengaruhi oleh faktor penuaan. Semakin tua usia seseorang, dinding pembuluh darahnya cenderung menjadi lebih kaku dan rentan terhadap penumpukan plak.
    
    **Dimana saya bisa tahu?** Melalui KTP, Kartu Keluarga, atau Akta Kelahiran.
    """)

with st.expander("Kenapa perlu Jenis Kelamin?"):
    st.markdown("""
    **Definisi:** Jenis kelamin biologis pasien (Pria/Wanita).
    
    **Kenapa penting?** Secara statistik medis, pria memiliki risiko terkena penyakit jantung lebih tinggi di usia muda dibandingkan wanita (sebelum masa menopause).
    
    **Dimana saya bisa tahu?** Melalui KTP atau identitas pribadi.
    """)

with st.expander("Apa maksud angka pada Tipe Nyeri Dada (cp)?"):
    st.markdown("""
    **Definisi:** Sensasi nyeri, sesak, atau tertekan di area dada.
    
    **Arti Angka Dropdown:**
    * **1 (Typical angina):** Nyeri dada klasik akibat otot jantung kekurangan suplai darah.
    * **2 (Atypical angina):** Nyeri dada ringan yang tidak sepenuhnya memenuhi ciri khas masalah jantung.
    * **3 (Non-anginal pain):** Nyeri dada yang bukan disebabkan oleh jantung (misalnya asam lambung atau nyeri otot).
    * **4 (Asymptomatic):** Tidak ada rasa nyeri sama sekali (namun bisa jadi sangat berbahaya karena iskemia diam-diam).
    
    **Kenapa penting?** Karakteristik rasa sakit adalah kunci utama bagi dokter untuk mendiagnosis serangan jantung.
    
    **Dimana saya bisa tahu?** Dari keluhan fisik yang dirasakan secara langsung oleh pasien.
    """)

with st.expander("Kenapa perlu Tekanan Darah Istirahat (trestbps)?"):
    st.markdown("""
    **Definisi:** Angka tekanan darah atas (sistolik) saat pasien dalam keadaan tenang/istirahat total.
    
    **Kenapa penting?** Hipertensi (darah tinggi) memaksa jantung memompa lebih keras dari seharusnya, yang lama-kelamaan akan merusak otot jantung dan pembuluh darah koroner.
    
    **Dimana saya bisa tahu?** Diukur menggunakan alat tensimeter (Sphygmomanometer) di klinik, rumah sakit, atau apotek terdekat.
    """)

with st.expander("Kenapa perlu Kolesterol Serum?"):
    st.markdown("""
    **Definisi:** Total kadar lemak (kolesterol) di dalam sirkulasi darah yang diukur dalam satuan mg/dl.
    
    **Kenapa penting?** Kolesterol jahat yang terlalu tinggi adalah penyebab utama terbentuknya plak (kerak) yang menyumbat pembuluh darah menuju jantung.
    
    **Dimana saya bisa tahu?** Lewat pemeriksaan laboratorium ambil darah, atau menggunakan alat tes darah portabel di apotek.
    """)

with st.expander("Kenapa perlu Gula Darah Puasa (fbs)?"):
    st.markdown("""
    **Definisi:** Apakah kadar gula di dalam darah lebih tinggi dari 120 mg/dl setelah puasa semalaman?
    
    **Kenapa penting?** Gula darah tinggi adalah indikator penyakit Diabetes. Diabetes sangat merusak dinding pembuluh darah dan meningkatkan risiko penyakit jantung secara drastis.
    
    **Dimana saya bisa tahu?** Melakukan cek gula darah (menggunakan alat glukometer) di pagi hari setelah berpuasa tidak makan selama minimal 8 jam.
    """)

with st.expander("Apa maksud angka pada Hasil EKG Istirahat (restecg)?"):
    st.markdown("""
    **Definisi:** Rekaman aktivitas listrik jantung saat pasien sedang berbaring istirahat.
    
    **Arti Angka Dropdown:**
    * **0 (Normal):** Aktivitas listrik jantung sehat dan teratur.
    * **1 (ST-T wave abnormality):** Ada sedikit kelainan pada gelombang listrik, bisa menjadi sinyal awal otot jantung kurang oksigen.
    * **2 (Left ventricular hypertrophy):** Terdeteksi adanya pembengkakan pada bilik kiri jantung.
    
    **Kenapa penting?** EKG adalah alat diagnostik utama. Kelainan listrik pada jantung adalah bukti nyata adanya kerusakan organ.
    
    **Dimana saya bisa tahu?** Melalui pemeriksaan mesin EKG (Elektrokardiogram) yang dipasang di dada saat berkunjung ke rumah sakit.
    """)

with st.expander("Kenapa perlu Detak Jantung Maksimal (thalach)?"):
    st.markdown("""
    **Definisi:** Angka tertinggi denyut jantung per menit yang berhasil dicapai pasien saat dipaksa beraktivitas keras.
    
    **Kenapa penting?** Jantung yang sakit atau salurannya tersumbat tidak akan memiliki daya tahan untuk berdetak cepat dan memompa darah dengan maksimal saat tubuh membutuhkannya.
    
    **Dimana saya bisa tahu?** Lewat pemeriksaan *Treadmill Stress Test* di hadapan dokter, atau dipantau menggunakan *smartwatch* saat berolahraga berat.
    """)

with st.expander("Apa itu Angina Akibat Olahraga (exang)?"):
    st.markdown("""
    **Definisi:** Apakah pasien merasakan sakit dada hebat (*angina*) **hanya** pada saat sedang berolahraga atau mengangkat beban berat?
    
    **Kenapa penting?** Pembuluh darah yang menyempit mungkin masih bisa mengalirkan darah saat Anda duduk santai (tidak sakit). Tapi saat dipakai lari (olahraga), suplai darah kurang, dan jantung akan "berteriak" kesakitan.
    
    **Dimana saya bisa tahu?** Dari pengalaman observasi diri sendiri, apakah dada selalu terasa ditekan saat digunakan untuk naik tangga atau berolahraga.
    """)

with st.expander("Kenapa perlu Depresi ST (oldpeak)?"):
    st.markdown("""
    **Definisi:** Angka penurunan (depresi) segmen garis ST pada grafik EKG akibat olahraga, dibandingkan saat istirahat.
    
    **Kenapa penting?** Semakin besar angkanya, semakin parah tingkat keparahan sumbatan arteri jantung (menunjukkan otot jantung benar-benar kekurangan oksigen saat beraktivitas).
    
    **Dimana saya bisa tahu?** Ini adalah data teknis yang hanya bisa dibaca oleh dokter Kardiologi dari hasil *print-out* kertas tes EKG Treadmill Anda.
    """)

with st.expander("Apa maksud angka pada Kemiringan Segmen ST (slope)?"):
    st.markdown("""
    **Definisi:** Arah kemiringan garis grafik EKG pada saat detak jantung mencapai puncaknya.
    
    **Arti Angka Dropdown:**
    * **1 (Upsloping):** Garis mengarah ke atas (Normal dan jantung sehat).
    * **2 (Flat):** Garis mendatar (Tanda bahaya aliran darah tidak lancar).
    * **3 (Downsloping):** Garis menurun drastis (Tanda darurat jantung iskemik).
    
    **Kenapa penting?** Bentuk kemiringan garis ini sangat akurat untuk mendeteksi pembuluh darah koroner mana yang tersumbat.
    
    **Dimana saya bisa tahu?** Melalui analisis dokter spesialis jantung berdasarkan tes EKG.
    """)

with st.expander("Kenapa perlu Jumlah Pembuluh Darah Utama (ca)?"):
    st.markdown("""
    **Definisi:** Jumlah pembuluh darah utama di jantung (pilihan angka 0 sampai 3) yang terdeteksi mengalami penyempitan parah.
    
    **Kenapa penting?** Jika angkanya 0, berarti selang darah bersih. Jika angkanya 1, 2, apalagi 3, itu artinya jalan tol utama menuju jantung Anda mengalami kemacetan total akibat sumbatan plak keras.
    
    **Dimana saya bisa tahu?** Melalui operasi kecil bernama Fluoroskopi atau Kateterisasi Jantung (Angiografi) di mana dokter menyuntikkan zat pewarna ke aliran darah jantung.
    """)

with st.expander("Apa maksud angka pada Hasil Thallium Scan (thal)?"):
    st.markdown("""
    **Definisi:** Hasil visualisasi pemindaian nuklir untuk melihat area jantung mana yang dialiri darah dan mana yang tidak.
    
    **Arti Angka Dropdown:**
    * **3 (Normal):** Darah mengalir lancar ke seluruh bagian otot jantung.
    * **6 (Fixed defect):** Ada bagian jantung yang "mati" permanen (biasanya karena ada riwayat serangan jantung sebelumnya).
    * **7 (Reversable defect):** Darah tidak mengalir saat pasien disuruh olahraga, tapi mengalir normal saat disuruh istirahat (penyumbatan fungsional).
    
    **Kenapa penting?** Ini adalah tes pamungkas. Model AI bisa tahu persis dari data ini apakah jantung pasien masih layak bekerja atau sudah mengalami kerusakan jaringan.
    
    **Dimana saya bisa tahu?** Melalui serangkaian tes *Thallium Stress Test* (Kedokteran Nuklir) di rumah sakit fasilitas besar.
    """)