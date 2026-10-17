# -*- coding: utf-8 -*-
"""
Part 1: Bab IV (Objek Penelitian, Penyajian Data CAR, ROA, ROE, BOPO, FDR, ZPR)
dan Bab V (Penyusunan Matriks Keputusan & Prinsip Normalisasi).
Total: 32 paragraphs
"""

PART1_PARAPHRASES = {
    3: (
        "Sebagai entitas perbankan syariah yang menyediakan layanan lalu lintas pembayaran, "
        "Bank Umum Syariah (BUS) tidak semata mengemban fungsi komersial melalui penghimpunan "
        "dan penyaluran dana pihak ketiga. Bank syariah secara inheren memikul mandat sosial, "
        "seperti menghimpun serta mendistribusikan dana zakat, infak, sedekah, hibah, maupun instrumen "
        "kebajikan lainnya berdasarkan regulasi yang berlaku. Di samping itu, lembaga ini berwenang "
        "mengelola wakaf uang guna disalurkan kepada pengelola wakaf (nazhir) selaras amanah wakif. "
        "Karakteristik ganda ini menegaskan bahwa orientasi BUS mencakup integrasi fungsional antara "
        "intermediasi keuangan dan tanggung jawab sosial."
    ),
    4: (
        "Penelitian ini menetapkan Bank Umum Syariah di Indonesia yang memenuhi kriteria purposive sampling "
        "pada Bab III sebagai objek kajian. Observasi dilakukan sepanjang rentang waktu 2021–2025 berbasis data sekunder "
        "yang bersumber dari laporan tahunan maupun laporan keuangan publikasi resmi masing-masing bank. "
        "Guna menjamin keabsahan, konsistensi, serta ketertelusuran data dalam evaluasi kinerja, verifikasi silang "
        "dilakukan melalui kanal resmi Otoritas Jasa Keuangan (OJK), khususnya publikasi kelembagaan perbankan syariah "
        "yang memuat status legal entitas yang diteliti."
    ),
    8: (
        "Perubahan kelembagaan material berlangsung pada PT Bank Victoria Syariah sepanjang tahun 2025. "
        "Aksi korporasi diawali penuntasan akuisisi oleh BTN per 5 Juni 2025, yang dilanjutkan dengan transformasi entitas "
        "menjadi PT Bank Syariah Nasional (BSN) serta peluncuran identitas barunya pada 2 Oktober 2025. Selanjutnya, integrasi "
        "seluruh hak dan kewajiban BTN Syariah ke dalam BSN terealisasi secara yuridis per 22 Desember 2025. Dinamika restrukturisasi "
        "ini menuntut perlakuan analitis khusus terhadap data BSN tahun 2025 agar komparabilitasnya terhadap data historis "
        "Bank Victoria Syariah periode 2021–2024 tetap terjaga secara objektif."
    ),
    9: (
        "Pengukuran performa perbankan syariah dalam studi ini mengoperasionalkan enam indikator sebagaimana dirumuskan pada Bab III. "
        "Dimensi finansial diartikulasikan melalui lima rasio pokok, yaitu Capital Adequacy Ratio (CAR) atau Kewajiban Penyediaan Modal "
        "Minimum (KPMM), Return on Assets (ROA), Return on Equity (ROE), Biaya Operasional terhadap Pendapatan Operasional (BOPO), "
        "dan Financing to Deposit Ratio (FDR). Adapun dimensi sosial diukur melalui Zakat Performance Ratio (ZPR). Konstruksi "
        "multidimensi ini selaras dengan landasan teoretis pengukuran kinerja berbasis falah, yang memandang bahwa penilaian bank syariah "
        "harus melampaui tolok ukur moneter konvensional demi menginternalisasi aspek normatif syariah. Kendati demikian, keenam rasio "
        "tersebut merupakan desain operasional spesifik dalam penelitian ini, sehingga tidak dimaksudkan mereplikasi instrumen model falah "
        "terdahulu secara identik."
    ),
    16: (
        "Sebagaimana disajikan pada Tabel 4.2, tingkat permodalan (CAR/KPMM) Bank Umum Syariah selama rentang 2021–2025 "
        "memperlihatkan dinamika yang bervariasi antarlembaga maupun antartahun. Posisi permodalan Bank Syariah Indonesia "
        "bergerak sangat stabil pada rentang 20,29%–22,09%. Sebaliknya, Bank Muamalat Indonesia mencatatkan lonjakan rasio modal "
        "dari 23,76% pada 2021 menjadi 32,70% pada 2022, sebelum mengalami penyusutan berkala ke level 26,37% pada 2025. "
        "Tren penurunan juga dialami BCA Syariah, yaitu dari 41,40% (2021) menuju 27,70% (2025). Di sisi lain, BTPN Syariah secara konsisten "
        "mengukuhkan rasio CAR/KPMM yang sangat kokoh pada kisaran 51,60%–58,27%."
    ),
    17: (
        "Stabilitas kecukupan modal turut ditunjukkan oleh Bank Mega Syariah dengan pergerakan rasio di rentang 25,59% hingga 30,86%. "
        "Sementara itu, Bank Panin Dubai Syariah mengalami penyusutan rasio dari 25,81% pada 2021 menjadi 18,86% pada 2025. "
        "Fluktuasi modal yang sangat tajam dialami Bank Victoria Syariah/Bank Syariah Nasional, dengan lonjakan ekspansi CAR/KPMM "
        "hingga menyentuh 149,68% pada 2022, sebelum akhirnya terkoreksi ke posisi 37,64% pada 2025. Adapun bank pembangunan daerah syariah, "
        "seperti Bank BJB Syariah, Bank Aceh Syariah, dan Bank NTB Syariah, cenderung menjaga ketahanan modal pada koridor yang moderat "
        "meski tetap diwarnai dinamika tahunan."
    ),
    18: (
        "Pola permodalan yang sangat ekspansif tercatat pada Bank Aladin Syariah, yang membuka periode pengamatan dengan CAR/KPMM "
        "sebesar 390,50% pada 2021 seiring injeksi modal awal, sebelum termoderasi secara gradual menjadi 49,29% pada 2025. "
        "Secara komprehensif, data empiris ini mengindikasikan bahwa kapasitas permodalan Bank Umum Syariah sepanjang 2021–2025 "
        "memiliki corak manajemen ketahanan modal yang heterogen, baik yang berorientasi pada stabilitas portofolio maupun yang dipengaruhi "
        "oleh restrukturisasi korporasi."
    ),
    23: (
        "Merujuk pada Tabel V, profil profitabilitas aset (ROA) Bank Umum Syariah periode 2021–2025 mencerminkan disparitas capaian "
        "yang signifikan. Bank Syariah Indonesia berhasil membukukan kenaikan ROA secara berkesinambungan dari 1,61% pada 2021 menjadi 2,49% "
        "pada 2024, sebelum mengalami penyesuaian minor ke level 2,38% pada 2025. Berbeda halnya dengan Bank Muamalat Indonesia, yang perolehan "
        "ROA-nya relatif terbatas dan berfluktuasi tipis di koridor 0,02%–0,09%. Sementara itu, BCA Syariah mencatat perbaikan efisiensi laba "
        "aset dari 1,10% pada 2021 ke puncaknya 1,60% pada 2024, lalu terkoreksi ke 1,50% pada 2025."
    ),
    24: (
        "BTPN Syariah secara konsisten mencetak keunggulan profitabilitas aset di atas rata-rata industri syariah. ROA bank ini naik dari 10,72% "
        "(2021) menjadi 11,43% (2022), meski kemudian terkoreksi menjadi 6,34% (2023) serta 6,33% (2024), dan kembali menguat ke level 7,15% pada 2025. "
        "Pada Bank Mega Syariah, rasio ROA tertekan dari 4,08% (2021) menuju 1,96% (2023), sebelum pulih ke angka 2,32% pada 2025. Adapun Bank Panin "
        "Dubai Syariah memperlihatkan fase pemulihan yang nyata; sempat membukukan kinerja minus -6,72% pada 2021, bank ini berhasil berbalik "
        "mencetak laba dengan ROA 1,79% pada 2022, kendati kembali melandai ke 0,11% pada penutupan 2025."
    ),
    25: (
        "Kinerja Bank Victoria Syariah/Bank Syariah Nasional bergerak naik dari 0,71% (2021) menjadi 1,47% (2025), meskipun sempat terkontraksi "
        "ke level 0,45% pada 2022. Sebaliknya, Bank BJB Syariah menunjukkan tren pelemahan bertahap, yakni dari 0,96% (2021) menjadi 0,46% (2025). "
        "Bank Aceh Syariah mampu mempertahankan kinerja profitabilitas yang solid pada kisaran 1,59%–2,05%. Transformasi penting terjadi pada "
        "Bank Aladin Syariah, yang berhasil mengakhiri rentetan kerugian operasional periode 2021–2024 (-8,81% pada 2021 hingga -0,90% pada 2024) "
        "dengan membukukan ROA positif 1,24% pada 2025. Sementara itu, Bank NTB Syariah sempat mencatatkan lonjakan perolehan laba hingga 2,07% "
        "pada 2023, sebelum akhirnya mengalami penurunan tajam menjadi 0,11% pada 2025."
    ),
    26: (
        "Secara menyeluruh, fluktuasi ROA pada Bank Umum Syariah sepanjang 2021–2025 merefleksikan dinamika produktivitas aset yang tidak seragam. "
        "Disparitas ini mencakup entitas dengan pertumbuhan stabil, entitas yang menghadapi volatilitas pasar, hingga bank yang berada dalam "
        "tahap pemulihan dari tekanan keuangan menuju profitabilitas positif. Fakta ini menegaskan adanya perbedaan kapasitas manajerial dan "
        "skala bisnis dalam mengonversi portofolio aset menjadi pendapatan operasional bersih."
    ),
    32: (
        "Berdasarkan sajian data pada Tabel 4.4, tingkat pengembalian ekuitas (ROE) Bank Umum Syariah selama 2021–2025 menunjukkan keragaman "
        "yang lebar antarbank. Bank Syariah Indonesia memperlihatkan penguatan imbal hasil modal yang konsisten, beranjak dari 13,71% pada 2021 "
        "hingga menyentuh 17,77% pada 2024, sebelum melandai tipis ke 16,85% pada 2025. Pada Bank Muamalat Indonesia, imbal hasil ekuitas bertahan "
        "pada tingkat yang sangat rendah, bergerak fluktuatif di rentang 0,20%–0,56%. Di sisi lain, BCA Syariah memperlihatkan pertumbuhan nilai "
        "ekuitas yang sehat dan stabil, dengan peningkatan bertahap dari 3,20% pada 2021 hingga mencapai 6,70% pada 2025."
    ),
    33: (
        "BTPN Syariah mempertahankan kinerja imbal hasil pemegang saham yang kuat, dengan torehan ROE 23,67% (2021) dan 24,21% (2022), "
        "meskipun normalisasi pembiayaan menyebabkan rasionya terkoreksi ke 13,22% (2023) dan 12,96% (2025). Bank Mega Syariah yang sempat "
        "membukukan ROE tinggi sebesar 28,48% pada 2021 mengalami penurunan tajam menjadi 9,76% pada 2023, sebelum perlahan naik ke posisi 11,60% "
        "pada 2025. Tekanan modal paling berat dialami Bank Panin Dubai Syariah pada 2021 dengan defisit ROE mencapai -31,76%, yang kemudian "
        "berbalik positif menjadi 11,51% pada 2022 melalui langkah penyehatan, sebelum termoderasi ke level 0,68% pada 2025."
    ),
    34: (
        "Fluktuasi ROE Bank Victoria Syariah/Bank Syariah Nasional bergerak dinamis dari 1,79% (2021) ke 0,95% (2023), kemudian melonjak ke 5,38% "
        "pada 2025 seiring konsolidasi kelembagaan. Bank BJB Syariah sempat mencatat lonjakan imbal hasil ekuitas hingga 8,68% pada 2022, kendati "
        "selanjutnya melandai berkala menjadi 4,09% pada 2025. Pada Bank Aceh Syariah, rasio ROE terkoreksi dari 16,88% (2021) menuju 10,76% (2025). "
        "Perkembangan positif diperlihatkan Bank Aladin Syariah yang berhasil melepaskan diri dari zona imbal hasil negatif periode 2021–2024 "
        "dan mencetak ROE positif 4,48% pada 2025. Sebaliknya, Bank NTB Syariah yang sempat mencatatkan ROE 13,58% pada 2023 harus menghadapi penurunan "
        "hingga 0,33% pada 2025."
    ),
    35: (
        "Gambaran umum pergerakan ROE Bank Umum Syariah selama kurun waktu penelitian memperlihatkan divergensi efisiensi pengelolaan modal. "
        "Heterogenitas pencapaian ini menegaskan bahwa efektivitas manajemen bank dalam mendayagunakan ekuitas pemegang saham untuk menghasilkan "
        "nilai tambah sangat dipengaruhi oleh strategi intermediasi, struktur pendanaan, dan fase ekspansi masing-masing entitas."
    ),
    41: (
        "Berdasarkan paparan Tabel VII, rasio efisiensi operasional (BOPO) Bank Umum Syariah sepanjang 2021–2025 mencerminkan disparitas struktur biaya "
        "yang kontras. Bank Syariah Indonesia menunjukkan perbaikan efisiensi yang solid, ditandai penurunan rasio BOPO dari 80,46% pada 2021 menjadi "
        "69,93% pada 2024, sebelum sedikit meningkat menjadi 71,57% pada 2025. Sebaliknya, Bank Muamalat Indonesia dibayangi beban operasional yang tinggi, "
        "dengan rasio yang bertahan pada level ketat antara 96,62%–99,41%. Adapun BCA Syariah berhasil mengendalikan rasio bebannya dari 84,80% (2021) "
        "menjadi 78,60% (2023), kendati kembali bergerak ke 80,60% pada 2025."
    ),
    42: (
        "BTPN Syariah mempertahankan posisi sebagai salah satu bank paling efisien, mencatatkan BOPO 59,97% (2021) dan 58,12% (2022), "
        "meski pergeseran beban risiko sempat menaikkan rasionya ke 76,24% (2023) sebelum melandai ke 70,26% pada 2025. Bank Mega Syariah mencatat "
        "kenaikan rasio biaya dari 64,64% (2021) ke 77,64% (2024), disusul perbaikan menjadi 75,13% pada 2025. Perubahan paling ekstrem terlihat pada "
        "Bank Panin Dubai Syariah, di mana beban operasional melonjak hingga 202,74% pada 2021, sebelum ditekan tajam ke 76,99% pada 2022 dan perlahan "
        "naik kembali menjadi 97,80% pada 2025."
    ),
    43: (
        "Pada Bank Victoria Syariah/Bank Syariah Nasional, dinamika BOPO terpantau fluktuatif di level 91,35% (2021) dan 94,41% (2022), "
        "sebelum membaik signifikan ke 75,11% pada 2025 pascatransformasi. Bank BJB Syariah sempat menurunkan rasio bebannya menjadi 84,90% pada 2022, "
        "namun kembali mengalami pembengkakan biaya hingga 94,12% pada 2025. Sementara itu, Bank Aceh Syariah mempertahankan kinerja efisiensi yang "
        "stabil sepanjang 2021–2024, sebelum rasionya meningkat ke posisi 81,63% pada 2025."
    ),
    44: (
        "Struktur biaya Bank Aladin Syariah menunjukkan karakteristik khas bank digital pada fase rintisan; rasio BOPO tercatat sangat tinggi "
        "sebesar 428,40% (2021) dan 354,75% (2022) akibat belanja infrastruktur teknologi, sebelum keberhasilan monetisasi operasional memangkas rasio ini "
        "secara drastis menjadi 89,07% pada 2025. Adapun Bank NTB Syariah yang semula beroperasi stabil pada koridor BOPO 80%–83% (2021–2024) mengalami "
        "lonjakan beban operasional hingga menyentuh 99,03% pada 2025."
    ),
    45: (
        "Kecenderungan rasio BOPO pada Bank Umum Syariah selama periode pengamatan mencerminkan spektrum efisiensi operasional yang beragam. "
        "Sebagian bank syariah berhasil menekan biaya operasional melalui konsolidasi dan optimalisasi digital, sedangkan sebagian lainnya masih menghadapi "
        "tekanan beban overhead yang tinggi terhadap pendapatan yang dihasilkan."
    ),
    51: (
        "Sesuai data pada Tabel 4.6, rasio intermediasi (FDR) Bank Umum Syariah sepanjang 2021–2025 memperlihatkan keragaman ekspansi pembiayaan "
        "terhadap dana pihak ketiga. Bank Syariah Indonesia menunjukkan peningkatan intermediasi yang konsisten dari 73,39% pada 2021 ke puncaknya 84,97% "
        "pada 2024, sebelum sedikit menyesuaikan ke 83,74% pada 2025. Sebaliknya, Bank Muamalat Indonesia mencatatkan kapasitas penyaluran dana yang "
        "relatif rendah dan tertahan di kisaran 38,33%–47,14%. Sementara itu, BCA Syariah konsisten menjaga fungsi intermediasinya dalam batas yang sangat "
        "pruden pada koridor 79,90%–85,50%."
    ),
    52: (
        "BTPN Syariah mencatatkan rasio FDR yang relatif tinggi pada awal periode, yakni 95,17% (2021) dan 95,68% (2022), sebelum secara bertahap "
        "terkonvergensi ke level 84,79% pada 2025. Bank Mega Syariah mengalami pertumbuhan intermediasi dari 62,84% pada 2021 dan 54,63% pada 2022 "
        "menjadi 78,90% pada 2025. Adapun Bank Panin Dubai Syariah yang semula mencatat ekspansi pembiayaan agresif dengan FDR 107,56% pada 2021 "
        "secara bertahap mengendalikan penyaluran dananya hingga mencapai 92,57% pada 2025."
    ),
    53: (
        "Dinamika penyaluran pembiayaan Bank Victoria Syariah/Bank Syariah Nasional bergerak sangat dinamis, dari posisi 65,26% pada 2021, "
        "melonjak signifikan hingga 107,85% pada 2023, lalu termoderasi ke level 93,43% pada 2025. Bank BJB Syariah memperlihatkan tren peningkatan "
        "penyaluran dana dari 81,55% (2021) menjadi 93,65% (2024), sebelum ditutup pada level 92,35% (2025). Tren penguatan intermediasi juga dibukukan "
        "Bank Aceh Syariah yang meningkat stabil dari 68,06% pada 2021 menjadi 89,19% pada 2025."
    ),
    54: (
        "Perubahan rasio intermediasi paling dramatis dicatat oleh Bank Aladin Syariah. Pada 2021 rasio FDR tercatat 0,00% karena ketiadaan portofolio "
        "pembiayaan, kemudian melonjak pesat menjadi 173,27% pada 2022 seiring peluncuran pembiayaan baru, sebelum akhirnya terkoreksi ke level 50,01% "
        "pada 2025. Di sisi lain, Bank NTB Syariah konsisten mempertahankan pengelolaan likuiditas intermediasi yang stabil dalam koridor 86,90%–94,35% "
        "sepanjang periode observasi."
    ),
    55: (
        "Secara agregat, pola FDR Bank Umum Syariah periode 2021–2025 mengindikasikan disparitas strategi manajemen likuiditas dan agresivitas "
        "penyaluran pembiayaan. Sebagian bank syariah beroperasi sangat dekat dengan batas target intermediasi regulator, sementara sebagian lainnya "
        "menghadapi kendala under-financing maupun kelebihan ekspansi pembiayaan melampaui himpunan dana simpanan."
    ),
    66: (
        "Sebagaimana terangkum pada Tabel IX, kontribusi sosial melalui Zakat Performance Ratio (ZPR) pada Bank Umum Syariah periode 2021–2025 "
        "menunjukkan variasi yang sangat kontras. Bank Syariah Indonesia menunjukkan komitmen penyaluran zakat yang berkelanjutan dengan rasio yang naik "
        "dari 0,5102% pada 2021 menjadi 0,6085% pada 2025. Pada Bank Muamalat Indonesia, rasio ZPR terkoreksi dari 0,2056% (2021) ke 0,0889% (2024), "
        "sebelum sedikit membaik menjadi 0,0981% pada 2025. Di sisi lain, BCA Syariah membukukan rasio ZPR yang sangat minim dan cenderung menyusut, "
        "yaitu dari 0,0029% pada 2021 menjadi 0,0013% pada 2025."
    ),
    67: (
        "BTPN Syariah mencatatkan rasio ZPR sebesar 0,0000% sepanjang lima tahun pengamatan karena tidak mengalokasikan zakat entitas secara langsung "
        "dari aset bersih perusahaan dalam pos terkait. Fluktuasi cukup lebar diperlihatkan Bank Mega Syariah, yang meningkat dari 0,2269% (2021) "
        "menjadi 0,7890% (2022), sebelum menurun kembali ke level 0,2854% pada 2025. Pola volatil juga dialami Bank Panin Dubai Syariah dengan rasio "
        "0,0073% (2021), nihil 0,0000% (2022), melonjak ke 0,2282% (2023), dan melandai ke 0,0756% pada 2025."
    ),
    68: (
        "Bank Victoria Syariah/Bank Syariah Nasional membukukan rasio ZPR yang sangat rendah pada kisaran 0,0001%–0,0071%. Bank BJB Syariah juga "
        "menunjukkan tren penurunan kontribusi zakat dari 0,0441% pada 2021 menjadi 0,0009% pada 2025. Sebaliknya, Bank Aceh Syariah memperlihatkan "
        "lompatan rasio zakat yang impresif, berawal dari 0,0545% pada 2023 menjadi 0,3959% pada 2024 dan mencapai 0,4131% pada 2025 seiring penguatan "
        "kebijakan filantropi daerah."
    ),
    69: (
        "Peningkatan bertahap juga dicapai Bank Aladin Syariah dari 0,0000% (2021) menjadi 0,0200% (2025). Sementara itu, Bank NTB Syariah mencatatkan "
        "penguatan dimensi sosial yang sangat signifikan dalam dua tahun terakhir, beranjak dari 0,0597% pada 2023 melonjak menjadi 0,4045% pada 2024 "
        "dan 0,4399% pada 2025, mencerminkan komitmen kelembagaan yang kian menguat terhadap alokasi zakat berbasis aset bersih."
    ),
    70: (
        "Secara umum, tren ZPR Bank Umum Syariah sepanjang 2021–2025 merefleksikan disparitas kebijakan internal dalam pengalokasian dana kebajikan. "
        "Perbedaan proporsi penyaluran zakat terhadap aset bersih ini memperlihatkan bahwa internalisasi fungsi sosial perbankan syariah belum merata, "
        "di mana sebagian bank memprioritaskan alokasi zakat institusional secara signifikan, sementara sebagian lainnya masih mengandalkan "
        "skema filantropi non-perusahaan."
    ),
    97: (
        "Standardisasi nilai antarindikator melalui normalisasi mutlak diperlukan mengingat setiap variabel memiliki satuan, rentang skala, "
        "dan orientasi pengukuran yang berlainan. Dalam penelitian ini, prosedur normalisasi dieksekusi secara terpisah pada masing-masing "
        "tahun pengamatan guna menjamin keadilan evaluasi komparatif antar-Bank Umum Syariah dalam ruang waktu yang setara. Metode min-max "
        "normalization diterapkan pada indikator berkategori benefit dan cost, sedangkan rasio FDR dikelola menggunakan pendekatan target criterion."
    ),
    98: (
        "Indikator CAR/KPMM, ROA, ROE, dan ZPR ditetapkan sebagai benefit criteria, yang berarti semakin besar nilai capaian maka semakin tinggi "
        "skor normalisasinya mendekati angka 1,0000. Sebaliknya, BOPO dikategorikan sebagai cost criterion, di mana nilai rasio yang semakin rendah "
        "mencerminkan efisiensi yang lebih unggul sehingga menghasilkan nilai normalisasi yang lebih tinggi. Adapun FDR diperlakukan khusus sebagai "
        "target criterion, dengan evaluasi performa yang didasarkan pada tingkat kedekatan deviasi terhadap koridor batas intermediasi ideal "
        "yang telah ditetapkan dalam metodologi penelitian."
    ),
}
