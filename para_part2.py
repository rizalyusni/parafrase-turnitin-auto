# -*- coding: utf-8 -*-
"""
Part 2: Bab V (Normalisasi Matriks Keputusan 2021 & FPI 2021, Normalisasi 2022 & FPI 2022).
Total: 35 paragraphs
"""

PART2_PARAPHRASES = {
    104: (
        "Pada tahun 2021, batas minimum CAR/KPMM berada pada level 20,02% sedangkan nilai maksimum menyentuh 390,50%. "
        "Mengacu pada sebaran rentang tersebut, kalkulasi normalisasi permodalan untuk Bank Syariah Indonesia diformulasikan sebagai berikut:"
    ),
    112: (
        "Rasio ROA diperlakukan sebagai benefit criterion; dengan demikian, peningkatan efisiensi aset dalam menghasilkan surplus "
        "akan berkorelasi positif dengan perolehan skor normalisasi yang kian mendekati angka 1,0000. Formulasi normalisasi ROA dirumuskan melalui:"
    ),
    114: (
        "Rentang ROA industri pada 2021 bergerak dari titik terendah -8,81% pada Bank Aladin Syariah hingga titik tertinggi 10,72% "
        "pada BTPN Syariah. Berdasarkan sebaran nilai ekstrem tersebut, skor normalisasi ROA untuk Bank Syariah Indonesia dihitung melalui:"
    ),
    126: (
        "Indikator ROE diposisikan dalam kategori benefit criterion, di mana profitabilitas ekuitas yang lebih tinggi merepresentasikan "
        "penciptaan nilai pemegang saham yang optimal dan diganjar dengan nilai normalisasi yang semakin mendekati 1,0000. "
        "Adapun prosedur normalisasinya dihitung dengan persamaan:"
    ),
    128: (
        "Sepanjang tahun 2021, perolehan ROE terendah tercatat sebesar -31,76% pada Bank Panin Dubai Syariah, sementara perolehan "
        "tertinggi dicapai oleh Bank Mega Syariah sebesar 28,48%. Dari rentang nilai ekstrem tersebut, normalisasi ROE Bank Syariah Indonesia "
        "dieksekusi sebagai berikut:"
    ),
    138: (
        "Indikator BOPO berkarakter cost criterion, mengingat esensi efisiensi operasional menuntut pemangkasan rasio biaya terhadap "
        "pendapatan operasional. Dalam kerangka ini, bank yang mampu meminimalkan beban operasionalnya berhak atas nilai normalisasi "
        "yang lebih tinggi. Skema transformasi nilai BOPO dijalankan menggunakan rumus:"
    ),
    140: (
        "Batas bawah BOPO tahun 2021 dicatatkan oleh BTPN Syariah sebesar 59,97%, sedangkan batas atas operasional tertinggi dialami "
        "Bank Aladin Syariah sebesar 428,40%. Atas dasar sebaran tersebut, besaran normalisasi BOPO untuk Bank Syariah Indonesia dihitung sebagai berikut:"
    ),
    153: (
        "Rasio FDR diklasifikasikan sebagai target criterion karena ekspansi pembiayaan yang defisit maupun berlebihan sama-sama "
        "mengandung risiko struktural perbankan. Penelitian ini menetapkan rentang 84%–94% sebagai koridor intermediasi optimal. "
        "Capaian FDR yang beroperasi tepat di dalam rentang tersebut diberikan deviasi jarak nol, sedangkan deviasi di luar batas koridor "
        "dihitung dari selisih mutlak terhadap ambang terdekat sesuai persamaan:"
    ),
    173: (
        "ZPR difungsikan sebagai benefit criterion guna mengukur kontribusi kebajikan, di mana proporsi alokasi zakat terhadap aset "
        "bersih yang semakin besar akan menghasilkan nilai normalisasi yang kian mendekati 1,0000. Normalisasi ZPR dirumuskan melalui:"
    ),
    177: (
        "Pada tahun 2021, batas bawah alokasi ZPR berada pada angka 0,0000%, sedangkan capaian tertinggi dibukukan Bank Syariah Indonesia "
        "sebesar 0,5102%. Perhitungan normalisasi ZPR untuk Bank Muamalat Indonesia diuraikan melalui:"
    ),
    185: (
        "Mengacu pada rekapitulasi normalisasi 2021, Bank Syariah Indonesia mengamankan skor ZPR sempurna 1,0000 berkat posisinya sebagai "
        "kontributor zakat tertinggi. Sebaliknya, BTPN Syariah dan Bank Aladin Syariah memperoleh skor normalisasi 0,0000 akibat ketiadaan "
        "alokasi zakat berbasis aset bersih pada tahun tersebut."
    ),
    187: (
        "Setelah seluruh indikator tahun 2021 tertransformasi sesuai sifat kriteria benefit, cost, maupun target, seluruh skor dihimpun "
        "ke dalam matriks normalisasi terpadu. Matriks ini merangkum skor terstandarisasi CAR/KPMM, ROA, ROE, BOPO, FDR, dan ZPR bagi "
        "seluruh Bank Umum Syariah sampel. Selanjutnya diterapkan equal weighting, yakni pembobotan seragam 1/6 (16,67%) untuk tiap-tiap "
        "indikator. Agregasi linier antara perkalian bobot dan nilai normalisasi tersebut menghasilkan skor akhir Falah Performance Index (FPI) 2021."
    ),
    205: (
        "Berdasarkan agregasi pembobotan tersebut, Bank Syariah Indonesia membukukan nilai indeks FPI sebesar 0,6853 pada 2021. "
        "Skor komposit ini merefleksikan konvergensi performa dari keenam indikator yang telah distandardisasi secara berimbang. "
        "Besaran FPI seluruh sampel kemudian dijadikan tolok ukur hierarki performa Bank Umum Syariah pada periode 2021."
    ),
    207: (
        "Hasil pengukuran Falah Performance Index (FPI) 2021 menempatkan Bank Syariah Indonesia di peringkat teratas dengan skor 0,6853. "
        "BTPN Syariah membuntuti di posisi kedua dengan raihan 0,6683, disusul Bank Mega Syariah di peringkat ketiga sebesar 0,6425. "
        "Adapun posisi keempat dan kelima masing-masing diduduki oleh Bank NTB Syariah (0,5526) dan Bank Aceh Syariah (0,5249)."
    ),
    208: (
        "Peringkat keenam diisi BCA Syariah dengan FPI 0,5088, terpaut tipis dari Bank BJB Syariah di posisi ketujuh dengan skor 0,5084. "
        "Selanjutnya, Bank Victoria Syariah/Bank Syariah Nasional menempati urutan kedelapan (0,4643) dan Bank Muamalat Indonesia berada di peringkat "
        "kesembilan (0,4575). Urutan terbawah dihuni oleh Bank Panin Dubai Syariah di posisi kesepuluh (0,2647) serta Bank Aladin Syariah di posisi "
        "kesebelas (0,2266)."
    ),
    209: (
        "Distribusi pemeringkatan ini memetakan posisi relatif setiap Bank Umum Syariah berdasarkan kinerja simultan keenam indikator pada 2021. "
        "Tingginya nilai indeks mengindikasikan keunggulan agregat bank dalam menyeimbangkan aspek ketahanan finansial, efisiensi, fungsi "
        "intermediasi, dan mandat sosial."
    ),
    211: (
        "Tahapan analisis berlanjut pada normalisasi matriks keputusan tahun 2022 guna menyetarakan skala dan dimensi pengukuran lintas indikator. "
        "Standardisasi ini menjadi prasyarat esensial agar perbandingan antar-BUS dapat dilakukan secara adil sebelum diintegrasikan ke dalam "
        "Falah Performance Index (FPI). Prosedur matematis disesuaikan dengan tipologi masing-masing rasio, mencakup benefit, cost, dan target criterion."
    ),
    213: (
        "Sebagai kriteria benefit, kecukupan modal (CAR/KPMM) menuntut nilai rasio yang tinggi guna mengoptimalkan bantalan risiko. "
        "Semakin kokoh modal bank syariah, semakin tinggi skor normalisasi yang diperoleh. Transformasi nilai dilakukan dengan persamaan:"
    ),
    219: (
        "Berdasarkan hasil standardisasi CAR/KPMM 2022, Bank Aladin Syariah memimpin perolehan dengan skor normalisasi tertinggi 1,0000, "
        "sedangkan Bank Syariah Indonesia mencatatkan skor normalisasi permodalan terendah sebesar 0,0000 dalam sebaran sampel tahun tersebut."
    ),
    221: (
        "Indikator ROA dikonstruksikan sebagai kriteria benefit, di mana efektivitas pengelolaan aset dalam menghasilkan laba bersih "
        "akan dihargai dengan perolehan skor normalisasi yang kian mendekati angka 1,0000. Formulasi perhitungannya mengacu pada:"
    ),
    226: (
        "Hasil pengolahan data ROA tahun 2022 menunjukkan bahwa BTPN Syariah sukses mendulang skor normalisasi sempurna 1,0000, "
        "sementara Bank Aladin Syariah membukukan skor terendah 0,0000 akibat tekanan profitabilitas aset pada tahun berkenaan."
    ),
    228: (
        "Diposisikan dalam kriteria benefit, kenaikan rasio ROE mencerminkan kepiawaian manajemen dalam memberikan imbal hasil optimal "
        "atas ekuitas pemegang saham, yang ditransformasikan menuju skor maksimal 1,0000 melalui rumus:"
    ),
    237: (
        "Melalui kalkulasi normalisasi ROE 2022, BTPN Syariah kembali mengamankan skor puncak 1,0000 berkat efisiensi ekuitasnya yang unggul, "
        "sedangkan Bank Aladin Syariah menempati posisi dasar dengan skor 0,0000."
    ),
    239: (
        "Indikator BOPO diperlakukan sebagai kriteria cost; penghematan beban operasional terhadap pendapatan mencerminkan efisiensi internal "
        "yang unggul sehingga rasio yang lebih rendah menghasilkan skor normalisasi yang lebih tinggi mendekati 1,0000 melalui rumus:"
    ),
    245: (
        "Berdasarkan tabel normalisasi BOPO 2022, BTPN Syariah meraih nilai normalisasi tertinggi 1,0000 berkat kemampuan menekan beban "
        "operasional ke level paling hemat. Sebaliknya, Bank Aladin Syariah menempati skor normalisasi 0,0000 karena membukukan rasio BOPO "
        "tertinggi pada tahun yang sama."
    ),
    249: (
        "FDR dioperasionalkan sebagai target criterion mengingat penyaluran pembiayaan yang terlalu ekspansif memicu risiko likuiditas, "
        "sedangkan rasio yang terlampau rendah mengindikasikan disfungsi intermediasi. Rentang sasaran dipatok pada 84%–94%, di mana deviasi "
        "nol berlaku bagi capaian di dalam koridor, sementara deviasi nilai di luar koridor dihitung dari ambang terdekat menggunakan rumus:"
    ),
    254: (
        "Hasil normalisasi FDR 2022 menempatkan Bank NTB Syariah pada skor tertinggi 1,0000 karena rasio pembiayaannya berhasil mendarat "
        "presisi dalam batas target 84%–94%. Adapun Bank Aladin Syariah memperoleh skor 0,0000 lantaran mencatatkan deviasi penyaluran dana "
        "paling lebar dari rentang sasaran."
    ),
    256: (
        "Sesuai hakikatnya sebagai indikator kebajikan sosial, ZPR tergolong benefit criterion, di mana komitmen penyaluran zakat yang lebih besar "
        "secara proporsional terhadap aset bersih menghasilkan nilai normalisasi yang semakin tinggi melalui rumus:"
    ),
    262: (
        "Pada indikator ZPR 2022, Bank Mega Syariah berhasil merebut nilai normalisasi tertinggi 1,0000 berkat intensitas penyaluran zakat "
        "tertinggi. Sementara itu, skor dasar 0,0000 tercatat pada BTPN Syariah dan Bank Panin Dubai Syariah akibat nihilnya alokasi zakat korporasi "
        "berbasis aset bersih pada tahun tersebut."
    ),
    264: (
        "Seluruh capaian terstandardisasi tahun 2022 selanjutnya dikompilasi ke dalam matriks normalisasi komprehensif yang memuat skor CAR/KPMM, "
        "ROA, ROE, BOPO, FDR, dan ZPR bagi tiap-tiap entitas bank syariah. Prinsip equal weighting kembali diterapkan dengan mengalokasikan bobot "
        "seimbang sebesar 1/6 (16,67%) per indikator. Penjumlahan hasil kali matriks dan bobot menghasilkan skor komposit Falah Performance "
        "Index (FPI) untuk periode 2022."
    ),
    269: (
        "Hasil agregasi multikriteria tahun 2022 menyajikan spektrum performa komposit yang beragam pada perbankan syariah Indonesia. "
        "BTPN Syariah sukses memuncaki indeks dengan skor FPI 0,6961, sedangkan Bank Aladin Syariah berada di posisi terendah dengan skor 0,1674. "
        "Raihan FPI ini selanjutnya menjadi pijakan utama dalam penyusunan peringkat kinerja relatif bank pada 2022."
    ),
    271: (
        "Penyusunan hierarki kinerja 2022 dilakukan secara sistematis dengan mengurutkan nilai akhir FPI dari yang tertinggi hingga terendah. "
        "Struktur pemeringkatan ini mengonfirmasi posisi relatif masing-masing Bank Umum Syariah dalam menyelaraskan indikator finansial dan sosial."
    ),
    276: (
        "Evaluasi FPI tahun 2022 menobatkan BTPN Syariah di peringkat pertama dengan perolehan skor 0,6961. Bank Syariah Indonesia menempati "
        "peringkat kedua dengan skor 0,6464, dibuntuti ketat oleh Bank Mega Syariah pada posisi ketiga dengan perolehan 0,6433."
    ),
    277: (
        "Peringkat keempat diamankan Bank Victoria Syariah/Bank Syariah Nasional dengan skor FPI 0,5613, disusul Bank NTB Syariah di peringkat "
        "kelima (0,5428) dan Bank Aceh Syariah di posisi keenam (0,5284). Selanjutnya, peringkat ketujuh hingga kesembilan masing-masing "
        "ditempati oleh Bank Panin Dubai Syariah (0,5146), Bank BJB Syariah (0,4929), dan BCA Syariah (0,4833)."
    ),
    278: (
        "Papan bawah dihuni oleh Bank Muamalat Indonesia di peringkat kesepuluh dengan nilai 0,3888 serta Bank Aladin Syariah di posisi "
        "kesebelas dengan capaian 0,1674. Urutan ini merefleksikan posisi absolut dan kinerja komparatif masing-masing Bank Umum Syariah "
        "berdasarkan agregasi enam indikator falah sepanjang tahun 2022."
    ),
}
