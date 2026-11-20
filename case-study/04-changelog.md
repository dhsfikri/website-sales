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
- Page ujian **Industri** (`industri.html`) dibina: pilih 1 daripada 8 industri → headline, 3 masalah biasa, demo chat (cara biasa vs skrip Sir) dan pakej Ebook 2026 + Framework industri RM47 berubah ikut industri. Link `?i=hartanah` dll untuk iklan ikut industri. Pixel: PilihIndustri, ViewContent RM47/RM37, IndustriKlik. Belum diterbitkan.
- Poster retarget v2 (gaya UI-mockup ala iklan Reply.la, brandkit hijau/krim/emas): R3 Industri (RM47), R4 P&L 3% vs 6% (RM37), R5 Intip + PREVIEW10. Fail: `ads/creative/retarget-r3/r4/r5.png`, sumber `retarget-v2.html`. Sir: offer kekal sama, cuma vibes page berubah; fokus retarget.
- **Sales page baru LIVE (18 Nov):** gaya Reply.la (terang, mockup telefon, kad terapung) + brandkit, headline "Team masih tak closed di Wassap? Skrip & formula dah siap." Offer kekal RM37. Dipasang ke form 21578 (iklan), 22025 (sd-th) dan 22024 (sd-wa). Teks live disahkan sama 100% dengan `bcl/ebook-reply-style.html`. Form retarget 21730 tidak diubah. Ukur: InitiateCheckout / LP view, sasaran >3% (asas ~1%).
- 19 Nov: Sir sambung WhatsApp **+60 14-771 1169** ke Page Sir Dharma (untuk iklan Click-to-WhatsApp). Nombor butang sales page / bio kekal 016-767 7759 buat masa ini. Menunggu Sir cipta ad set WhatsApp (Sales → Messaging apps → WhatsApp, RM10/hari); Claude pasang iklan (OFF).
- 19 Nov: Kempen WhatsApp dicipta sebagai **draf** melalui API (mod draf): kempen 120252809186400048 (Engagement, CBO RM10/hari), ad set 120252809186890048 (WhatsApp, Conversations, MY, cadangan umur 28–50, A+ Audience, exclude 180 Hari Pembeli), iklan WA1 R3 Industri (120252809188880048) dan WA2 R4 P&L (120252809189600048), CTA WhatsApp Message. Sekatan sama: "Advertiser is missing" (pematuhan Malaysia: perlu pilih verified advertiser/beneficiary di Ads Manager). regional_regulated_categories=MALAYSIA_UNIVERSAL ditambah, tapi ID identiti verified tidak boleh diset melalui API. Sir perlu pilih advertiser di bahagian Compliance, kemudian Publish.
- 19 Nov: Sir pilih advertiser di Ads Manager; semua ralat draf hilang. WhatsApp +60 14-771 1169 disahkan dalam promoted_object (page_whatsapp_number_id 1879194930095098). **ID identiti verified advertiser: 2037511550243904** (universal_beneficiary & universal_payer, regional_regulated_categories MALAYSIA_UNIVERSAL + VOLUNTARY_VERIFICATION). Ad set baru boleh dicipta sepenuhnya melalui API dengan nilai ini. Draf menunggu kebenaran Sir untuk publish.
- **Peraturan kerja iklan (19 Nov, dari Sir):** Claude cipta semua kempen/ad set/iklan sebagai **draf** sahaja, hantar ringkasan untuk Sir review, dan publish hanya selepas Sir beri izin jelas. Nota: advertiser pada draf WhatsApp terisi sendiri bila draf dibuka di Ads Manager (Sir tidak tekan apa-apa).
- **Peraturan sekatan draf (19 Nov):** bila draf kena sekatan, Claude ingatkan Sir; jika Sir lambat, Claude semak semula draf sendiri (sekatan mungkin dah hilang) sebelum minta izin publish.
- Kempen WhatsApp ditukar jadi **retarget Deep Dive** (arah Sir: "dah beli banyak ebook tapi team masih struggle, tiada guideline, WhatsApp untuk set Deep Dive percuma"). Poster baru: `ads/creative/deepdive-d1.png`, `deepdive-d2.png`.
- 19 Nov: Draf ditukar: kempen "19Nov2026 | Deep Dive | WhatsApp Retarget" (RM5/hari), ad set "Retarget Deep Dive | Pembeli + Pelawat + Engaged" (custom audience sahaja: 180 Hari Pembeli, 14 Hari Pelawat, 30 Hari Website, IG Engaged, Engaged With Page; A+A off sebab custom-audience-only), iklan DD1 & DD2 (poster Deep Dive, CTA WhatsApp, tulis "DEEP DIVE"). Tiada ralat. Start time API tidak boleh dijadual (ralat 1487057), jadi Claude akan ingatkan Sir untuk publish pada **21 Nov 9 pagi** (peringatan dijadual).
- 19 Nov: Poster Deep Dive dikemas kini dengan **gambar sebenar** (Sir tunjuk + sesi coaching HQ klien), ikut arahan Sir. Creative baru: DD1 29881948414762944, DD2 1665668155257914 (CTA WhatsApp). Draf tiada ralat. Nota teknikal: edit image_url terus pada draf ad beri ralat "Missing media"; cara betul = ads_create_creative (link_url api.whatsapp.com/send + CTA WHATSAPP_MESSAGE) kemudian set creative_id.
- 19 Nov: Ralat Meta #1815589 ("Link title and description of CTA are deprecated", 12 placement tak jalan) pada DD1/DD2. Punca: creative dari ads_create_creative tambah call_to_action.value.link_title. Dibetulkan: creative inline dengan image_hash sedia ada (DD1 c7dd56ed62f6098c1541193abab90d46, DD2 ddbd242fd8069f1981370fbea7a705ff) dan CTA WHATSAPP_MESSAGE value {app_destination: WHATSAPP} sahaja. Tiada ralat. **Pelajaran:** untuk iklan WhatsApp, guna creative inline + image_hash, jangan ads_create_creative.
- 19 Nov: Draf Deep Dive ditukar ke poster **D5** (foto konsultasi) dan **D6** (Sir + sesi coaching), render 2x (2160×2700). image_hash D5 5b435456abc487414b926e62c2cbec01, D6 5e45d5dc094612a5bf1ba31ea3f6c81b. Tiada ralat. Garis panduan poster baru: `10-garis-panduan-poster.md` (premium, realistic, 4K, cinematic).
- 19 Nov: **Webhook ujian** dipasang pada form WhatsApp sd-wa (22024) sahaja → trigger Murpati (URL disimpan di BCL, tidak dalam repo). Event: form-submit, payment-success, payment-failed. Untuk diuji Sir (isi borang, batal bayar), kemudian ditutup/dilaras ikut fungsi trigger.
- 19 Nov: Sir buat test bayar sebenar di sd-wa (RM11, 14:23). URL webhook sd-wa ditukar ke trigger Murpati "Payment Receive" yang baru (URL di BCL sahaja). Claude hantar data ujian (payment-success, nombor Sir) ke trigger → Murpati balas `captured`. Langkah seterusnya: Sir petakan medan (payer_telephone_number) + mesej + syarat status=success di Murpati; kemudian pasang ke form lain.
- 19 Nov: Trigger Murpati kedua "Follow Up Tak Bayar" ditambah pada webhook sd-wa (2 URL kini). Data ujian payment-failed (status cancelled, nombor Sir) dihantar ke trigger ini.
- 19 Nov (review): **Pause live** G3 (120252758037790048), CV4 (120252778529820048), CV5 (120252778530200048), R2 (120252752442390048). **Draf baru** (tiada ralat): H1 Ejen Hartanah RM47 (120252812352350048) dalam ad set Minggu 1 → form iklan; RP1 retarget premium "Masih Fikir? Intip" (120252812353090048) dalam ad set Retarget → form preview + PREVIEW10. Poster: `ads/creative/h1-4k.jpg`, `rp1-4k.jpg`. Menunggu "publish" Sir.
- 19 Nov: **H1 Hartanah dan RP1 Retarget premium di-publish** (status ACTIVE, effective IN_PROCESS: dalam semakan Meta). Pause G3/CV4/CV5/R2 disahkan. Draf Deep Dive WhatsApp tidak disentuh (jadual 21 Nov).
- 19 Nov (arahan Sir: "Pasang setting. Iklan deep dive pun boleh jalan."): **Setting standard dipasang dan di-publish** pada 4 ad set: Minggu 1 (120252739281570048), Carousel Owner Servis (120252778480440048), Retarget (120252751545220048), Deep Dive (120252809186890048). Bahasa Malay + English (Meta simpan sebagai locales 6, 24, 41). Placement FB feed/story/reels + IG feed/story/reels sahaja (disahkan dalam read-back). Audience, umur, exclude dan budget tidak diubah.
- 19 Nov: **Kempen Deep Dive WhatsApp di-publish ACTIVE** (kempen 120252809186400048, RM5/hari; iklan D5 120252809188880048 dan D6 120252809189600048), status IN_PROCESS (semakan Meta). Peringatan 21 Nov ditukar jadi semakan report sahaja.
- 20 Nov (arahan Sir: "Pause semua yg tak okay. Budget kene bawah RM50"): **Pause** kempen Story Preview Traffic (120252762325780048, RM11/hari; ~250 LPV, 0 IC sejak 16 Nov), iklan **B** Formula (120252739511730048; ~RM29, 0 purchase) dan **CV3** Hitam (120252778529480048; 0 klik semalam, 0 purchase). **Bajet**: Minggu 1 RM30 → RM20, Carousel RM25 → RM15. Retarget RM5 dan Deep Dive RM5 kekal. Jumlah bajet harian **RM76 → RM45**. Iklan yang kekal: E3, H1 (Minggu 1); CV1, CV2 (Carousel); R1, RP1 (Retarget); D5, D6 (Deep Dive). Semua disahkan live.
- 20 Nov: Sir risau burst budget (Meta boleh belanja sehingga +75% sehari). Keputusan Sir: **kekal RM45/hari**, dan Sir sendiri set **account spending limit** di Billing sebagai brek kecemasan (cadangan RM350/minggu). Tiada tool API untuk set had ini.
- 20 Nov: Sir jumpa iklan **H1** keluar dengan banner bcl.my. Punca (silap Claude): image_url di luar link_data, Meta guna gambar preview link BCL. **RP1** kena sama. Poster diupload semula: H1 hash 833999eefec2e35dbf6df99e661febfb, RP1 hash 1e349e8cbdf2cc60e6cda6df434da25b; kedua-dua iklan dikemas kini dalam draf (tiada ralat), menunggu "publish" Sir. Iklan lain (E3, CV1, CV2, R1, D5, D6) disemak: semua ada image_hash poster sendiri. Peraturan semak gambar ditambah di `10-garis-panduan-poster.md`.
- 20 Nov: Sir "publish". H1 dan RP1 di-publish dengan poster betul. Read-back live: H1 creative 2062296984473537 (hash 833999ee... = h1-4k.jpg), RP1 creative 2663900010710236 (hash 1e349e8c... = rp1-4k.jpg). Status IN_PROCESS (semakan Meta). Skill projek baru `.claude/skills/iklan-meta-sirdharma/SKILL.md` simpan semua peraturan iklan (draf, bajet bawah RM50, setting standard, semak gambar).
- 20 Nov: Plan konsep iklan baru "Skrip siap copy-paste" (owner / team sales / ejen, destinasi WhatsApp) ditulis di `11-konsep-iklan-skrip-copy-paste.md`. Belum ada poster atau draf.
