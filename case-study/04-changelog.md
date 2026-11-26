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
- 20 Nov (19:50): **Pause CV2** Terang (120252778528530048) atas arahan Sir (RM14.81 hari ini, 0 IC). Carousel kini tinggal CV1 sahaja (RM15/hari). Nota: H1 Hartanah berkongsi ad set Minggu 1 (MY 25–65, Advantage+ Audience, tiada interest hartanah); hanya copy dan gambar yang berbeza.
- 20 Nov (20:00): Sir tanya kenapa webhook tak jalan untuk transaksi gagal Pakej Hartanah (form iklan 21578). Punca: webhook Murpati hanya dipasang pada form sd-wa (22024); form lain belum. **Dipasang** 2 trigger Murpati (Payment Receive + Follow Up Tak Bayar, URL di BCL sahaja) pada form **21578** (ebook-sirdharma), **22025** (sd-th) dan **21730** (preview-ebook-2026), event form-submit + payment-success + payment-failed. Transaksi gagal 17:56 tidak akan dihantar semula; perlu follow up manual.
- 20 Nov: Cadangan struktur funnel iklan (Top/Middle/Bottom/Selepas Beli) ditulis di `12-struktur-funnel-iklan.md`. Belum ada perubahan pada iklan.
- 20 Nov: Sir: "Saya taknak hartanah di awal, itu perlu di retargetting." Plan funnel dikemas kini: H1 pindah dari Top ke Bottom.
- 20 Nov: Sir tetapkan TOP = tips percuma, video pendek, gambar realistik sedia ada, ke sales page untuk data pixel (impression murah). Plan funnel dikemas kini (TOP = Traffic LPV); shot list 3 video di `13-video-tips-top.md`, tunggu kelulusan.
- 20 Nov: 3 video motion graphic tips TOP (T1 harga, T2 bluetick, T3 owner 3 nombor), 15 saat, 9:16 + 4:5, muzik disintesis. Fail: `ads/video-tips/out/t{1,2,3}_{916,45}.mp4`, sumber `ads/video-tips/tips.html`. Sementara sebelum video Sir sendiri. Menunggu semakan Sir.
- 20 Nov (malam, arahan Sir: "Saya okay.. terus adjust semua iklan yg berjalan skrg"): **Struktur funnel baru dilancarkan** (jumlah RM45/hari):
  - **TOP** (baru) kempen 120252834701930048 "20Nov2026 | TOP | Tips Percuma | Traffic LPV", RM15/hari. Ad set 120252834707930048: MY 25–55 A+A, exclude Pembeli 180H + Pelawat SP 14H, Malay+English, feed/story/reels, optimum LPV. Iklan video T1/T2/T3 (120252834728400048, 120252834729560048, 120252834730620048), 9:16 untuk story/reels + 4:5 untuk feed, butang Learn More → ebook-sirdharma.
  - **MIDDLE** (baru) kempen 120252834702000048 "20Nov2026 | MIDDLE | Skrip Copy-Paste | WhatsApp", RM15/hari. Ad set 120252834708350048: IG Engaged + Page Engaged + Website 30H, exclude Pembeli 180H, Pelawat SP 14H, Mula Bayar 14H. Iklan M1 (video T1) 120252834734310048 dan M2 (video T3) 120252834736000048, CTA WhatsApp, tulis "SKRIP" (1 skrip percuma).
  - **BOTTOM** = kempen Retarget 120252750115110048 (RM5 → RM10), ad set 120252751545220048 audience ditukar ke Pelawat SP 14H + **Mula Bayar 14H** (audience baru 120252834701800048), exclude Pembeli. Iklan: RP1, R1, **H1** (baru 120252834740550048) dan **E3** (baru 120252834740980048).
  - **SELEPAS BELI** = Deep Dive ad set 120252809186890048 kini Pembeli 180H sahaja, RM5.
  - **Pause**: kempen Minggu 1 (120252739207400048) dan Carousel (120252778455590048).
  - Semua tiada ralat; read-back: 4 kempen ACTIVE (TOP 15, MIDDLE 15, BOTTOM 10, Deep Dive 5), iklan IN_PROCESS (semakan Meta). Video diupload ke Meta (6 video + 3 thumbnail).
- 20 Nov (malam, Sir: "Deep dive tu tak perlu.. itu terus masuk retargetting.. pembeli kita belum banyak.. Atau awak akses semua yang membeli ebook. Jadikan audience"): **Pause kempen Deep Dive** (120252809186400048). Bajet BOTTOM RM10 → **RM15**. Jumlah kekal RM45 (TOP 15, MIDDLE 15, BOTTOM 15). Senarai pembeli BCL: 79 pembeli berjaya (tidak termasuk test Sir). Cipta Custom Audience senarai pelanggan melalui API **gagal**: akaun iklan perlu dimasukkan ke Business portfolio (ralat 1870050). Fail CSV (emel, telefon, nama, negara) disediakan di scratchpad untuk Sir upload sendiri di Ads Manager; **tidak disimpan dalam repo** (data peribadi).
- 20 Nov (20:28): Semakan status: **semua 9 iklan funnel ACTIVE** (lulus review Meta): TOP T1/T2/T3, MIDDLE M1/M2, BOTTOM RP1/R1/H1/E3. Tiada ralat. Iklan baru belum ada impression lagi (baru lulus).
- 20 Nov: Sir: "Result kita pantau kalau dah 24jam". Semakan pertama funnel baru dianjak ke **21 Nov 8:30 malam** (24 jam selepas iklan lulus). Tiada perubahan iklan sebelum itu.
- 20 Nov: Peraturan baru Sir: **setiap ad set = 3 video + 2 poster**. Direkod dalam skill dan `09-setting-iklan-standard.md`.
- 20 Nov: Ayat WhatsApp engage semula + voucher (PREVIEW10, SD01) ditambah di `06-organik-whatsapp-threads.md`.
- 21 Nov (pagi): Semak Murpati (014-771 1169): sejak iklan MIDDLE lulus, hanya **1 lead iklan sebenar** (Yusoff, dari M1, 1:08 pagi). Meta lapor 2 "conversation started". Nombor ini disambung melalui QR, jadi Murpati tidak rekod rujukan iklan (from_ad kosong). Untuk kira lead iklan: guna Murpati sebagai sumber sebenar, kenal pasti melalui mesej pertama (cadangan: tukar mesej isi automatik kepada "SKRIP").
- 21 Nov: 2 auto-reply keyword Murpati ditulis (nombor 014-771 1169), **masih OFF** sehingga Sir hidupkan di Murpati > Auto Reply: (1) "Iklan SKRIP - skrip percuma" (trigger: SKRIP, "Can I get more info on this", "maklumat lanjut tentang ini", "nak skrip"; tunggu 8 saat; hantar skrip harga percuma + tanya owner/team/ejen); (2) "Link ebook + PREVIEW10" (trigger: PREVIEW10, link ebook, nak beli ebook, macam mana nak beli; hantar link preview + kod).
- 21 Nov: Atas permintaan Sir, auto-reply SKRIP dipecah 2 chat: (1/2) headline (tunggu 5 saat), (2/2) salam + skrip + soalan (tunggu 12 saat), trigger sama. Kedua-dua masih OFF. Jumlah peraturan: 3/5.
- 21 Nov: Auto-reply SKRIP ditukar kepada ayat Sir sendiri (chat 1: headline + soalan fokus closing; chat 2: iklan cukup & konsisten, isu lead bukan tak terer). Masih OFF. Gaya ayat Sir direkod di `14-gaya-ayat-sir-dharma.md`.
- 21 Nov: Skrip rekomen + harga (5 jenis prospek, jadual harga, bantahan) ditulis di `15-skrip-rekomen-harga.md`, ikut gaya ayat Sir.
- 21 Nov: Skrip rekomen v2 (Sir: tak perlu tanya, terus rekomen + link + urgency). Akses Google Drive ke fail ebook disahkan (PDF Ebook 2026 boleh dibaca).
- 21 Nov: Auto-reply "Iklan SKRIP (3/3) - rekomen + link" ditulis (tunggu 22 saat): rekomen general Ebook 2026 + RM37/PREVIEW10 + link preview + urgency jujur (kos menunggu, tiada tarikh palsu). Masih OFF. Peraturan Murpati: 4/5.
- 21 Nov (petang): Belajar gaya chat Sir dari Murpati (4 lead iklan WhatsApp setakat 6 petang: Yusoff, Dandarawi, Shafiq/LG, Dila/takaful). Corak direkod di `14-gaya-ayat-sir-dharma.md`. Ayat rekomen versi 2b (general/hartanah/owner) disimpan di `15`.
- 21 Nov: 6 template Murpati ditulis (`16-template-murpati.md`). Gagal masuk ke Murpati: sambungan kekurangan kebenaran savedreplies:write; Sir perlu sambung semula Murpati. Template "Receive Payment" sedia ada masih ada [link group pembeli].
- 21 Nov (6:33 petang): Selepas Sir sambung semula Murpati, **6 template Saved Replies dimasukkan** (/harga, /kupon, /link, /detail, /kenapa, /terima). Template "Receive Payment" dibetulkan: [link group pembeli] → link group sebenar.
- 21 Nov: Skill baru `.claude/skills/whatsapp-closing-sirdharma/` (flow ebook Bab 3 dengan rujukan muka surat, gaya human Sir, produk/harga/kupon, setup Murpati). Ebook 2026 dibaca dari Google Drive; isi ebook tidak disalin ke repo (repo awam), hanya rujukan muka surat. Skrip rekomen versi 3 (ikut flow ebook + human) di `15`.
- 21 Nov: 24 gambar dimuat naik ke Media Gallery Murpati (mockup, cover, 5 testimoni, gambar auto TY/FU, 2 poster, 8 cover produk, 5 cover framework). Tiada cover: Framework Takaful, Produk Kesihatan, Gadget.
- 23 Nov: Fail `HANDOFF-COWORK.md` dibuat untuk pindah kerja ke Cowork (ringkasan keadaan, peraturan, tindakan tertangguh, cara report jimat token).
- 23 Nov (16:00): Report harian 22 Nov ditambah dalam `03-result-harian.md` (sesi Cowork). Tiada perubahan iklan/BCL/Murpati.
- 25 Nov: Audience baru **"Video Tips 50% 30H"** (120252891870510048), ENGAGEMENT dari Page: orang yang tengok video Page sekurang-kurangnya 50% dalam 30 hari. Anggaran ~1,000 orang, sedang diisi (status 441). Percubaan audience ThruPlay ikut ID video tertentu gagal (ralat 2654). Belum dipasang pada mana-mana ad set.
- 25 Nov: Audience **"Video ThruPlay 30H"** (120252891886570048) dibuat dari Page (event thruplay_watched, 30 hari), sedang diisi. WhatsApp dah okay (Sir). Brief kreatif struktur baru: 4 video + 4 poster baru.
- 25 Nov: 7 video tips versi laju (T1–T7, 12 saat) siap. 9 fail dimuat naik ke Google Drive folder "Iklan Sir Dharma - Video Final". 5 fail 9:16 (T3–T7) gagal: melebihi had 3.1 MB setiap upload dari sesi ini.
- 25 Nov: SFX ditambah pada semua 7 video (slam, whoosh, pop mesej, bunyi taip, impact, ding harga, klik CTA), disegerakkan dengan animasi. Semua 14 video kini bawah 3.1 MB dan **semua dimuat naik ke Drive** (versi lama tanpa SFX dipindah ke Trash). Skrip render/SFX disimpan di `ads/video-tips/tools/`.
- 25 Nov: Sir lulus versi audio punchy ("much better"). 14 video final (T1–T7, beat 128 BPM + SFX) dimuat naik ke Drive "Iklan Sir Dharma - Video Final"; versi lama dipindah ke Trash. Semua fail bawah 3 MB.
- 25 Nov: **Draf iklan struktur baru (belum publish).** 13 video V2 + 2 thumbnail dimuat naik ke Meta (semua ready).
  - TOP (120252834701930048): bajet RM15 → RM10 (draf). 3 iklan baru PAC (9:16 story/reels + 4:5 feed): T2 Bluetick, T3 Owner 3 Nombor, T7 Bila Follow Up → sales page ebook-sirdharma.
  - MIDDLE baru (120252892405900048, Sales Website, RM25 CBO): ad set 120252892406320048 optimasi Purchase, audience Video 50% + ThruPlay + IG/Page Engaged + Website 30H, exclude Pelawat SP 14H / Mula Bayar 14H / Pembeli 180H, identiti Malaysia diset. 3 iklan PAC: T4 Lepas Harga, T6 Tak Reply, T5 Follow Up Memaksa (CTA Shop Now, RM37).
  - BOTTOM WhatsApp (guna semula 120252834702000048, nama baru, RM15 → RM10 draf): audience Pelawat SP 14H + Mula Bayar 14H + ThruPlay, exclude Pembeli. 2 iklan WhatsApp video: T1 Tips Harga, T4 Lepas Harga (PREVIEW10). M1/M2 lama dipause (kempen memang paused, tiada kesan live).
  - Bila publish: pause iklan TOP lama T1/T2/T3 dan kempen Retarget Sales 120252750115110048. Jumlah bajet jadi RM45/hari.
- 25 Nov: **Sir: "Okay publish".** Struktur baru live: TOP RM10 (T2/T3/T7 V2), MIDDLE Sales Website RM25 (T4/T6/T5), BOTTOM WhatsApp RM10 (T1/T4 V2). Dipause: iklan TOP lama T1/T2/T3, kempen Retarget Sales 120252750115110048. Jumlah RM45/hari. 8 iklan baru dalam review Meta (IN_PROCESS). Pantau 48 jam.
- 25 Nov: Senarai iklan live penuh (ayat, headline, link video Drive, ID) di `17-iklan-live.md`. Skill iklan dikemas kini: struktur funnel baru + peraturan pantau CTR (arahan Sir). HANDOFF-COWORK dikemas kini.
- 25 Nov: `CLAUDE.md` dibuat (dibaca automatik setiap sesi): keadaan semasa, peraturan Sir, peta fail ikut tugas, tip jimat token.
- 26 Nov: Sir beri export Murpati (2,029 nombor, group Database Kelas SD) untuk custom audience. Fail bersih dibuat di luar repo (bukan pembeli 1,971 · dah beli 58). Cipta customer list audience gagal lagi: ralat 1870050, akaun iklan belum masuk Business portfolio. Tunggu Sir.
- 26 Nov: Sir masukkan akaun iklan ke Business portfolio dan accept terma Custom Audience. 2 customer list audience dicipta (kosong, tunggu Sir upload CSV): Murpati Bukan Pembeli 120252910518420048 · Murpati Dah Beli Ebook 120252910518500048.
- 26 Nov: Audience ketiga dicipta (kosong, tunggu upload): Kenalan HP Sir · Bukan Pembeli 120252910552100048 (6,073 nombor kenalan telefon Sir, tolak pembeli). Senarai pembeli digabung dari 2 export = 65 nombor. Fail di luar repo.
- 26 Nov: Draf (belum publish) ad set baru dalam MIDDLE 120252910616860048: Kenalan HP Sir + Group Kelas SD, exclude Pembeli Murpati + Pembeli 180H, Purchase, tiada bajet tambahan (kongsi CBO RM25). Iklan K1 'Kenalkan Diri Sir + PREVIEW10' 120252910620330048, poster ads/creative/kenalan-4k.jpg, image_hash 40196416a49e30fae327f3b95ae96ed4 disahkan dalam draf, link preview-ebook-2026.
- 26 Nov: Video K1 'Kenalkan diri Sir + PREVIEW10' (12s, 9:16 + 4:5, beat + SFX) siap: ads/video-tips/out/k1_*.mp4 (config 8 dalam tips.html). Belum dimasukkan ke iklan.
- 26 Nov: Video K1 dimuat naik ke Meta (9:16 1864018681383433, 4:5 1169333562255243) dan Drive folder Video Final. Draf iklan 'MID K1 Video' 120252911090300048 (PAC) ditambah dalam ad set 120252910616860048. Belum publish, tunggu poster Gemini.
