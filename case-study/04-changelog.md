# 04 · Changelog

Setiap perubahan pada funnel, iklan dan setting. Paling baru di atas.

## 27 Nov 2026

- BOTTOM digabung ke MIDDLE (lihat `ads/skrip-iklan-v3-bundle.md`). Kempen "25Nov2026 | BOTTOM | Retarget Video + Pelawat | WhatsApp" di-PAUSE.
- Ad set baru dalam MIDDLE: "MIDDLE · Retarget Pelawat SP 14H + Mula Bayar 14H · Exclude Pembeli · Purchase" (ID 120252938858730048), ke form retarget. Dibina dalam draf, dipublish PAUSED, kemudian ON (atas arahan Sir).
- 7 iklan V3 (copy 3 pakej RM37/RM67/RM99, CTA Get Offer) dibina dalam draf, dipublish PAUSED, kemudian ON. 6 lulus review segera; T4 V3 masih dalam review semasa log ditulis.
- Iklan V2 T6, T5 dan K1 lama di-PAUSE (diganti V3). V2 T4 dibiar ACTIVE sehingga T4 V3 lulus review.
- Bajet MIDDLE dinaikkan RM25 → RM35 sehari (RM25 MIDDLE + RM10 bekas BOTTOM). Jumlah belanja harian akaun kekal RM45.
- Satu draf lama "MID K1 · Kenalkan Diri Sir + PREVIEW10" dalam Ads Manager tidak disentuh.

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
