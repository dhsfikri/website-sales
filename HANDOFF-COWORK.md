# Handoff ke Cowork · Ebook Sir Dharma (dikemas kini 25 Nov 2026)

Baca fail ini dulu. Semua butiran ada dalam fail yang dirujuk; jangan baca semua sekali gus (jimat token).

## Matlamat
Jual Ebook 2026 "Wassap Masih Relevan?" (RM37, asal RM67) + framework/bundle. Sasaran RM10,000. Jualan sebenar setakat 22 Nov: **RM317.60**. Bajet iklan bawah **RM50/hari** (sekarang RM45).

## Peraturan Sir (wajib)
- Bahasa Melayu santai, panggil "Sir". Tak faham, tanya.
- Iklan: draf dulu, publish hanya bila Sir kata "publish"/"OK". Jangan ubah bajet tanpa izin.
- Setiap ad set: 3 video + 2 poster. Poster premium, realistik, 4K, cinematic (`case-study/10-garis-panduan-poster.md`). Semak image_hash sebelum publish.
- **Repo awam**: jangan simpan nama/nombor prospek, URL webhook, isi ebook, atau token.
- Log setiap perubahan: `case-study/04-changelog.md`; result: `case-study/03-result-harian.md`.

## Skill (baca bila perlu)
- `.claude/skills/iklan-meta-sirdharma/SKILL.md`: akaun Meta, struktur funnel, setting standard, resipi creative.
- `.claude/skills/whatsapp-closing-sirdharma/SKILL.md`: flow ebook (rujukan muka surat), gaya chat Sir, produk/harga/kupon, setup Murpati.

## Keadaan sekarang
**Meta (akaun 1235454997962640)**: struktur baru publish 25 Nov, RM45/hari. Senarai penuh iklan + ayat + link video: `case-study/17-iklan-live.md`.
| Lapisan | Kempen | Bajet |
|---|---|---|
| TOP | 120252834701930048 Traffic LPV, video V2 T2/T3/T7 | RM10 |
| MIDDLE | 120252892405900048 Sales Website (Purchase), video T4/T6/T5 | RM25 |
| BOTTOM | 120252834702000048 WhatsApp SKRIP, video T1/T4 (PREVIEW10) | RM10 |
| Dipause | Retarget Sales 120252750115110048, TOP lama T1–T3, M1/M2, Deep Dive, Minggu 1, Carousel, Story Preview | |
Pantau CTR (arahan Sir): sasaran ≥1% TOP/MIDDLE, ≥1.5% BOTTOM.

**BCL (sweetcactusenterprise.bcl.my)**
| Form | Slug | Kegunaan (remarks dalam transaksi) |
|---|---|---|
| 21578 | ebook-sirdharma | Iklan/sales page ("Toolkit Team Sales"), semua 17 produk |
| 21730 | preview-ebook-2026 | Retarget + kupon ("Preview Ebook 2026 (Retarget)") |
| 22024 | sd-wa | WhatsApp ("Kedai Ebook Sir Dharma - WhatsApp") |
| 22025 | sd-th | Threads |
- Sales page live: `bcl/ebook-reply-style.html` (21578, 22025, 22024); retarget: `bcl/retarget-bcl.html` (21730). Kemas kini guna `update_form_content`.
- Pixel 255927347311677 + CAPI aktif pada form (jangan salin token). Selepas bayar → `terima-kasih.html`.
- Webhook Murpati (TY bayar + follow up tak bayar) pada keempat-empat form; URL hanya dalam BCL.
- Kupon: PREVIEW10 (10%, tiada luput), SD01 (25%, pembeli lama).
- Produk & harga penuh: skill `whatsapp-closing-sirdharma` bahagian 4.
- Kira jualan: `list_transactions` status success; buang transaksi test Sir (nama/emel Dharma).
- 79 pembeli berjaya (CSV untuk audience Meta tidak disimpan dalam repo).

**Murpati (014-771 1169)**: auto-reply SKRIP 1/3–3/3 ON (Sir), Link PREVIEW10. 7 template (/harga /kupon /link /detail /kenapa /terima + Receive Payment). 24 gambar dalam Media Gallery.

## Tindakan tertangguh (tunggu Sir)
1. (Selesai 25 Nov) Struktur bajet baru TOP 10 / MIDDLE 25 / BOTTOM 10.
2. Kreatif ikut 3 video + 2 poster: semua ad set perlu 2 poster; BOTTOM perlu 1 video lagi.
3. Semak mesej isi automatik iklan WhatsApp = "SKRIP".
4. (25 Nov) Draf creative baru 8 iklan live (video hook dari frame 0 + thumbnail betul) tunggu Sir kata "publish". Publish: `ads_activate_entity` pada 8 ad ID dalam `case-study/17-iklan-live.md`, kemudian baca live dan sahkan hash thumbnail.
4. Audience senarai pembeli: Sir perlu masukkan akaun iklan ke Business portfolio, kemudian upload CSV (fail di luar repo).
5. Cover framework belum ada: Takaful, Produk Kesihatan, Gadget.
6. Buang nama prospek lama dari `case-study/03`, `04`, `14` (repo awam).
7. Fast Action Bonus (ebook m/s 67–70): cadangan free 1 framework jika bayar dalam 24 jam, perlu kelulusan Sir.

## Report harian (cara jimat token)
1. Meta: `ads_get_ad_entities` level ad, `date_preset` yesterday, filter campaign.id 3 kempen di atas, fields: amount_spent, impressions, link_click, landing_page_view, omni_initiated_checkout, omni_purchase, results, cost_per_result.
2. BCL: `list_transactions` (status all, tarikh semalam–hari ini).
3. Murpati: `list_conversations` number 60147711169, limit 15.
4. Tulis 1 baris dalam `03-result-harian.md` (tanpa nama), lapor ringkas kepada Sir.
