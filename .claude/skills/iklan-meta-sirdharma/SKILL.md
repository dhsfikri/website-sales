---
name: iklan-meta-sirdharma
description: Peraturan dan resipi untuk cipta, edit, publish dan report iklan Meta (Facebook/Instagram/WhatsApp) Sir Dharma bagi Ebook 2026 dan Deep Dive. Guna setiap kali sentuh iklan Meta, poster iklan, bajet, atau report iklan dan BCL.
---

# Iklan Meta Sir Dharma

Bahasa: Melayu Malaysia santai, panggil "Sir". Jika arahan tak jelas, tanya dulu.
Log setiap perubahan dalam `case-study/04-changelog.md` dan result dalam `case-study/03-result-harian.md`.

## Akaun
- Ad account 1235454997962640, Page 111701606844448, IG user 17841410538491353, pixel 255927347311677.
- Identiti verified Malaysia: `regional_regulated_categories` ["MALAYSIA_UNIVERSAL","VOLUNTARY_VERIFICATION"], `regional_regulation_identities` {"universal_beneficiary":"2037511550243904","universal_payer":"2037511550243904"}. Wajib pada ad set baru, jika tidak keluar ralat "Advertiser is missing".

## Peraturan kerja (dari Sir)
1. Cipta semua sebagai **draf**. Publish hanya bila Sir tulis **"publish"** (atau arahan jelas seperti "boleh jalan").
2. Draf kena sekatan: ingatkan Sir; jika Sir lambat, semak semula sendiri.
3. Jangan hidupkan iklan atau ubah bajet tanpa izin jelas Sir.
4. **Jumlah bajet harian di bawah RM50** (sekarang RM45). Sir set account spending limit sendiri sebagai brek.
5. Pause iklan yang lemah (belanja tanpa IC/purchase, atau 0 klik). Pause boleh terus (edit live).

## Struktur funnel (sejak 20 Nov, RM45/hari)
| Lapisan | Kempen | Audience | Bajet |
|---|---|---|---|
| TOP | 120252834701930048 Traffic LPV, video tips percuma → sales page | MY 25–55 A+A, exclude Pembeli 180H + Pelawat SP 14H | RM15 |
| MIDDLE | 120252834702000048 Engagement → WhatsApp "SKRIP" | IG/Page Engaged + Website 30H, exclude Pembeli, Pelawat SP 14H, Mula Bayar 14H | RM15 |
| BOTTOM | 120252750115110048 Sales Purchase (RP1, R1, H1, E3) | Pelawat SP 14H + Mula Bayar 14H (120252834701800048), exclude Pembeli | RM15 |
| (dipause 20 Nov) | Deep Dive 120252809186400048 | Pembeli 180H | - |
Hartanah (H1) hanya di BOTTOM, bukan untuk orang sejuk (arahan Sir).

## Kreatif setiap ad set (arahan Sir 20 Nov)
- Setiap ad set: **3 video + 2 poster** (5 iklan).
- Video: 15 saat, 9:16 (story/reels) + 4:5 (feed) melalui placement customization; template `ads/video-tips/tips.html`.
- Poster: ikut `case-study/10-garis-panduan-poster.md` (premium, realistic, 4K, cinematic) dan semak image_hash.

## Setting standard ad set
- Lokasi Malaysia. Bahasa `locales` [41, 1001] (Malay + English All).
- Placement sahaja: `publisher_platforms` [facebook, instagram], `facebook_positions` [feed, story, facebook_reels], `instagram_positions` [stream, story, reels].
- Exclude Pembeli 180 hari (120252750113400048) kecuali kempen yang sasar pembeli (Deep Dive).
- Advantage+ Audience: jangan hantar `age_max` keras; guna `age_range`. Custom-audience-only: `advantage_audience` 0 + `advantage_audience_off_reason` CUSTOM_AUDIENCE_ONLY.

## Gambar iklan (WAJIB, pelajaran 20 Nov)
Kes: H1 dan RP1 keluar dengan banner bcl.my sebab `image_url` diletak di luar `link_data`; Meta ambil gambar preview link.
1. Upload poster: `ads_create_creative` dengan `image_url` (raw.githubusercontent.com dipin pada commit SHA yang dah di-push), kemudian `ads_get_creatives` untuk dapatkan `image_hash`.
2. Creative iklan inline: `object_story_spec.link_data.image_hash` (carousel: `child_attachments[].image_hash`). Jangan sekali-kali guna `image_url` di luar link_data.
3. Sebelum minta publish: baca draf (`object_state=draft`) dan sahkan `image_hash` sama dengan poster. Tiada hash / hash lain = jangan publish.
4. Lepas publish: baca creative live, sahkan hash sekali lagi.

## Iklan WhatsApp (Click-to-WhatsApp)
- Creative inline: `link_data.link` "https://api.whatsapp.com/send", `image_hash`, `call_to_action` {"type":"WHATSAPP_MESSAGE","value":{"app_destination":"WHATSAPP"}}.
- Jangan guna `ads_create_creative` untuk creative akhir (ia tambah `link_title` yang deprecated, ralat #1815589).

## Mod draf (teknikal)
- Edit pada objek live jadi draf; publish dengan `ads_activate_entity` + `object_ids`. Jangan set `publish_as_active` kecuali Sir mahu hidupkan.
- Pause terus ubah live (`is_draft=false`); jangan panggil activate untuk pause.
- Bajet dalam unit sen (RM20 = 2000).
- `start_time` tak boleh edit pada draf ad set (ralat 1487057); set `null`.
- Selepas publish, sentiasa baca semula live untuk sahkan.

## Poster
Ikut `case-study/10-garis-panduan-poster.md`: premium, realistic, 4K, cinematic, gambar sebenar (bukan kartun), guna brand kit. Render Playwright deviceScaleFactor 2.

## Report
- Meta: `ads_get_ad_entities` level ad (amount_spent, link_click, landing_page_view, omni_initiated_checkout, omni_purchase, results).
- BCL: `list_transactions` (status all). Bandingkan purchase Meta dengan jualan sebenar BCL (test Sir boleh dikira oleh pixel).
- Pixel: `ads_get_dataset_stats` (waktu Pacific).
- Peraturan sales page: IC/LPV mesti melebihi 3%.
- Jangan simpan data peribadi pembeli atau URL webhook dalam repo.
