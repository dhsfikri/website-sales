# 04 · Changelog

Setiap perubahan pada funnel, iklan dan setting. Paling baru di atas.

## 15 Nov 2026

- Kempen retarget dicipta (PAUSED): "15Nov2026 | Ebook 2026 | Retarget | Preview10" (ID 120252750115110048), Sales, RM5 sehari (CBO), lowest cost.
- Audience baru: "14 Hari Pelawat Sales Page Ebook 2026" (120252750113240048, URL mengandungi ebook-sirdharma) dan "180 Hari Pembeli (Purchase SD2026)" (120252750113400048, untuk exclude).
- Creative retarget R1 dicipta (3290555938000251): poster iklan B, link ke /form/preview-ebook-2026, CTA Shop Now, Advantage+ creative OFF.
- Ad set retarget melalui API ditolak lagi ("Advertiser is missing"), walaupun akaun Sir dah verified. Sir perlu cipta ad set dalam Ads Manager.
- Punca ralat API "Advertiser is missing": ad set yang target Malaysia perlu medan `regional_regulated_categories = MALAYSIA_UNIVERSAL` + `regional_regulation_identities` (universal_beneficiary, universal_payer). Medan ini tidak ambil default akaun, dan tool Meta Ads MCP belum sokong medan ini. Penyelesaian: Sir cipta ad set (pilih beneficiary/payer) dalam Ads Manager; Claude set audience dan pasang iklan melalui API.
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
