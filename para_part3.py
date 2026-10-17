# -*- coding: utf-8 -*-
"""
Part 3: Bab V (Normalisasi Matriks Keputusan 2023, 2024, 2025 & Perhitungan FPI Tahunan).
Total: 44 paragraphs
"""

PART3_PARAPHRASES = {
    282: (
        "Analisis data berlanjut pada periode 2023 dengan mengonstruksi matriks keputusan berbasis enam indikator fundamental "
        "Bank Umum Syariah: CAR/KPMM, ROA, ROE, BOPO, FDR, dan ZPR. Matriks ini mendokumentasikan besaran empiris aktual setiap bank "
        "sebelum diproses melalui standardisasi skala dan komputasi Falah Performance Index (FPI)."
    ),
    286: (
        "Sebaran nilai pada matriks keputusan 2023 memperlihatkan disparitas unit dan rentang skala yang lebar antarbank syariah. "
        "Konsekuensinya, normalisasi data mutlak dilakukan selaras dengan karakteristik masing-masing indikator guna menghasilkan "
        "skor terstandarisasi yang valid untuk perumusan indeks komposit Falah Performance Index (FPI)."
    ),
    294: (
        "Hasil standardisasi CAR/KPMM tahun 2023 menempatkan Bank Aladin Syariah pada raihan skor tertinggi 1,0000 berkat ekspansi "
        "modal dasarnya, sedangkan Bank BJB Syariah memperoleh skor normalisasi terendah 0,0000 di antara kelompok bank sampel."
    ),
    296: (
        "Sebagai benefit criterion, rasio ROA memproyeksikan efektivitas pengelolaan aset; peningkatan kapasitas menghasilkan surplus "
        "akan mengerek nilai normalisasi mendekati angka maksimal 1,0000 berdasarkan formulasi:"
    ),
    302: (
        "Melalui kalkulasi normalisasi ROA 2023, BTPN Syariah kembali menduduki peringkat teratas dengan skor 1,0000 berkat keunggulan marginnya, "
        "sementara Bank Aladin Syariah mencatatkan skor dasar 0,0000 akibat tekanan profitabilitas pada tahun berjalan."
    ),
    304: (
        "Kriteria benefit pada rasio ROE mengimplikasikan bahwa imbal hasil ekuitas yang kian optimal akan menghasilkan apresiasi "
        "nilai normalisasi yang kian mendekati 1,0000 sesuai rumus matematis:"
    ),
    310: (
        "Hasil pengukuran normalisasi ROE 2023 mencatatkan Bank Syariah Indonesia di posisi teratas dengan perolehan skor sempurna 1,0000, "
        "sedangkan posisi terbawah dengan skor 0,0000 kembali ditempati oleh Bank Aladin Syariah."
    ),
    312: (
        "Ditetapkan sebagai cost criterion, rasio BOPO memandang efisiensi biaya sebagai pencapaian positif; semakin tertekan beban operasional "
        "terhadap pendapatan, semakin tinggi skor normalisasi yang dianugerahkan melalui rumus:"
    ),
    319: (
        "Pada tahun 2023, Bank Syariah Indonesia meraih skor normalisasi BOPO tertinggi sebesar 1,0000 berkat struktur operasional yang "
        "paling efisien. Sebaliknya, Bank Aladin Syariah membukukan nilai normalisasi terendah pada kisaran 0,5900 akibat tingginya beban "
        "operasional pada fase ekspansi bisnisnya."
    ),
    321: (
        "Perlakuan FDR sebagai target criterion didasarkan pada prinsip kehati-hatian, di mana ekspansi pembiayaan yang defisit maupun "
        "berlebihan sama-sama menyimpan risiko. Penelitian mematok koridor sasaran 84%–94% dengan jarak deviasi nol, sedangkan "
        "capaian di luar batas tersebut dihitung jarak mutlaknya terhadap ambang batas terdekat menggunakan formula:"
    ),
    327: (
        "Berdasarkan hasil normalisasi FDR 2023, BTPN Syariah, Bank Panin Dubai Syariah, dan Bank BJB Syariah serentak mengamankan skor "
        "tertinggi 1,0000 berkat rasio pembiayaan yang mendarat presisi dalam koridor target 84%–94%. Di sisi lain, Bank Muamalat Indonesia "
        "mencatat skor terendah 0,0000 akibat simpangan penyaluran dana yang paling lebar dari batas target."
    ),
    329: (
        "Mengemban kriteria benefit, kenaikan rasio ZPR mencerminkan komitmen filantropi institusional yang kian mendalam, di mana "
        "proporsi alokasi zakat yang lebih besar terhadap aset bersih diganjar skor normalisasi mendekati 1,0000 melalui rumus:"
    ),
    335: (
        "Standardisasi ZPR 2023 menempatkan Bank Syariah Indonesia di peringkat puncak dengan raihan skor normalisasi 1,0000 berkat alokasi zakat "
        "terbesar, disusul Bank NTB Syariah (0,4410), Bank Mega Syariah (0,4070), Bank Aceh Syariah (0,3630), dan Bank Panin Dubai Syariah (0,2790). "
        "Adapun BTPN Syariah berada di batas terendah dengan skor 0,0000 karena ketiadaan alokasi zakat berbasis aset bersih pada periode tersebut."
    ),
    337: (
        "Tahapan penggabungan skor terstandarisasi CAR/KPMM, ROA, ROE, BOPO, FDR, dan ZPR tahun 2023 dieksekusi melalui matriks normalisasi terpadu. "
        "Pendekatan equal weighting diterapkan secara konsisten dengan memberikan bobot setara 1/6 (16,67%) bagi tiap-tiap indikator, "
        "selaras dengan metodologi analisis yang dirumuskan pada Bab III."
    ),
    344: (
        "Hasil sintesis matriks normalisasi 2023 mengonfirmasi variasi pencapaian tiap-tiap Bank Umum Syariah lintas indikator. "
        "Perkalian seluruh nilai normalisasi dengan bobot seimbang 16,67% dan penjumlahannya menghasilkan indeks komposit FPI. "
        "Angka akhir FPI mencerminkan konvergensi menyeluruh dari kinerja ketahanan permodalan, rentabilitas, efisiensi operasional, "
        "kapasitas intermediasi, serta dedikasi sosial bank."
    ),
    346: (
        "Berdasarkan nilai Falah Performance Index (FPI) 2023 yang telah diperoleh, tahapan evaluasi dilanjutkan dengan mengurutkan bank "
        "dari skor tertinggi ke terendah guna merefleksikan posisi bersaing relatif industri perbankan syariah."
    ),
    351: (
        "Pemeringkatan Falah Performance Index 2023 menempatkan Bank Syariah Indonesia di takhta tertinggi dengan FPI 0,7439, dibuntuti oleh "
        "BTPN Syariah di posisi kedua (0,7098) dan Bank NTB Syariah di peringkat ketiga (0,6451). Urutan berikutnya ditempati Bank Aceh Syariah, "
        "Bank Mega Syariah, Bank Panin Dubai Syariah, BCA Syariah, Bank Victoria Syariah, Bank BJB Syariah, serta Bank Aladin Syariah, "
        "sementara Bank Muamalat Indonesia berada di posisi terbawah dengan skor 0,2446. Konstelasi ini menegaskan heterogenitas kinerja agregat BUS."
    ),
    364: (
        "Normalisasi ROA 2024 mengukuhkan BTPN Syariah di posisi tertinggi dengan skor 1,0000 berkat pencapaian laba aset terunggul. "
        "Peringkat selanjutnya diraih Bank Syariah Indonesia (0,4690), Bank Mega Syariah (0,4070), Bank Aceh Syariah (0,4030), dan Bank NTB Syariah "
        "(0,3800), sementara Bank Aladin Syariah menempati skor dasar 0,0000 seiring masih berlangsungnya tekanan profitabilitas aset."
    ),
    366: (
        "Sebagai variabel benefit, nilai ROA yang lebih tinggi mencerminkan kapasitas produktivitas aset yang lebih kuat, sehingga bermuara "
        "pada perolehan skor normalisasi yang kian mendekati angka 1,0000 melalui persamaan matematis standar:"
    ),
    371: (
        "Hasil transformasi ROA 2024 menunjukkan bahwa BTPN Syariah sukses mempertahankan keunggulan normalisasi 1,0000, diikuti Bank Syariah "
        "Indonesia (0,4690), Bank Mega Syariah (0,4070), Bank Aceh Syariah (0,4030), dan Bank NTB Syariah (0,3800). Capaian terendah 0,0000 "
        "dialami Bank Aladin Syariah, yang menggarisbawahi variasi kapasitas BUS dalam mendulang surplus dari basis aset yang dikelola."
    ),
    373: (
        "Indikator ROE diperlakukan sebagai benefit criterion; semakin kokoh kemampuan bank menghasilkan imbal hasil atas ekuitas modal, "
        "semakin tinggi skor normalisasi yang diraih menuju batas maksimal 1,0000 dengan rumus:"
    ),
    379: (
        "Evaluasi kinerja komposit Falah Performance Index tahun 2023 menegaskan dominasi Bank Syariah Indonesia di peringkat pertama (0,7439), "
        "disusul BTPN Syariah di peringkat kedua (0,7098) dan Bank NTB Syariah di peringkat ketiga (0,6451). Entitas lainnya menduduki posisi "
        "berikutnya secara berjenjang, dengan Bank Muamalat Indonesia mencatatkan skor terendah sebesar 0,2446 sebagai cerminan kendala "
        "profitabilitas dan intermediasi pada periode tersebut."
    ),
    381: (
        "Diklasifikasikan sebagai cost criterion, indikator BOPO menuntut pengendalian rasio serendah mungkin; penghematan biaya operasional "
        "akan dihargai dengan perolehan skor normalisasi yang lebih tinggi mendekati 1,0000 melalui formulasi:"
    ),
    387: (
        "Standardisasi BOPO tahun 2024 menempatkan Bank Syariah Indonesia pada skor sempurna 1,0000 berkat kemampuan menekan beban biaya operasional "
        "ke tingkat paling efisien. Posisi berikutnya diraih BTPN Syariah (0,8618), Bank Aceh Syariah (0,8092), Bank Mega Syariah (0,8041), "
        "dan BCA Syariah (0,7543), sedangkan Bank Aladin Syariah mencatat skor 0,0000 karena beban operasionalnya masih tertinggi."
    ),
    389: (
        "Rasio FDR dievaluasi melalui target criterion guna mencegah bahaya pengetatan likuiditas maupun penumpukan dana menganggur. "
        "Koridor target dipatok pada 84%–94% dengan penalti deviasi nol, sedangkan deviasi di luar batas target dihitung jaraknya secara "
        "proporsional melalui rumus:"
    ),
    395: (
        "Pada tahun 2024, normalisasi FDR mencatatkan skor sempurna 1,0000 bagi Bank Syariah Indonesia, BTPN Syariah, Bank BJB Syariah, "
        "Bank Aladin Syariah, dan Bank NTB Syariah karena seluruhnya beroperasi di dalam koridor 84%–94%. Posisi berikutnya diisi Bank Panin Dubai "
        "Syariah (0,9690), BCA Syariah (0,9385), Bank Mega Syariah (0,8609), Bank Aceh Syariah (0,8595), dan Bank Victoria Syariah (0,7682), "
        "sedangkan Bank Muamalat Indonesia terpuruk pada skor 0,0000 akibat jarak deviasi pembiayaan yang paling lebar."
    ),
    397: (
        "Sebagai benefit criterion, rasio ZPR mencerminkan intensitas tanggung jawab sosial perbankan syariah; semakin tinggi alokasi dana "
        "zakat terhadap aset bersih, semakin optimal skor normalisasi yang diperoleh melalui persamaan:"
    ),
    402: (
        "Hasil normalisasi ZPR 2024 menempatkan Bank Syariah Indonesia di peringkat teratas dengan skor 1,0000 berkat kontribusi zakat terbesarnya. "
        "Capaian berikutnya ditorehkan Bank NTB Syariah (0,3601), Bank Mega Syariah (0,3596), Bank Aceh Syariah (0,3219), dan Bank Panin Dubai "
        "Syariah (0,1912), sedangkan BTPN Syariah menempati skor 0,0000 akibat ketiadaan pos zakat entitas pada laporan tahunan 2024."
    ),
    404: (
        "Hasil normalisasi seluruh indikator 2024 (CAR/KPMM, ROA, ROE, BOPO, FDR, dan ZPR) dihimpun ke dalam matriks terpadu sebagai basis komputasi "
        "Falah Performance Index (FPI). Bobot seragam sebesar 16,67% (equal weighting) dialokasikan pada tiap-tiap indikator guna memastikan "
        "keseimbangan evaluasi multidimensi."
    ),
    409: (
        "Kompilasi matriks normalisasi FPI 2024 menghasilkan diversifikasi capaian kinerja agregat perbankan syariah. Bank Syariah Indonesia "
        "memimpin dengan skor FPI tertinggi 0,7546, disusul BTPN Syariah (0,7254) dan Bank NTB Syariah (0,5587). Sebaliknya, Bank Muamalat "
        "Indonesia mencatatkan skor komposit terendah 0,1325, mengonfirmasi disparitas performa menyeluruh antarbank pada 2024."
    ),
    411: (
        "Sebagai kriteria benefit, penguatan rasio CAR/KPMM menjadi indikator ketahanan modal bank dalam mengantisipasi risiko sistemik, "
        "di mana rasio yang semakin kokoh ditransformasikan menjadi skor normalisasi yang kian mendekati 1,0000 melalui rumus:"
    ),
    417: (
        "Berdasarkan normalisasi CAR/KPMM 2025, BTPN Syariah memuncaki peringkat dengan skor 1,0000 berkat keunggulan rasio modal 57,74%, "
        "disusul Bank Aladin Syariah (0,7827) dan Bank Victoria Syariah/Bank Syariah Nasional (0,4830). Adapun Bank Panin Dubai Syariah "
        "mencatat nilai normalisasi 0,0000 dengan rasio terendah 18,86%, merefleksikan disparitas bantalan modal antarlembaga."
    ),
    419: (
        "Karakteristik benefit criterion pada rasio ROA memastikan bahwa bank dengan kapasitas penciptaan surplus aset yang lebih tinggi "
        "akan memperoleh apresiasi nilai normalisasi yang semakin mendekati batas optimal 1,0000 sesuai rumus:"
    ),
    434: (
        "Berdasarkan hasil pemutakhiran normalisasi ROA 2025, BTPN Syariah mempertahankan skor tertinggi 1,0000 dengan perolehan laba aset "
        "sebesar 7,15%, diikuti Bank Syariah Indonesia (0,3282) dan Bank Mega Syariah (0,3197). Posisi terendah 0,0000 ditempati Bank Muamalat "
        "Indonesia dengan raihan ROA 0,05%, yang menegaskan variasi tajam kemampuan monetisasi aset di industri perbankan syariah."
    ),
    436: (
        "Dalam kerangka benefit criterion, tingkat efektivitas manajemen dalam mendayagunakan modal pemegang saham (ROE) berbanding lurus "
        "dengan skor normalisasi yang dihasilkan, dengan formulasi perhitungan matematis:"
    ),
    442: (
        "Sesuai data normalisasi ROE 2025 yang telah disesuaikan, Bank Syariah Indonesia mengamankan skor puncak 1,0000 berkat ROE sebesar 16,85%. "
        "Posisi selanjutnya diraih Bank Victoria Syariah/Bank Syariah Nasional (0,7881), BTPN Syariah (0,7645), dan Bank Mega Syariah (0,6822), "
        "sementara Bank NTB Syariah berada di posisi terendah 0,0000 dengan capaian ROE 0,33%."
    ),
    444: (
        "BOPO diperlakukan sebagai cost criterion; efisiensi biaya operasional terhadap perolehan pendapatan menjadi acuan penentuan skor, "
        "di mana rasio yang kian tertekan akan menghasilkan nilai normalisasi yang semakin tinggi melalui rumus:"
    ),
    452: (
        "Hasil standardisasi BOPO 2025 menetapkan BTPN Syariah pada nilai normalisasi tertinggi 1,0000 berkat rasio biaya terendah 70,26%, "
        "disusul Bank Syariah Indonesia (0,9545) dan Bank Mega Syariah (0,8307). Adapun Bank NTB Syariah mencatatkan skor terendah 0,0000 "
        "karena lonjakan rasio BOPO hingga 99,03%, mengindikasikan perbedaan signifikan dalam efisiensi operasional."
    ),
    455: (
        "Sebagai target criterion, pengukuran FDR mengacu pada koridor intermediasi sehat 84%–94% guna mencegah ketidakseimbangan likuiditas. "
        "Capaian di dalam rentang target memperoleh jarak penalti nol, sedangkan nilai di luar koridor dihitung jarak deviasinya terhadap ambang terdekat:"
    ),
    463: (
        "Pada indikator FDR 2025, skor sempurna 1,0000 diraih oleh BCA Syariah, BTPN Syariah, Bank Panin Dubai Syariah, Bank Victoria Syariah/"
        "Bank Syariah Nasional, Bank BJB Syariah, Bank Aceh Syariah, dan Bank NTB Syariah karena seluruhnya berada dalam rentang target 84%–94%. "
        "Bank Syariah Indonesia mencatat skor 0,9940 akibat deviasi minor di bawah batas target minimum, Bank Mega Syariah membukukan 0,8831, "
        "Bank Aladin Syariah 0,2211, dan Bank Muamalat Indonesia memperoleh skor 0,0000 akibat penyimpangan jarak paling lebar."
    ),
    465: (
        "Mengusung kriteria benefit, rasio ZPR memotret dimensi kemaslahatan sosial; semakin tinggi porsi alokasi zakat terhadap aset bersih, "
        "semakin optimal nilai normalisasi yang diraih menuju angka 1,0000 melalui rumus:"
    ),
    473: (
        "Sesuai data laporan keuangan publikasi 2025, normalisasi ZPR menempatkan Bank Syariah Indonesia di peringkat puncak dengan skor 1,0000, "
        "diikuti Bank Mega Syariah (0,4024) dan Bank Aceh Syariah (0,2979). Sementara itu, Bank NTB Syariah membukukan 0,0630, Bank Muamalat Indonesia "
        "0,0566, Bank Aladin Syariah 0,0311, dan Bank Panin Dubai Syariah 0,0270, sedangkan BTPN Syariah mencatat skor 0,0000 karena ketiadaan "
        "alokasi zakat entitas."
    ),
    475: (
        "Analisis data 2025 diintegrasikan melalui penyusunan matriks keputusan komprehensif berdasarkan enam indikator kinerja: CAR/KPMM, "
        "ROA, ROE, BOPO, FDR, dan ZPR. Matriks ini merangkum nilai empiris aktual sebelum dilakukan normalisasi multikriteria dan perhitungan indeks FPI."
    ),
    479: (
        "Rekapitulasi matriks normalisasi FPI 2025 mengantarkan BTPN Syariah pada skor indeks tertinggi sebesar 0,7941, diikuti Bank Syariah "
        "Indonesia di posisi kedua (0,7263) dan Bank Mega Syariah di posisi ketiga (0,5618). Sebaliknya, Bank Muamalat Indonesia berada di posisi "
        "terbawah dengan raihan 0,0453, merefleksikan disparitas tajam pencapaian kinerja falah antarbank syariah pada akhir periode pengamatan."
    ),
}
