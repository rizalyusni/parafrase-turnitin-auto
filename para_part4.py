# -*- coding: utf-8 -*-
"""
Part 4: Bab V (Pembahasan Indikator Keuangan dan Sosial: CAR, ROA, ROE, BOPO, FDR, ZPR
serta Evaluasi Perkembangan Kinerja Komposit FPI).
Total: 56 paragraphs
"""

PART4_PARAPHRASES = {
    481: (
        "Sistematika pembahasan disusun selaras dengan hierarki rumusan masalah guna memastikan eksplanasi data berlangsung "
        "secara runtut dan komprehensif. Pembahasan melampaui deskripsi angka statistik semata, mencakup elaborasi dinamika kinerja "
        "Bank Umum Syariah kurun 2021–2025, dekonstruksi hasil pengukuran Falah Performance Index (FPI), pemetaan posisi kompetitif "
        "antarbank, serta kontekstualisasi temuan empiris terhadap perwujudan prinsip falah."
    ),
    484: (
        "Temuan empiris mengonfirmasi bahwa trayektori kinerja Bank Umum Syariah sepanjang 2021–2025 memperlihatkan corak yang majemuk "
        "dan dinamis. Tidak ditemukan satu bank pun yang mendominasi performa terbaik pada seluruh indikator secara serentak. "
        "Sebagian bank memiliki bantalan modal yang tebal namun diiringi profitabilitas yang tertekan, sedangkan bank lain mencetak "
        "laba dan efisiensi prima kendati kontribusi zakatnya masih minim. Realitas ini menegaskan bahwa performa perbankan syariah "
        "bersifat multidimensional sehingga evaluasinya menuntut pendekatan holistik yang menimbang seluruh parameter secara simultan."
    ),
    486: (
        "Capital Adequacy Ratio (CAR) merefleksikan daya tahan permodalan bank dalam menyangga ekspansi operasional serta mengabsorpsi "
        "potensi risiko kerugian. Ditetapkan sebagai benefit criterion dalam studi ini, rasio CAR yang semakin tinggi mencerminkan postur "
        "ketahanan solvabilitas yang kian tangguh dalam menghadapi guncangan finansial."
    ),
    487: (
        "Kapasitas permodalan Bank Umum Syariah periode 2021–2025 memperlihatkan rentang variasi yang sangat lebar. BTPN Syariah dan "
        "Bank Aladin Syariah secara konsisten mencatatkan CAR di atas rata-rata industri. Bank Aladin Syariah, misalnya, membukukan CAR "
        "sebesar 390,50% pada 2021 dan 189,28% pada 2022 pascasuntikan ekuitas, sebelum bergerak melandai menjadi 96,17% (2023), 64,96% (2024), "
        "dan 49,29% pada 2025. Kendati menyusut berkala seiring ekspansi aset, posisi permodalan tersebut tetap mencerminkan bantalan modal "
        "yang sangat memadai."
    ),
    488: (
        "Kendati demikian, tingginya rasio permodalan tidak serta-merta menggaransi tingginya perolehan skor komposit FPI. Fenomena ini "
        "terlihat nyata pada Bank Aladin Syariah; keunggulan absolut pada CAR belum mampu mengantarkan bank ke peringkat teratas FPI. "
        "Kondisi ini membuktikan bahwa kecukupan modal pasif harus ditransformasikan secara produktif ke dalam penciptaan laba, efisiensi "
        "operasional, kedalaman intermediasi, serta realisasi tanggung jawab sosial zakat demi mencapai kinerja falah yang paripurna."
    ),
    489: (
        "Secara komprehensif, fluktuasi CAR selama 2021–2025 membuktikan bahwa ketahanan modal merupakan pilar fundamental perbankan "
        "syariah yang terus bertransformasi; dalam arsitektur Falah Performance Index, skor permodalan tidak berdiri sendiri melainkan "
        "harus dikonvergensikan bersama indikator rentabilitas, efisiensi, intermediasi, dan filantropi guna menghasilkan evaluasi yang berimbang."
    ),
    491: (
        "Return on Assets (ROA) mencerminkan kepiawaian manajemen dalam mendayagunakan seluruh aset produktif guna menghasilkan laba bersih. "
        "Dalam algoritma FPI, ROA difungsikan sebagai kriteria benefit, di mana efisiensi pemanfaatan aset yang semakin tinggi akan menghasilkan "
        "skor normalisasi yang semakin mendekati nilai optimal 1,0000."
    ),
    492: (
        "Disparitas kapasitas menghasilkan laba antar-Bank Umum Syariah tampak sangat kontras sepanjang periode penelitian. BTPN Syariah "
        "secara konsisten memimpin pencapaian ROA dengan mencetak 10,72% pada 2021 dan meningkat ke 11,43% pada 2022. Meskipun terkoreksi "
        "menjadi 6,34% (2023) dan 6,33% (2024) akibat normalisasi pasar, rasionya kembali menguat ke level 7,15% pada 2025. Capaian ini "
        "menegaskan dominasi BTPN Syariah dalam memonetisasi portofolio aset di atas rata-rata bank syariah lainnya."
    ),
    493: (
        "Bank Syariah Indonesia turut memperlihatkan kinerja profitabilitas aset yang sehat dan berkesinambungan. ROA bank meningkat dari 1,61% "
        "(2021) menjadi 2,35% (2022), sedikit melandai ke 1,98% (2023), lalu memuncak ke 2,49% (2024) sebelum bertengger di level 2,38% pada 2025. "
        "Tren stabil ini mencerminkan keberhasilan integrasi pascamerger dalam mengoptimalkan skala ekonomis aset yang dikelola."
    ),
    494: (
        "Sebaliknya, Bank Muamalat Indonesia mencatatkan profitabilitas aset yang sangat marjinal di sepanjang periode observasi, dengan ROA "
        "sebesar 0,02% pada 2021, 0,09% pada 2022, 0,02% pada 2023, 0,03% pada 2024, dan 0,05% pada 2025. Keterbatasan rentabilitas ini "
        "mengindikasikan bahwa kapasitas aset produktif bank dalam menghasilkan surplus bersih masih sangat terbatas dibandingkan pesaing industrinya."
    ),
    495: (
        "Trayektori pemulihan yang mencolok ditunjukkan oleh Bank Aladin Syariah. Setelah menanggung rentetan ROA negatif sebesar -8,81% (2021), "
        "-10,85% (2022), -4,22% (2023), dan -0,90% (2024) pada masa investasi digital, bank ini sukses membalikkan kinerja menjadi positif "
        "sebesar 1,24% pada 2025. Titik balik ini menandai keberhasilan awal monetisasi model bisnis perbankan digital yang dirintis."
    ),
    496: (
        "Secara menyeluruh, sebaran ROA Bank Umum Syariah 2021–2025 merefleksikan heterogenitas efektivitas manajerial; BTPN Syariah unggul pada "
        "margin profitabilitas tinggi, Bank Syariah Indonesia menunjukkan ketahanan kinerja yang konsisten, Bank Muamalat Indonesia masih berjuang "
        "di level profitabilitas rendah, sementara Bank Aladin Syariah merealisasikan perbaikan dari zona defisit menuju profitabilitas positif pada 2025."
    ),
    498: (
        "Return on Equity (ROE) merefleksikan kapasitas entitas dalam menciptakan nilai tambah atas modal pemegang saham. Sebagaimana halnya "
        "CAR dan ROA, ROE dikategorikan sebagai kriteria benefit, di mana efisiensi pengelolaan ekuitas yang kian optimal akan menghasilkan "
        "apresiasi skor normalisasi yang lebih tinggi mendekati 1,0000."
    ),
    499: (
        "Dinamika imbal hasil modal antar-BUS memperlihatkan fluktuasi tajam. Bank Mega Syariah yang membukukan ROE impresif 28,51% pada 2021 "
        "mengalami koreksi signifikan menjadi 11,73% (2022), 9,76% (2023), dan 9,81% (2024), sebelum menguat kembali ke level 11,60% pada 2025. "
        "Perubahan ini menunjukkan adanya normalisasi margin keuntungan modal pascapandemi yang kemudian mulai pulih pada akhir periode."
    ),
    500: (
        "Bank Syariah Indonesia membukukan stabilitas pertumbuhan ROE yang sangat solid, beranjak dari 13,71% pada 2021 menjadi 16,88% pada 2022 "
        "dan bertahan di 16,84% pada 2023. Kinerja berlanjut menguat ke 17,77% pada 2024 sebelum ditutup pada level 16,85% pada 2025, mencerminkan "
        "konsistensi tinggi dalam mendistribusikan imbal hasil bagi pemegang modal."
    ),
    501: (
        "BTPN Syariah turut mencetak ROE yang sangat kuat, terutama di awal periode pengamatan dengan raihan 23,67% (2021) dan 24,21% (2022). "
        "Kendati pergeseran provisi pembiayaan menurunkan rasio menjadi 13,22% (2023) dan 12,63% (2024), bank mampu menjaga ketahanan imbal hasil "
        "ekuitasnya di level 12,96% pada 2025, tetap tergolong kompetitif di ranah industri syariah nasional."
    ),
    502: (
        "Pada kutub berbeda, Bank Aladin Syariah mengalami tekanan defisit ekuitas berturut-turut sebesar -10,10% (2021), -8,50% (2022), "
        "-7,55% (2023), dan -2,43% (2024), sebelum berhasil mencatatkan ROE positif 4,48% pada 2025. Pergeseran ini menegaskan bahwa modal disetor "
        "yang masif tidak serta-merta melahirkan return ekuitas yang memadai tanpa efektivitas alokasi aset yang menghasilkan laba bersih."
    ),
    503: (
        "Secara keseluruhan, komparasi ROE Bank Umum Syariah kurun 2021–2025 membuktikan perbedaan mendasar dalam produktivitas modal; "
        "BSI mempertahankan pertumbuhan yang stabil, BTPN Syariah menjaga imbal hasil tinggi meski terkoreksi dari puncak awal, Bank Mega Syariah "
        "mengalami normalisasi rasio, dan Bank Aladin Syariah mencatat fase pembalikan kinerja dari minus ke surplus pada 2025."
    ),
    508: (
        "Indikator BOPO difungsikan untuk memotret derajat efisiensi operasional perbankan dengan memperbandingkan beban terhadap pendapatan operasional. "
        "Berbanding terbalik dengan kriteria benefit, BOPO dioperasionalkan sebagai cost criterion, di mana rasio yang semakin rendah mencerminkan "
        "efisiensi biaya yang kian prima sehingga dihargai dengan nilai normalisasi yang semakin tinggi."
    ),
    509: (
        "Hasil pengujian empiris mengukuhkan BTPN Syariah sebagai salah satu bank paling efisien, dengan BOPO sebesar 59,97% (2021) dan 58,12% (2022). "
        "Meskipun kenaikan biaya pencadangan sempat mendongkrak rasio ke 76,24% (2023) dan 75,37% (2024), manajemen berhasil menekannya kembali ke 70,26% "
        "pada 2025. Posisi ini memastikan struktur operasional BTPN Syariah tetap berada pada kategori sangat sehat menurut standar pengawasan perbankan."
    ),
    510: (
        "Efisiensi operasional yang terjaga turut diperlihatkan Bank Syariah Indonesia, di mana rasio BOPO membaik dari 80,46% pada 2021 menjadi 71,27% "
        "pada 2022, sebelum bergerak tipis ke 75,88% pada 2023. Tren perbaikan berlanjut ke titik 69,93% pada 2024 dan ditutup pada 71,57% pada 2025, "
        "membuktikan keberhasilan sinergi operasional pascamerger dalam menekan inefisiensi beban overhead."
    ),
    511: (
        "Kondisi restriktif dialami Bank Muamalat Indonesia yang menanggung beban operasional mendekati batas penerimaan, dengan rasio BOPO "
        "sebesar 99,29% (2021), 96,62% (2022), 99,41% (2023), 99,04% (2024), dan 98,80% (2025). Tingginya rasio yang mendekati 100% ini mengindikasikan "
        "bahwa hampir seluruh pendapatan operasional terserap untuk menutup ongkos operasional, sehingga ruang pembentukan laba bersih menjadi sangat sempit."
    ),
    512: (
        "Transformasi efisiensi paling radikal ditunjukkan oleh Bank Aladin Syariah. Membuka periode dengan BOPO sebesar 428,40% (2021) dan 354,75% (2022) "
        "akibat belanja modal teknologi, bank ini secara konsisten merampingkan biaya hingga rasionya menyusut drastis menjadi 128,65% (2023), 109,29% (2024), "
        "dan akhirnya berhasil menembus koridor efisiensi 89,07% pada 2025 seiring peningkatan basis pendapatan operasional."
    ),
    513: (
        "Secara menyeluruh, dinamika BOPO Bank Umum Syariah sepanjang 2021–2025 menggarisbawahi disparitas penguasaan beban operasional; "
        "BTPN Syariah dan BSI membuktikan kepemimpinan efisiensi biaya, Bank Muamalat Indonesia terkendala struktur beban yang kaku, sementara Bank Aladin "
        "Syariah membukukan lompatan efisiensi terbesar melalui pemangkasan rasio biaya secara progresif."
    ),
    516: (
        "Financing to Deposit Ratio (FDR) mengukur efektivitas bank syariah dalam mendistribusikan dana simpanan masyarakat ke sektor pembiayaan riil. "
        "Dalam metodologi FPI, FDR diperlakukan secara khusus sebagai target criterion, di mana capaian di dalam rentang optimal 84%–94% dianugerahi "
        "skor sempurna 1,0000, sementara simpangan ke bawah (under-financing) maupun ke atas (over-financing) dikenakan penalti penurunan skor secara proporsional."
    ),
    517: (
        "Bank NTB Syariah konsisten menjaga fungsi intermediasinya pada batas ideal, membukukan FDR sebesar 90,96% (2021), 89,21% (2022), 94,35% (2023), "
        "90,22% (2024), dan 86,90% (2025). Meskipun realisasi 2023 sedikit melampaui batas atas koridor, secara umum manajemen likuiditas bank "
        "berhasil menjaga keseimbangan penyaluran pembiayaan selaras dengan kapasitas penghimpunan dana pihak ketiga."
    ),
    518: (
        "BTPN Syariah mencatat rasio FDR yang relatif ekspansif pada fase awal dengan torehan 95,17% pada 2021 dan 95,68% pada 2022, yang menempatkannya "
        "sedikit di atas batas atas target. Memasuki 2023, bank mengalibrasi ekspansi pembiayaannya hingga rasionya bergerak ke 93,78%, berlanjut ke 86,76% "
        "pada 2024, dan mendarat di 84,79% pada 2025, sehingga seluruhnya beroperasi tepat di dalam zona target optimal penelitian."
    ),
    519: (
        "Kalibrasi portofolio pembiayaan BTPN Syariah tersebut menegaskan transisi strategi likuiditas yang pruden; keberhasilan menurunkan FDR "
        "dari kisaran 95% menuju koridor 84%–94% sepanjang 2023–2025 membuktikan komitmen menjaga kesinambungan intermediasi tanpa mengorbankan likuiditas."
    ),
    520: (
        "Bank Syariah Indonesia memperlihatkan penguatan kapasitas intermediasi secara terencana, di mana rasio FDR meningkat progresif dari 73,39% "
        "pada 2021 menuju puncak 84,97% pada 2024. Kendati melandai tipis ke level 83,74% pada 2025 (hanya terpaut 0,26% di bawah ambang batas minimum), "
        "pencapaian ini mencerminkan optimalisasi pemanfaatan dana simpanan publik untuk pembiayaan produktif secara berkelanjutan."
    ),
    521: (
        "Pada posisi berseberangan, Bank Muamalat Indonesia mencatatkan rasio intermediasi yang persisten di bawah ambang optimal, yakni 38,33% (2021), "
        "40,63% (2022), 47,14% (2023), 40,08% (2024), dan 40,36% (2025). Jarak deviasi yang lebar dari koridor sasaran 84%–94% ini mengindikasikan "
        "terjadinya under-financing yang cukup dalam, di mana porsi penyaluran pembiayaan tertahan jauh di bawah kapasitas dana simpanan yang dihimpun."
    ),
    522: (
        "Volatilitas ekstrem dialami Bank Aladin Syariah, yang mencatatkan lonjakan FDR hingga 173,27% pada 2022 pascapeluncuran pembiayaan baru, "
        "sebelum terkoreksi ke 95,31% (2023) dan 87,72% (2024). Pada 2025, rasionya merosot ke level 50,01%. Sebagaimana diungkapkan dalam laporan "
        "tahunan resminya, penurunan rasio ke 50,01% pada 2025 mencerminkan kebijakan likuiditas superkonservatif akibat lonjakan penghimpunan dana "
        "yang dialokasikan ke instrumen pasar uang berisiko rendah."
    ),
    523: (
        "Secara komprehensif, dinamika FDR Bank Umum Syariah 2021–2025 menegaskan bahwa fungsi intermediasi menuntut keseimbangan dinamis; Bank NTB "
        "Syariah dan BTPN Syariah sukses mempertahankan rasio di zona optimal, BSI terus berekspansi mendekati batas ideal, sedangkan Bank Muamalat "
        "dan Bank Aladin menghadapi kendala deviasi yang cukup lebar dari rentang target 84%–94% yang ditetapkan."
    ),
    525: (
        "Zakat Performance Ratio (ZPR) memotret kontribusi kebajikan institusional bank syariah melalui perbandingan alokasi zakat terhadap basis "
        "aset bersih yang dikelola. Berperan sebagai benefit criterion, rasio zakat yang lebih besar mencerminkan komitmen sosial yang kian luhur. "
        "Analisis diarahkan pada konsistensi kebijakan filantropi dan posisi komparatif antarbank guna menangkap dimensi kemaslahatan sosial secara objektif."
    ),
    526: (
        "Bank Syariah Indonesia secara konsisten mengukuhkan keunggulan absolut pada dimensi sosial ZPR. Pada 2023 dan 2025, BSI membukukan nilai "
        "normalisasi sempurna 1,0000 berkat porsi alokasi zakat terbesar di industri. Dominasi ini membuktikan bahwa pertumbuhan skala bisnis "
        "pada BSI diimbangi secara nyata oleh penguatan komitmen filantropi Islam dalam wujud penyaluran zakat korporasi."
    ),
    527: (
        "Kontribusi filantropi yang kokoh turut ditunjukkan Bank Mega Syariah dengan perolehan skor normalisasi ZPR 0,4071 (2023) dan 0,4024 (2025), "
        "menempatkannya sebagai salah satu kontributor sosial paling signifikan. Kinerja positif juga dibukukan Bank Aceh Syariah melalui skor "
        "normalisasi zakat sebesar 0,3633 (2023) dan 0,2979 (2025) selaras dengan mandat qanun perbankan syariah di daerah."
    ),
    528: (
        "Bank NTB Syariah sempat mencatatkan capaian menonjol pada 2023 dengan skor normalisasi ZPR sebesar 0,4410 di atas Bank Mega Syariah, "
        "kendati pada 2025 rasionya termoderasi ke level 0,0630. Fluktuasi ini mengindikasikan bahwa alokasi zakat institusional sangat sensitif "
        "terhadap dinamika penyesuaian laba bersih tahunan dan perubahan kebijakan dividen sosial bank."
    ),
    529: (
        "Di sisi lain, mayoritas bank syariah seperti BCA Syariah, Bank Victoria Syariah/Bank Syariah Nasional, Bank BJB Syariah, dan Bank Aladin "
        "Syariah membukukan rasio ZPR yang relatif minim. BTPN Syariah bahkan secara konsisten mencatatkan skor normalisasi 0,0000 sepanjang periode "
        "observasi karena tidak mengalokasikan zakat entitas dari aset bersih dalam pos laporan keuangan yang diteliti."
    ),
    530: (
        "Divergensi ZPR membuktikan bahwa performa sosial perbankan syariah tidak berjalan linier dengan kesuksesan finansial. Lembaga dengan "
        "profitabilitas dan kecukupan modal superior tidak secara otomatis mengalokasikan zakat dalam jumlah proporsional. Fenomena ini menggarisbawahi "
        "urgensi integrasi rasio ZPR ke dalam Falah Performance Index guna menyingkap dimensi normatif yang luput dari kalkulasi finansial murni."
    ),
    531: (
        "Secara agregat, perkembangan ZPR 2021–2025 memperlihatkan polarisasi komitmen sosial di perbankan syariah; BSI, Bank Mega Syariah, dan Bank "
        "Aceh Syariah konsisten mengalokasikan zakat secara signifikan, sedangkan entitas lainnya masih belum menempatkan zakat korporasi sebagai "
        "prioritas utama. Temuan ini menegaskan peran krusial ZPR dalam menyempurnakan evaluasi kinerja perbankan berbasis falah."
    ),
    533: (
        "Sintesis atas dinamika CAR, ROA, ROE, BOPO, FDR, dan ZPR sepanjang 2021–2025 menunjukkan bahwa kinerja Bank Umum Syariah di Indonesia "
        "berlangsung sangat heterogen dan dinamis. Tidak satu pun bank menguasai seluruh indikator secara serentak, di mana setiap institusi "
        "memiliki diferensiasi profil antara ketahanan modal, profitabilitas, efisiensi operasional, intermediasi, dan kepedulian sosial."
    ),
    534: (
        "Pada ranah permodalan, perolehan CAR yang tinggi terbukti tidak otomatis diiringi kemampuan menghasilkan laba yang sepadan. Fenomena bank "
        "dengan rasio CAR tebal namun memiliki ROA atau ROE rendah menegaskan bahwa modal yang melimpah harus dikelola secara produktif dan "
        "terarah agar dapat menggerakkan roda profitabilitas dan nilai tambah perusahaan."
    ),
    535: (
        "Ditinjau dari profitabilitas, ROA dan ROE memetakan disparitas performa yang tajam. BTPN Syariah unggul dalam margin keuntungan aset, "
        "BSI mempertahankan stabilitas imbal hasil yang tangguh, sementara sejumlah bank sempat terperangkap dalam zona rugi sebelum pulih pada 2025. "
        "Realitas ini menempatkan efisiensi monetisasi aset dan modal sebagai pilar penentu kesehatan finansial jangka panjang."
    ),
    536: (
        "Aspek efisiensi operasional (BOPO) mengonfirmasi ketimpangan kapasitas pengendalian biaya antarbank. Sebagian bank mampu menekan rasio biaya "
        "secara disiplin di bawah ambang batas industri, sedangkan sebagian lainnya dibebani ongkos operasional yang tinggi, meski ada yang berhasil "
        "melakukan pembalikan efisiensi secara drastis melalui transformasi digital."
    ),
    537: (
        "Pada dimensi intermediasi, pencapaian FDR yang ideal menuntut keseimbangan antara ekspansi pembiayaan dan manajemen likuiditas. Keberhasilan "
        "beroperasi di koridor target 84%–94% membuktikan kapabilitas bank dalam menjalankan mandat ekonomi riil tanpa terpapar risiko kekeringan "
        "likuiditas maupun penumpukan dana menganggur."
    ),
    538: (
        "Adapun dimensi sosial (ZPR) menyingkap asimetri antara keberhasilan komersial dan alokasi kebajikan. Lemahnya korelasi otomatis antara "
        "laba tinggi dan besaran zakat institusional mempertegas bahwa tanggung jawab sosial syariah memerlukan kebijakan kelembagaan yang terikat "
        "secara eksplisit pada nilai-nilai falah."
    ),
    539: (
        "Secara komprehensif, evaluasi parsial keenam rasio menegaskan bahwa kesehatan bank syariah tidak dapat diukur secara parsial. Kinerja prima "
        "mensyaratkan integrasi seimbang antara modal, laba, efisiensi, pembiayaan, dan filantropi, yang seluruhnya disatukan secara komposit "
        "melalui Falah Performance Index (FPI) periode 2021–2025."
    ),
    544: (
        "Dalam menginterpretasikan dinamika FPI, perlu ditekankan bahwa prosedur normalisasi dieksekusi secara independen pada setiap tahun observasi. "
        "Oleh sebab itu, skor FPI merefleksikan posisi kompetitif relatif suatu bank di antara sesama BUS pada tahun yang bersangkutan, bukan "
        "pertumbuhan absolut antarwaktu mengingat batas nilai ekstrem normalisasi bergerak dinamis setiap tahunnya."
    ),
    545: (
        "Hasil komputasi empiris membuktikan bahwa Bank Syariah Indonesia dan BTPN Syariah mendominasi posisi terdepan kinerja komposit FPI. "
        "BSI mengukir skor FPI sebesar 0,6853 (2021), 0,6464 (2022), 0,7439 (2023), 0,7545 (2024), dan 0,7263 (2025). Di sisi lain, BTPN Syariah "
        "mencatat kenaikan berkesinambungan dari 0,6683 (2021) menuju 0,6961 (2022), 0,7098 (2023), 0,7254 (2024), hingga mencapai puncak 0,7941 "
        "pada 2025. Capaian ini mencerminkan keandalan kedua bank dalam menjaga konsistensi kinerja lintas indikator."
    ),
    546: (
        "Bank Mega Syariah turut mengukuhkan posisi sebagai institusi dengan kinerja komposit yang solid, mencatatkan skor FPI 0,6425 (2021), "
        "0,6433 (2022), 0,5830 (2023), 0,5426 (2024), dan 0,5618 (2025). Meski termoderasi dibanding dua tahun pertama, kekuatan komposit bank "
        "tetap stabil di papan atas perbankan syariah nasional."
    ),
    547: (
        "Volatilitas kinerja komposit lebih tampak pada Bank Aceh Syariah, BCA Syariah, dan Bank Victoria Syariah/Bank Syariah Nasional. "
        "Bank Aceh Syariah membukukan FPI 0,5249 (2021), 0,5284 (2022), melonjak ke 0,6010 (2023), sebelum melandai ke 0,5377 (2024) dan 0,4675 (2025). "
        "BCA Syariah mencatat pergerakan 0,5088 (2021), 0,4833 (2022), 0,5270 (2023), 0,4481 (2024), dan 0,4099 (2025). Adapun Bank Victoria Syariah/"
        "Bank Syariah Nasional menorehkan 0,4643 (2021), 0,5613 (2022), 0,4635 (2023), 0,4316 (2024), dan kembali naik ke 0,5088 (2025), "
        "merefleksikan dinamika restrukturisasi internal yang berlangsung."
    ),
    548: (
        "Bank NTB Syariah sempat mencatatkan penguatan FPI dari 0,5526 (2021) dan 0,5428 (2022) menjadi 0,6451 (2023) serta 0,5587 (2024), "
        "sebelum terkoreksi tajam ke 0,1890 pada 2025 akibat pelemahan skor normalisasi ROA, ROE, dan pembengkakan BOPO, kendati rasio FDR tetap aman "
        "dalam target. Realitas ini menegaskan bahwa keunggulan pada satu variabel tidak mampu mengimbangi kejatuhan skor indikator fundamental lainnya."
    ),
    549: (
        "Fluktuasi lebar juga dialami Bank Panin Dubai Syariah dengan skor FPI 0,2647 (2021), melesat ke 0,5146 (2022) dan 0,5679 (2023), "
        "namun kembali terkontraksi ke 0,3641 (2024) dan 0,1833 pada 2025. Pola ini mengindikasikan bahwa perbaikan kinerja pascarestrukturisasi "
        "masih menghadapi tantangan konsistensi jangka panjang."
    ),
    550: (
        "Penurunan skor FPI secara gradual dibukukan Bank BJB Syariah dari 0,5084 (2021) menjadi 0,4929 (2022), 0,4415 (2023), 0,3267 (2024), "
        "dan berakhir di 0,2477 pada 2025. Pelemahan ini berakar dari penurunan daya saing pada indikator profitabilitas, efisiensi biaya operasional, "
        "serta minimalnya kontribusi zakat institusional."
    ),
    551: (
        "Bank Aladin Syariah menunjukkan lintasan adaptasi khas perbankan digital, dengan FPI 0,2266 (2021), 0,1674 (2022), menguat ke 0,3338 (2023) "
        "dan 0,3384 (2024), serta bertengger di 0,3000 pada 2025. Meskipun modalnya sangat perkasa, nilai komposit bank sempat tertahan oleh tingginya "
        "beban operasional awal dan defisit laba sebelum fase pemulihan tercapai."
    ),
    552: (
        "Sementara itu, Bank Muamalat Indonesia memperlihatkan penurunan skor komposit yang berkesinambungan, dari 0,4575 (2021) menjadi 0,3888 (2022), "
        "0,2446 (2023), 0,1325 (2024), hingga menyentuh 0,0453 pada 2025. Tertekannya skor akhir ini dipicu oleh perolehan ROA minimal, beban BOPO "
        "yang sangat tinggi, serta deviasi intermediasi FDR yang menghasilkan skor normalisasi 0,0000 pada tahun terakhir."
    ),
    553: (
        "Secara holistik, evaluasi FPI 2021–2025 menyimpulkan bahwa keunggulan perbankan syariah ditentukan oleh orkestrasi seimbang di seluruh lini kinerja. "
        "BSI dan BTPN Syariah membuktikan ketangguhan sinergi antarindikator, sejumlah bank berada di kelompok menengah dengan fluktuasi moderat, "
        "sedangkan sebagian lainnya menghadapi tantangan ketahanan bisnis. Temuan ini memvalidasi FPI sebagai instrumen evaluasi komprehensif yang "
        "menyatukan dimensi finansial, intermediasi riil, dan kemaslahatan sosial."
    ),
}
