-- =====================================================================
-- DATABASE SQL SCHEMA: TURNITIN AUTOMATED PARAPHRASE TOOL
-- Kompatibel untuk PostgreSQL (Railway / Supabase) dan MySQL / SQLite
-- =====================================================================

-- 1. Tabel Kamus Padanan Kata Permanen (Preferred & Forbidden Synonyms)
CREATE TABLE IF NOT EXISTS dictionary_padanan (
    id SERIAL PRIMARY KEY,
    kata_asal VARCHAR(255) NOT NULL,
    padanan_disukai TEXT NOT NULL,
    padanan_terlarang TEXT,
    konteks VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_padanan_kata_asal ON dictionary_padanan(kata_asal);
CREATE INDEX IF NOT EXISTS idx_padanan_is_active ON dictionary_padanan(is_active);

-- 2. Tabel Istilah dan Entitas Terkunci (Locked Terms & Entities)
CREATE TABLE IF NOT EXISTS locked_terms (
    id SERIAL PRIMARY KEY,
    istilah VARCHAR(255) NOT NULL UNIQUE,
    kategori VARCHAR(100) DEFAULT 'Umum' NOT NULL,
    deskripsi TEXT,
    case_sensitive BOOLEAN DEFAULT TRUE,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_locked_terms_istilah ON locked_terms(istilah);
CREATE INDEX IF NOT EXISTS idx_locked_terms_kategori ON locked_terms(kategori);

-- 3. Tabel Riwayat Job Pemrosesan Dokumen (Paraphrase Jobs)
CREATE TABLE IF NOT EXISTS paraphrase_jobs (
    id VARCHAR(36) PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    original_size INT DEFAULT 0,
    total_paragraphs INT DEFAULT 0,
    narrative_count INT DEFAULT 0,
    locked_count INT DEFAULT 0,
    status VARCHAR(50) DEFAULT 'pending' NOT NULL,
    progress INT DEFAULT 0,
    validation_score FLOAT DEFAULT 100.0,
    file_path TEXT,
    result_path TEXT,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_jobs_status ON paraphrase_jobs(status);
CREATE INDEX IF NOT EXISTS idx_jobs_created_at ON paraphrase_jobs(created_at);

-- 4. Tabel Detail Audit Paragraf (Original vs Paraphrased)
CREATE TABLE IF NOT EXISTS job_paragraphs (
    id SERIAL PRIMARY KEY,
    job_id VARCHAR(36) NOT NULL,
    paragraph_index INT NOT NULL,
    style_name VARCHAR(100),
    classification VARCHAR(50) NOT NULL,
    is_locked BOOLEAN DEFAULT FALSE,
    original_text TEXT NOT NULL,
    paraphrased_text TEXT,
    audit_notes TEXT,
    CONSTRAINT fk_job_paragraphs_job FOREIGN KEY (job_id) REFERENCES paraphrase_jobs(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_job_paras_job_id ON job_paragraphs(job_id);
CREATE INDEX IF NOT EXISTS idx_job_paras_classification ON job_paragraphs(classification);

-- 5. Tabel Temuan Typo pada Elemen Terkunci (Audit Report)
CREATE TABLE IF NOT EXISTS job_typo_reports (
    id SERIAL PRIMARY KEY,
    job_id VARCHAR(36) NOT NULL,
    paragraph_index INT NOT NULL,
    typo_found VARCHAR(255) NOT NULL,
    saran_perbaikan VARCHAR(255),
    catatan TEXT,
    CONSTRAINT fk_job_typos_job FOREIGN KEY (job_id) REFERENCES paraphrase_jobs(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_typo_reports_job_id ON job_typo_reports(job_id);

-- 6. Tabel Pengaturan Sistem & Prompt
CREATE TABLE IF NOT EXISTS system_settings (
    key VARCHAR(100) PRIMARY KEY,
    value TEXT NOT NULL,
    description VARCHAR(255),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================================
-- DATA AWAL (SEED DATA): KAMUS PADANAN KATA & ISTILAH TERKUNCI
-- =====================================================================

-- Seed Padanan Kata Akademik
INSERT INTO dictionary_padanan (kata_asal, padanan_disukai, padanan_terlarang, konteks, is_active) VALUES
('berdasarkan tabel', 'merujuk pada tabel; sesuai data tabel; sebagaimana tertera pada tabel; data empiris pada tabel mengindikasikan', 'menurut tabel', 'Penyajian Data', TRUE),
('secara umum', 'secara komprehensif; secara menyeluruh; secara agregat; pada tataran umum', 'pada umumnya; biasanya', 'Pembahasan', TRUE),
('menunjukkan bahwa', 'mengindikasikan bahwa; merefleksikan bahwa; membuktikan bahwa; mengonfirmasi bahwa', 'memperlihatkan kalau; menampakkan', 'Analisis Data', TRUE),
('mengalami peningkatan', 'membukukan penguatan; mencatatkan kenaikan; bertumbuh secara positif; terapresiasi', 'naik terus; melonjak drastis', 'Statistik Finansial', TRUE),
('mengalami penurunan', 'mengalami penyusutan; tertekan berkala; terkontraksi; melandai; terkoreksi', 'merosot anjlok; jatuh', 'Statistik Finansial', TRUE),
('sangat penting', 'berperan krusial; memegang peranan fundamental; bernilai strategis; berdimensi vital', 'penting sekali', 'Metodologi & Teori', TRUE),
('hal tersebut', 'kondisi ini; dinamika tersebut; realitas empiris ini; fenomena tersebut', 'itu tadi; hal itu', 'Transisi Logis', TRUE),
('oleh karena itu', 'dengan demikian; konsekuensinya; atas pertimbangan tersebut; maka dari itu', 'sebab itu; karenanya', 'Kesimpulan & Argumen', TRUE),
('berbeda-beda', 'bervariasi; heterogen; memperlihatkan disparitas; beragam corak', 'lain-lain; bermacam-macam', 'Deskriptif Statistik', TRUE),
('disebabkan oleh', 'berakar dari; dipicu oleh; bertaut dengan; didorong oleh', 'gara-gara; karena sebab', 'Kausalitas', TRUE),
('berkaitan dengan', 'berkorelasi dengan; bertaut pada; beririsan dengan; bersinggungan dengan', 'nyambung sama; berhubungan', 'Hubungan Teoretis', TRUE),
('dihasilkan oleh', 'diciptakan melalui; dibukukan oleh; diperoleh atas; dikonversi dari', 'dibuat oleh', 'Hasil Kinerja', TRUE),
('memberikan dampak', 'berimplikasi pada; memberi konsekuensi terhadap; memengaruhi konstelasi', 'berakibat pada; membawa efek', 'Pembahasan', TRUE),
('dilakukan dengan', 'dieksekusi melalui; dioperasionalkan berlandaskan; diimplementasikan dengan', 'dibuat pakai', 'Metodologi', TRUE),
('menggunakan rumus', 'mengacu pada formulasi; dihitung berdasarkan persamaan matematis; diformulasikan melalui', 'pakai rumus', 'Normalisasi', TRUE),
('tidak selalu', 'tidak serta-merta; tidak secara otomatis; belum tentu berbanding lurus', 'nggak selalu; tidak mesti', 'Analisis Kritis', TRUE),
('sangat tinggi', 'berada pada level ekspansif; melampaui rata-rata industri; kokoh secara signifikan', 'tinggi banget', 'Rasio Finansial', TRUE),
('sangat rendah', 'berada pada level marjinal; tertekan di batas minimum; relatif terbatas', 'rendah sekali', 'Rasio Finansial', TRUE)
ON CONFLICT DO NOTHING;

-- Seed Istilah Terkunci
INSERT INTO locked_terms (istilah, kategori, deskripsi, case_sensitive, is_active) VALUES
('Otoritas Jasa Keuangan', 'Regulasi', 'Lembaga pengawas jasa keuangan Indonesia', TRUE, TRUE),
('Bank Indonesia', 'Regulasi', 'Bank sentral Republik Indonesia', TRUE, TRUE),
('Undang-Undang No. 21 Tahun 2008', 'Regulasi', 'UU Perbankan Syariah', TRUE, TRUE),
('Kewajiban Penyediaan Modal Minimum', 'Regulasi', 'Istilah resmi KPMM', TRUE, TRUE),
('KPMM', 'Variabel', 'Singkatan regulasi KPMM', TRUE, TRUE),
('Bank Umum Syariah', 'Entitas', 'Kategori BUS', TRUE, TRUE),
('PT Bank Syariah Indonesia Tbk', 'Entitas', 'BSI', TRUE, TRUE),
('Bank Syariah Indonesia', 'Entitas', 'Nama resmi BSI', TRUE, TRUE),
('BSI', 'Entitas', 'Akronim bank BSI', TRUE, TRUE),
('BTPN Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('Bank Mega Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('Bank Muamalat Indonesia', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('BCA Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('Bank Panin Dubai Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('PT Bank Victoria Syariah', 'Entitas', 'Entitas sebelum akuisisi', TRUE, TRUE),
('Bank Victoria Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('PT Bank Syariah Nasional', 'Entitas', 'Entitas pascaakuisisi BTN', TRUE, TRUE),
('Bank Syariah Nasional', 'Entitas', 'Nama bank BUS baru', TRUE, TRUE),
('BSN', 'Entitas', 'Akronim BSN', TRUE, TRUE),
('BTN Syariah', 'Entitas', 'Unit Usaha Syariah BTN', TRUE, TRUE),
('Bank BJB Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('Bank Aceh Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('Bank NTB Syariah', 'Entitas', 'Nama bank BUS', TRUE, TRUE),
('Bank Aladin Syariah', 'Entitas', 'Nama bank BUS digital', TRUE, TRUE),
('Capital Adequacy Ratio', 'Variabel', 'Rasio kecukupan modal', TRUE, TRUE),
('CAR', 'Variabel', 'Singkatan CAR', TRUE, TRUE),
('Return on Assets', 'Variabel', 'Rasio rentabilitas aset', TRUE, TRUE),
('ROA', 'Variabel', 'Singkatan ROA', TRUE, TRUE),
('Return on Equity', 'Variabel', 'Rasio imbal hasil modal', TRUE, TRUE),
('ROE', 'Variabel', 'Singkatan ROE', TRUE, TRUE),
('Biaya Operasional terhadap Pendapatan Operasional', 'Variabel', 'Rasio efisiensi BOPO', TRUE, TRUE),
('BOPO', 'Variabel', 'Singkatan BOPO', TRUE, TRUE),
('Financing to Deposit Ratio', 'Variabel', 'Rasio intermediasi pembiayaan', TRUE, TRUE),
('FDR', 'Variabel', 'Singkatan FDR', TRUE, TRUE),
('Zakat Performance Ratio', 'Variabel', 'Rasio kinerja sosial zakat', TRUE, TRUE),
('ZPR', 'Variabel', 'Singkatan ZPR', TRUE, TRUE),
('Falah Performance Index', 'Teori', 'Indeks kinerja falah', TRUE, TRUE),
('FPI', 'Teori', 'Singkatan FPI', TRUE, TRUE),
('Abu Zahrah', 'Teori', 'Tokoh Maqashid Syariah', TRUE, TRUE),
('maqashid syariah', 'Teori', 'Tujuan hukum syariah', FALSE, TRUE),
('tahdzib al-fard', 'Teori', 'Pilar pendidikan jiwa individu', FALSE, TRUE),
('iqamah al-\'adl', 'Teori', 'Pilar penegakan keadilan', FALSE, TRUE),
('jalb al-maslahah', 'Teori', 'Pilar perwujudan kemaslahatan', FALSE, TRUE),
('hifz al-mal', 'Teori', 'Konsep perlindungan harta', FALSE, TRUE),
('falah', 'Teori', 'Konsep keberhasilan sejati dunia-akhirat', FALSE, TRUE),
('5 Juni 2025', 'Formula', 'Tanggal penuntasan akuisisi Victoria Syariah oleh BTN', TRUE, TRUE),
('2 Oktober 2025', 'Formula', 'Tanggal peluncuran identitas baru BSN', TRUE, TRUE),
('22 Desember 2025', 'Formula', 'Tanggal efektif pengalihan hak/kewajiban BTN Syariah ke BSN', TRUE, TRUE)
ON CONFLICT (istilah) DO NOTHING;

-- Seed System Prompt
INSERT INTO system_settings (key, value, description) VALUES
('MASTER_SYSTEM_PROMPT', 'MASTER PROMPT PARAFRASE AKADEMIK — STRICT FORMAT LOCK, CONTENT PRESERVATION & SELF-VALIDATION FRAMEWORK', 'Framework utama parafrase Turnitin anti-rusak format dan anti-korupsi data.'),
('GEMINI_MODEL', 'gemini-2.5-flash', 'Model Gemini yang digunakan untuk parafrase otomatis.'),
('DEFAULT_BATCH_SIZE', '5', 'Jumlah paragraf naratif per batch request ke LLM.')
ON CONFLICT (key) DO NOTHING;
