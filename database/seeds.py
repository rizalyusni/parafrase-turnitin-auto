# -*- coding: utf-8 -*-
"""
Seed data for permanent vocabulary dictionary (padanan kata)
and protected locked terms.
"""
from sqlalchemy.orm import Session
from database.models import PadananKata, IstilahTerkunci, SystemSetting

INITIAL_PADANAN = [
    # Academic & Empirical Verbs / Connectors
    {"kata_asal": "berdasarkan tabel", "padanan_disukai": "merujuk pada tabel; sesuai data tabel; sebagaimana tertera pada tabel; data empiris pada tabel mengindikasikan", "padanan_terlarang": "menurut tabel", "konteks": "Penyajian Data"},
    {"kata_asal": "secara umum", "padanan_disukai": "secara komprehensif; secara menyeluruh; secara agregat; pada tataran umum", "padanan_terlarang": "pada umumnya; biasanya", "konteks": "Pembahasan"},
    {"kata_asal": "menunjukkan bahwa", "padanan_disukai": "mengindikasikan bahwa; merefleksikan bahwa; membuktikan bahwa; mengonfirmasi bahwa", "padanan_terlarang": "memperlihatkan kalau; menampakkan", "konteks": "Analisis Data"},
    {"kata_asal": "mengalami peningkatan", "padanan_disukai": "membukukan penguatan; mencatatkan kenaikan; bertumbuh secara positif; terapresiasi", "padanan_terlarang": "naik terus; melonjak drastis", "konteks": "Statistik Finansial"},
    {"kata_asal": "mengalami penurunan", "padanan_disukai": "mengalami penyusutan; tertekan berkala; terkontraksi; melandai; terkoreksi", "padanan_terlarang": "merosot anjlok; jatuh", "konteks": "Statistik Finansial"},
    {"kata_asal": "sangat penting", "padanan_disukai": "berperan krusial; memegang peranan fundamental; bernilai strategis; berdimensi vital", "padanan_terlarang": "penting sekali", "konteks": "Metodologi & Teori"},
    {"kata_asal": "hal tersebut", "padanan_disukai": "kondisi ini; dinamika tersebut; realitas empiris ini; fenomena tersebut", "padanan_terlarang": "itu tadi; hal itu", "konteks": "Transisi Logis"},
    {"kata_asal": "oleh karena itu", "padanan_disukai": "dengan demikian; konsekuensinya; atas pertimbangan tersebut; maka dari itu", "padanan_terlarang": "sebab itu; karenanya", "konteks": "Kesimpulan & Argumen"},
    {"kata_asal": "berbeda-beda", "padanan_disukai": "bervariasi; heterogen; memperlihatkan disparitas; beragam corak", "padanan_terlarang": "lain-lain; bermacam-macam", "konteks": "Deskriptif Statistik"},
    {"kata_asal": "disebabkan oleh", "padanan_disukai": "berakar dari; dipicu oleh; bertaut dengan; didorong oleh", "padanan_terlarang": "gara-gara; karena sebab", "konteks": "Kausalitas"},
    {"kata_asal": "berkaitan dengan", "padanan_disukai": "berkorelasi dengan; bertaut pada; beririsan dengan; bersinggungan dengan", "padanan_terlarang": "nyambung sama; berhubungan", "konteks": "Hubungan Teoretis"},
    {"kata_asal": "dihasilkan oleh", "padanan_disukai": "diciptakan melalui; dibukukan oleh; diperoleh atas; dikonversi dari", "padanan_terlarang": "dibuat oleh", "konteks": "Hasil Kinerja"},
    {"kata_asal": "memberikan dampak", "padanan_disukai": "berimplikasi pada; memberi konsekuensi terhadap; memengaruhi konstelasi", "padanan_terlarang": "berakibat pada; membawa efek", "konteks": "Pembahasan"},
    {"kata_asal": "dilakukan dengan", "padanan_disukai": "dieksekusi melalui; dioperasionalkan berlandaskan; diimplementasikan dengan", "padanan_terlarang": "dibuat pakai", "konteks": "Metodologi"},
    {"kata_asal": "menggunakan rumus", "padanan_disukai": "mengacu pada formulasi; dihitung berdasarkan persamaan matematis; diformulasikan melalui", "padanan_terlarang": "pakai rumus", "konteks": "Normalisasi"},
    {"kata_asal": "tidak selalu", "padanan_disukai": "tidak serta-merta; tidak secara otomatis; belum tentu berbanding lurus", "padanan_terlarang": "nggak selalu; tidak mesti", "konteks": "Analisis Kritis"},
    {"kata_asal": "sangat tinggi", "padanan_disukai": "berada pada level ekspansif; melampaui rata-rata industri; kokoh secara signifikan", "padanan_terlarang": "tinggi banget", "konteks": "Rasio Finansial"},
    {"kata_asal": "sangat rendah", "padanan_disukai": "berada pada level marjinal; tertekan di batas minimum; relatif terbatas", "padanan_terlarang": "rendah sekali", "konteks": "Rasio Finansial"},
]

INITIAL_LOCKED_TERMS = [
    # Peraturan & Regulasi
    {"istilah": "Otoritas Jasa Keuangan", "kategori": "Regulasi", "deskripsi": "Lembaga pengawas jasa keuangan Indonesia"},
    {"istilah": "Bank Indonesia", "kategori": "Regulasi", "deskripsi": "Bank sentral Republik Indonesia"},
    {"istilah": "Undang-Undang No. 21 Tahun 2008", "kategori": "Regulasi", "deskripsi": "UU Perbankan Syariah"},
    {"istilah": "Kewajiban Penyediaan Modal Minimum", "kategori": "Regulasi", "deskripsi": "Istilah hukum KPMM perbankan"},
    {"istilah": "KPMM", "kategori": "Variabel", "deskripsi": "Singkatan regulasi KPMM"},
    
    # Entitas Bank Umum Syariah
    {"istilah": "Bank Umum Syariah", "kategori": "Entitas", "deskripsi": "Kategori BUS"},
    {"istilah": "PT Bank Syariah Indonesia Tbk", "kategori": "Entitas", "deskripsi": "BSI"},
    {"istilah": "Bank Syariah Indonesia", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "BSI", "kategori": "Entitas", "deskripsi": "Akronim bank"},
    {"istilah": "BTPN Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "Bank Mega Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "Bank Muamalat Indonesia", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "BCA Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "Bank Panin Dubai Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "PT Bank Victoria Syariah", "kategori": "Entitas", "deskripsi": "Entitas sebelum akuisisi"},
    {"istilah": "Bank Victoria Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "PT Bank Syariah Nasional", "kategori": "Entitas", "deskripsi": "Entitas pascaakuisisi BTN"},
    {"istilah": "Bank Syariah Nasional", "kategori": "Entitas", "deskripsi": "Nama bank BUS baru"},
    {"istilah": "BSN", "kategori": "Entitas", "deskripsi": "Akronim BSN"},
    {"istilah": "BTN Syariah", "kategori": "Entitas", "deskripsi": "Unit Usaha Syariah BTN"},
    {"istilah": "Bank BJB Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "Bank Aceh Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "Bank NTB Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS"},
    {"istilah": "Bank Aladin Syariah", "kategori": "Entitas", "deskripsi": "Nama bank BUS digital"},

    # Rasio & Metodologi
    {"istilah": "Capital Adequacy Ratio", "kategori": "Variabel", "deskripsi": "Rasio kecukupan modal"},
    {"istilah": "CAR", "kategori": "Variabel", "deskripsi": "Singkatan CAR"},
    {"istilah": "Return on Assets", "kategori": "Variabel", "deskripsi": "Rasio rentabilitas aset"},
    {"istilah": "ROA", "kategori": "Variabel", "deskripsi": "Singkatan ROA"},
    {"istilah": "Return on Equity", "kategori": "Variabel", "deskripsi": "Rasio imbal hasil modal"},
    {"istilah": "ROE", "kategori": "Variabel", "deskripsi": "Singkatan ROE"},
    {"istilah": "Biaya Operasional terhadap Pendapatan Operasional", "kategori": "Variabel", "deskripsi": "BOPO"},
    {"istilah": "Beban Operasional Terhadap Pendapatan Operasional", "kategori": "Variabel", "deskripsi": "BOPO varian"},
    {"istilah": "BOPO", "kategori": "Variabel", "deskripsi": "Singkatan BOPO"},
    {"istilah": "Financing to Deposit Ratio", "kategori": "Variabel", "deskripsi": "Rasio intermediasi pembiayaan"},
    {"istilah": "FDR", "kategori": "Variabel", "deskripsi": "Singkatan FDR"},
    {"istilah": "Zakat Performance Ratio", "kategori": "Variabel", "deskripsi": "Rasio kinerja sosial zakat"},
    {"istilah": "ZPR", "kategori": "Variabel", "deskripsi": "Singkatan ZPR"},
    {"istilah": "Falah Performance Index", "kategori": "Teori", "deskripsi": "Indeks kinerja falah"},
    {"istilah": "FPI", "kategori": "Teori", "deskripsi": "Singkatan FPI"},

    # Teori & Syariah
    {"istilah": "Abu Zahrah", "kategori": "Teori", "deskripsi": "Tokoh Maqashid Syariah"},
    {"istilah": "maqashid syariah", "kategori": "Teori", "deskripsi": "Tujuan hukum syariah"},
    {"istilah": "tahdzib al-fard", "kategori": "Teori", "deskripsi": "Pilar pendidikan jiwa individu"},
    {"istilah": "iqamah al-'adl", "kategori": "Teori", "deskripsi": "Pilar penegakan keadilan"},
    {"istilah": "jalb al-maslahah", "kategori": "Teori", "deskripsi": "Pilar perwujudan kemaslahatan"},
    {"istilah": "hifz al-mal", "kategori": "Teori", "deskripsi": "Konsep perlindungan harta"},
    {"istilah": "falah", "kategori": "Teori", "deskripsi": "Konsep keberhasilan sejati dunia-akhirat"},

    # Tanggal Krusial
    {"istilah": "5 Juni 2025", "kategori": "Formula", "deskripsi": "Tanggal penuntasan akuisisi Victoria Syariah oleh BTN"},
    {"istilah": "2 Oktober 2025", "kategori": "Formula", "deskripsi": "Tanggal peluncuran identitas baru BSN"},
    {"istilah": "22 Desember 2025", "kategori": "Formula", "deskripsi": "Tanggal efektif pengalihan hak/kewajiban BTN Syariah ke BSN"},
]

def seed_database(db: Session):
    """Inserts initial padanan kata and locked terms if table is empty."""
    if db.query(PadananKata).count() == 0:
        for p in INITIAL_PADANAN:
            db.add(PadananKata(**p))
            
    if db.query(IstilahTerkunci).count() == 0:
        for term in INITIAL_LOCKED_TERMS:
            db.add(IstilahTerkunci(**term))
            
    # Check default system settings
    default_prompt_key = "MASTER_SYSTEM_PROMPT"
    if not db.query(SystemSetting).filter_by(key=default_prompt_key).first():
        db.add(SystemSetting(
            key=default_prompt_key,
            value="MASTER PROMPT PARAFRASE AKADEMIK — STRICT FORMAT LOCK, CONTENT PRESERVATION & SELF-VALIDATION FRAMEWORK",
            description="Framework utama parafrase Turnitin anti-rusak format dan anti-korupsi data."
        ))
        
    db.commit()
