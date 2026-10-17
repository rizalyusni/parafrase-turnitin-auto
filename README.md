# 🛡️ Turnitin Paraphrase Automator — Strict Format Lock & SQL Thesaurus

Aplikasi web dan backend API otomasi parafrase Turnitin untuk naskah akademik (skripsi, tesis, disertasi, jurnal ilmiah) dengan **penguncian format 100%**, proteksi tabel, persamaan matematika (*oMath*), sitasi Mendeley/Zotero, serta kamus padanan kata permanen berbasis database SQL.

Dibangun khusus untuk memenuhi standar:
> **MASTER PROMPT PARAFRASE AKADEMIK — STRICT FORMAT LOCK, CONTENT PRESERVATION & SELF-VALIDATION FRAMEWORK**

---

## 🌟 Fitur Utama

1. **Strict Format Lock 100%**:
   - Menjaga seluruh **48 tabel** dan setiap sel (2.892 sel) *byte-for-byte* identik.
   - Mengunci seluruh **52 objek rumus matematika Word (*oMath / oMathPara*)**, notasi $r_{ij}$, $d_i$, $w_i$, dan $FPI_i$.
   - Mengunci judul bab, subbab, nomor urut, serta margin halaman dan section setup.
2. **Kamus Padanan Kata SQL Permanen**:
   - Menggantikan kata/frasa berulang dengan diksi akademik formal tanpa menghasilkan sinonim mekanis yang janggal.
   - Daftar kata terlarang untuk mencegah istilah klise dan informal.
   - Manajemen CRUD interaktif melalui antarmuka web.
3. **Preservasi Entitas & Data Kritis**:
   - Menjamin 100% angka persentase, statistik, dan rasio (CAR, ROA, ROE, BOPO, FDR, ZPR).
   - Menjaga entitas bank syariah (BSI, BCA Syariah, BTPN Syariah, Bank Muamalat, BSN, dll.) dan kronologi regulasi (akuisisi BTN 5 Juni 2025, peluncuran BSN 2 Oktober 2025, integrasi 22 Desember 2025).
4. **Self-Validation Framework (Tahap 1–4, Checklist A–E)**:
   - Verifikasi otomatis terhadap integritas struktur, proteksi elemen terkunci, dan preservasi data empiris.
   - Menghasilkan laporan temuan *typo* pada bagian terkunci tanpa mengubah teks aslinya secara sepihak.
5. **Modern Responsive Web UI**:
   - Tampilan bersih berbasis Tailwind CSS dan Lucide Icons.
   - Drag-and-drop upload file `.docx`.
   - Real-time progress bar, live comparison diff viewer, dan one-click download file Word hasil parafrase.
6. **Siap Deploy ke Railway**:
   - Mendukung PostgreSQL (Railway Database) dengan fallback otomatis ke SQLite lokal.
   - Dilengkapi `Dockerfile`, `railway.json`, `Procfile`, dan `schema.sql`.

---

## 🚀 Panduan Menjalankan Secara Lokal

### 1. Prasyarat
- Python 3.10 atau 3.11
- Git

### 2. Instalasi Dependensi
```bash
git clone https://github.com/rizalyusni/parafrase-turnitin-auto.git
cd parafrase-turnitin-auto

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Konfigurasi Lingkungan (Opsional)
Salin `.env.example` menjadi `.env`:
```bash
cp .env.example .env
```
*(Jika ingin menggunakan AI Gemini untuk parafrase dinamis, masukkan `GEMINI_API_KEY` Anda di `.env`. Jika tidak diisi, aplikasi akan menggunakan mesin transformasi akademik internal berbasis aturan baku).*

### 4. Menjalankan Aplikasi
```bash
uvicorn main:app --reload --port 8000
```
Buka browser di: **http://localhost:8000**

---

## ☁️ Panduan Deployment ke Railway (1-Click)

Aplikasi telah disiapkan lengkap dengan `Dockerfile` dan `railway.json` untuk Railway:

1. **Push source code ke GitHub**:
   ```bash
   git add .
   git commit -m "feat: turnitin paraphrase automator with strict lock and sql thesaurus"
   git branch -M main
   git push -u origin main
   ```
2. **Buka Dashboard Railway**:
   - Masuk ke [railway.app](https://railway.app).
   - Klik **New Project** -> **Deploy from GitHub repo**.
   - Pilih repository: `rizalyusni/parafrase-turnitin-auto`.
3. **Tambahkan Database PostgreSQL di Railway**:
   - Pada proyek Railway Anda, klik **+ New** -> **Database** -> **Add PostgreSQL**.
   - Railway akan otomatis menginjeksi variabel `DATABASE_URL` ke service aplikasi Anda.
4. **Pengaturan Variabel Lingkungan (Environment Variables)**:
   - Tambahkan variabel (opsional):
     - `GEMINI_API_KEY`: Kunci API Google Gemini Anda.
5. **Selesai!** Railway akan otomatis mem-build image Docker dan menyediakan URL publik (HTTPS) untuk aplikasi Anda.

---

## 🗄️ Struktur Database SQL (`schema.sql`)

Tabel utama yang dikelola oleh SQLAlchemy & SQL:
1. `dictionary_padanan`: Kamus permanen padanan kata disukai dan terlarang.
2. `locked_terms`: Daftar istilah, entitas perbankan, dan regulasi yang dilindungi mutlak.
3. `paraphrase_jobs`: Rekam jejak pemrosesan dokumen, status, dan skor audit validasi.
4. `job_paragraphs`: Detail audit teks asli vs teks hasil parafrase per paragraf.
5. `job_typo_reports`: Log temuan kesalahan ketik pada subjudul atau formula terkunci.
6. `system_settings`: Konfigurasi Master Prompt dan model AI.

---

## 📄 Lisensi
Hak Cipta © 2026. Dikembangkan untuk peningkatan integritas penulisan karya ilmiah akademik.
