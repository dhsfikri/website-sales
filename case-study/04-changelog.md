# 04 · Changelog

Setiap perubahan pada funnel, iklan dan setting. Paling baru di atas.

## 17 Nov 2026

- Plan baru carousel value untuk owner bisnes servis (lihat `05-plan-value-carousel.md`). 3 carousel × 5 slide siap dalam 3 tema warna: hijau (asal), terang/krim, hitam-kuning (`ads/creative/carousel/`, `carousel/terang/`, `carousel/hitam/`).
- Kempen baru dicipta (PAUSED): "17Nov2026 | Ebook 2026 | Sales | Carousel Value Owner Servis" (120252778455590048), RM25 sehari CBO.
- Sir cipta ad set carousel (120252778480440048). Claude kemaskan: cadangan umur 28–50, nama ikut konvensyen; placeholder "New Sales ad" dipause.
- 5 iklan carousel dipasang (PAUSED, tunggu kelulusan Sir):
  - CV1 · C1 Problem · Hijau (ad 120252778528080048, creative 1084916441240799)
  - CV2 · C1 Problem · Terang (ad 120252778528530048, creative 1691837795905897)
  - CV3 · C1 Problem · Hitam (ad 120252778529480048, creative 2410595589711211)
  - CV4 · C2 Pain · Hijau (ad 120252778529820048, creative 1532602612028407)
  - CV5 · C3 Pleasure · Hijau (ad 120252778530200048, creative 1183174600704330)
  - Ujian warna: CV1 vs CV2 vs CV3 (angle sama). Ujian angle: CV1 vs CV4 vs CV5 (warna sama).
- F3 dipause (1 klik sahaja).
- Kempen carousel, ad set dan 5 iklan carousel di-ON atas kelulusan Sir. Perubahan bajet Minggu 1 (RM30 → RM12) ditolak oleh Sir, jadi Minggu 1 kekal RM30.
- Exclusion "180 Hari Pembeli (Purchase SD2026)" ditambah pada ad set carousel (ad set di-ON semula selepas auto-pause). Ujian audience Advantage+ vs manual targeting (cadangan nota Zaeem) ditangguh ke minggu depan selepas kreatif menang dikenal pasti.
- Ad set melalui API masih ditolak ("Advertiser is missing"). Tool duplicate ad set juga belum tersedia untuk akaun ini. Sir perlu cipta ad set dalam Ads Manager.

- Form saluran organik dengan link pendek (salinan penuh: item, harga, pixel SD2026 + CAPI, redirect terima kasih, featured image):
  - WhatsApp: /form/sd-wa (ID 22024, "Kedai Ebook Sir Dharma - WhatsApp", salinan form utama)
  - Threads: /form/sd-th (ID 22025, "Kedai Ebook Sir Dharma - Threads", salinan form Threads; /form/ebook-sirdharma-threads kekal aktif)
  - Jualan dikenal pasti ikut nama form dalam rekod transaksi BCL.
  - Link pendek oleh Sir: https://klik.vip/ebookclosing-wa (→ /form/sd-wa) dan https://klik.vip/ebookclosing-th (→ /form/sd-th) untuk posting WhatsApp dan Threads.

## 16 Nov 2026

- Conversions API (CAPI) di-ON oleh Sir untuk form utama (21578) dan Threads (21780); Claude ON untuk form retarget (21730) dengan token yang sama. Ketiga-tiga form: pixel 255927347311677 + CAPI ON. Token disimpan dalam BCL sahaja, tidak direkod dalam repo. Event server belum masuk semasa semakan (perlu ada pelawat/pembeli baru dahulu).
- Semakan tracking Purchase: pixel SD2026 TERIMA Purchase jualan 15 Nov dari sweetcactusenterprise.bcl.my (Events Manager: 1 Purchase pada 15 Nov waktu Pasifik). Halaman terima kasih (main) hanya PageView, tiada kiraan berganda. Masalahnya atribusi: Meta tidak padankan pembeli itu dengan klik/tontonan iklan dalam tetingkap 7 hari klik / 1 hari tonton, jadi iklan tunjuk 0 Purchase. Conversions API (CAPI) di form BCL masih OFF; perlu token dari Events Manager untuk hidupkan (hantar emel/telefon pembeli secara hash, padanan lebih tinggi).
- Atas maklum balas Sir (CTA kurang kuat): versi 3 dengan CTA kuat. Butang poster "KLIK SEKARANG · RM37", butang iklan Buy Now (dulu Shop Now), headline jadi ayat CTA, dan hujung primary text ada ajakan + FOMO pesaing. Tiada voucher untuk trafik sejuk (PREVIEW10 kekal untuk retarget sahaja). E3/F3/G3 di-ON, E2/F2/G2 di-PAUSE (baru jalan beberapa jam).
  - E3 · "KLIK SEKARANG: 5 SKRIP JAWAB HARGA · -44%" (ad 120252758037000048, creative 2011686783278791)
  - F3 · "JANGAN TANGGUH. KLIK SEKARANG, JIMAT 44%" (ad 120252758037440048, creative 1762814918119898)
  - G3 · "KLIK SEKARANG SEBELUM PESAING DAPAT DULU" (ad 120252758037790048, creative 1069605316096869)
- Atas maklum balas Sir (headline kurang punch): poster E/F/G dibuat semula dengan headline HURUF BESAR + angka (5 skrip, 3 hari, 2X, +0%) dan pelekat "JIMAT 44%". Headline iklan Meta juga huruf besar dengan angka. Iklan baru (PAUSED, tunggu kelulusan Sir):
  - E2 · "5 SKRIP JAWAB "BERAPA HARGA?" · JIMAT 44%" (ad 120252755840410048, creative 1126304950261190)
  - F2 · "3 HARI BLUETICK? 1 TEKNIK BUAT PROSPEK LAJU BAYAR" (ad 120252755840740048, creative 4438525923125417)
  - G2 · "BAJET ADS 2X, CLOSING +0%? · JIMAT 44%" (ad 120252755841810048, creative 1927007641602234)
  - E2, F2, G2 di-ON atas kelulusan Sir (16 Nov). Iklan aktif dalam kempen Minggu 1: B, E2, F2, G2.
  - Iklan E/F/G versi pertama dinamakan "(LAMA, JANGAN ON)" dan kekal PAUSED (tidak pernah jalan).
- Iklan A, C, D di-PAUSE atas arahan Sir (B kekal; B ambil ~62% belanja).
- 3 iklan baru dengan angle lain dipasang dalam ad set Minggu 1 (status PAUSED, menunggu kelulusan Sir untuk ON):
  - E · Skrip "Nak harga je" (ad 120252755812850048, creative 1654105010094324)
  - F · Penangguhan "Tanya husband dulu" (ad 120252755813510048, creative 2148865862416624)
  - G · Owner "Iklan bukan tongkat sakti" (ad 120252755813580048, creative 1580980460497497)
- Poster dibina dari `ads/creative/iklan-2.html` dan dimuat naik melalui URL raw GitHub (upload fail terus perlukan app Ads MCP).

## 15 Nov 2026

- Kempen retarget dicipta (PAUSED): "15Nov2026 | Ebook 2026 | Retarget | Preview10" (ID 120252750115110048), Sales, RM5 sehari (CBO), lowest cost.
- Audience baru: "14 Hari Pelawat Sales Page Ebook 2026" (120252750113240048, URL mengandungi ebook-sirdharma) dan "180 Hari Pembeli (Purchase SD2026)" (120252750113400048, untuk exclude).
- Creative retarget R1 dicipta (3290555938000251): poster iklan B, link ke /form/preview-ebook-2026, CTA Shop Now, Advantage+ creative OFF.
- Ad set retarget melalui API ditolak lagi ("Advertiser is missing"), walaupun akaun Sir dah verified. Sir perlu cipta ad set dalam Ads Manager.
- Punca ralat API "Advertiser is missing": ad set yang target Malaysia perlu medan `regional_regulated_categories = MALAYSIA_UNIVERSAL` + `regional_regulation_identities` (universal_beneficiary, universal_payer). Medan ini tidak ambil default akaun, dan tool Meta Ads MCP belum sokong medan ini. Penyelesaian: Sir cipta ad set (pilih beneficiary/payer) dalam Ads Manager; Claude set audience dan pasang iklan melalui API.
- Audience ad set retarget ditambah: IG Engaged (~1,300) dan Engaged With Page (~1,000), supaya audience cukup besar untuk delivery (pelawat 14 hari baru ~44 orang). Ad set dinamakan semula "MY | Pelawat 14H + IG Engaged + Page Engaged | Exclude Pembeli 180H | Advantage+ Placement | Purchase (Pixel SD2026)".
- Sir cipta ad set retarget dalam Ads Manager (120252751545220048): audience pelawat 14 hari sahaja, exclude pembeli 180 hari. Iklan R1 Formula Preview dan R2 Foto Sir Preview dipasang; kempen retarget ACTIVE.
- Form retarget (21730) dan coupon PREVIEW10 (4343) di-ON.

## 14 Nov 2026

- Disediakan untuk retarget (minggu 2): form BCL "Preview Ebook 2026 (Retarget)" (ID 21730, /form/preview-ebook-2026), 17 item sama seperti form utama (semua dengan Protected Content), status OFF. Coupon terpakai untuk jumlah troli, jadi semua ebook & bundle dapat 10%. Page fokus isi kandungan sebenar 105 m/s (dibaca terus dari PDF), 4 petikan sebenar, siapa sesuai/tak sesuai, FAQ. Coupon PREVIEW10 (10%, ID 4343; asalnya INTIP10, ditukar kerana "intip" janggal) dicipta dalam keadaan tidak aktif dan dihadkan pada form ini sahaja.
- Semakan pixel: 1 bayaran berjaya (test) direkod sebagai 2 Purchase, dan BCL turut hantar InitiateCheckout. Kesimpulan: BCL hantar Purchase sendiri. Purchase dibuang dari halaman terima kasih (kekal PageView) untuk elak kiraan berganda.
- Folder Drive testimoni disusun ke 7 folder (testimoni, poster, media, gambar kelas, potret, video, cover).
- Konvensyen nama: kempen mesti ada tarikh mula; ad set mesti sebut setting. Kempen → "14Nov2026 | Ebook 2026 | Sales | Minggu 1". Ad set → "MY | 25-65 | Advantage+ Audience | Advantage+ Placement | Purchase (Pixel SD2026)".
- Iklan C dan D lulus review dan ACTIVE.
- Kempen "Ebook 2026 - Sales - Minggu 1" di-ON. Iklan C dan D di-ON. A dan B kekal PAUSED, menunggu Sir ON dalam Ads Manager.
- Iklan D (poster foto, struktur inspirasi iklan pesaing) ditambah.
- 4 iklan (A, B, C, D) dipasang dalam ad set Sir; Advantage+ creative enhancements OFF; placeholder "New Sales ad" di-PAUSE.
- Ad set dibuat oleh Sir dalam Ads Manager (API ditolak: perlu verified advertiser untuk Malaysia).
- 15 Protected Content dicipta oleh Sir; Claude set Show on Receipt ON, pautkan ke 17 item (bundle dapat 3 ebook), betulkan tajuk "10 Framework Handle Rejection Like Pro".
- Didapati emel resit BCL tidak mengandungi link ebook. Protected Content dipilih sebagai cara penghantaran.
- Test purchase RM10 (LINK-592587): bayaran, halaman terima kasih, group WhatsApp dan emel resit berfungsi.
- Bundle ditukar nama: Teras → Skrip Siap Guna; Learning Lab → Asas Closing.
- Cover ebook dipasang pada 14 item; cover gabungan dibuat untuk 2 bundle.
- Penerangan item ditulis semula; butang kuantiti diaktifkan (sebelum ini semua item masuk sekali, RM499).
- Meta Pixel ditambah pada halaman terima kasih (PageView + Purchase RM37).
- GitHub Pages dihidupkan untuk halaman terima kasih.

## 13 Nov 2026

- Sales page dipindahkan ke dalam BCL (Custom HTML), bonus Group WhatsApp Pembeli ditambah.
- Borang BCL dicipta dengan 17 item; Meta Pixel diaktifkan pada borang.

## 17 Nov: bio klik.vip/link/3944 direka semula
- Versi 1 (block klik.vip, hijau/kuning) dan versi 2 (editorial, Custom HTML) dalam `bio/`. Ebook jadi tawaran utama; cadang form `sd-bio` + `klik.vip/ebookclosing-bio` untuk tracking bio.
- Grill bio selesai: ebook jadi CTA utama (link ebookclosing-th, tiada form baru), pixel + event klik dalam bio, kad Murpati referral. Tunggu link T5, Framework, Murpati.
- Bio live di klik.vip/sirdharma diuji (klik.vip dibenarkan dalam environment website-sales). Punca rosak: class card/btn bertembung Bootstrap klik.vip + margin .row. Semua class ditukar ke sd-*, tambah CSS paksa layout (bg krim, buang pink, lebar penuh).
- Bio: kad Framework diganti dengan tawaran sesi percuma bersama team via WhatsApp (untuk owner yang dah beli tapi team belum konsisten). Semua link lengkap.
- Bio live disemak: klik.vip potong Custom HTML sekitar 16,200 aksara, jadi skrip pixel klik terpotong (error JS). Tambah bio/build.py untuk padatkan kod (15,596 aksara), diuji tanpa error, pixel OK.
- Bio live disemak (versi padat): sama 100% dengan kod, tiada error, semua gambar & animasi OK, klik Ebook = ViewContent RM37, butang lain = BioKlik. klik.vip sendiri dah load pixel 255927347311677, jadi PageView dibuang dari kod kita (elak kiraan berganda). Kod kini 15,164 aksara.

## 18 Nov 2026
- Sales page (form 21578): hero baru. Headline P&L rugi ("Gaji RM3,600. Iklan RM3,000. Jualan RM4,500. Bulan ni anda rugi RM2,100."), foto kecil Sir + nama, 2 kad P&L (closing 3% rugi RM2,100 vs 6% untung RM2,400), nota "contoh kiraan". Foto besar kekal di bawah butang. Page lain (retarget, WA, Threads) tidak diubah.
- Ukuran: nilai selepas 100 LP view atau 3 hari. Menang jika InitiateCheckout/LP view > 3% (asas ~1%: 2/199).
- Page ujian **Panduan** diterbitkan: https://dhsfikri.github.io/website-sales/panduan.html (konsep "panduan dulu, jual kemudian" ala Reply.la: telefon chat demo, kalkulator P&L, 4 langkah tab, testimoni, harga 3 pilihan, penutup 2 pilihan). Butang beli → form 21578 dengan `?src=panduan`. Pixel: PageView, ViewContent (klik Ebook), PanduanKlik, KiraPL. Fail ditambah ke `main` dan `claude/focused-clarke-fnraay` dengan izin Sir.
- Semakan: sales page BCL live masih headline lama (hero P&L belum ditampal).
