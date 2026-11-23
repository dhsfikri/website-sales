# Handoff ke Cowork · Ebook Sir Dharma (23 Nov 2026)

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
**Meta (akaun 1235454997962640)**
| Lapisan | Kempen | Bajet | Status |
|---|---|---|---|
| TOP | 120252834701930048 Traffic LPV, video tips T1/T2/T3 | RM15 | Jalan baik (~RM0.24/LPV; T3 & T2 menang) |
| MIDDLE | 120252834702000048 WhatsApp "SKRIP", M1/M2 | RM15 | M1 bawa lead & 1 jualan; M2 hampir tiada delivery |
| BOTTOM | 120252750115110048 Retarget Sales: RP1, R1, H1, E3 | RM15 | Lemah (CPM tinggi, 0 IC) |
| Dipause | Minggu 1, Carousel, Deep Dive, Story Preview | | |

**BCL**: form 21578 ebook-sirdharma, 21730 preview-ebook-2026, 22024 sd-wa, 22025 sd-th. Webhook Murpati (TY + follow up tak bayar) pada semua form. Kupon PREVIEW10 (10%), SD01 (25%).

**Murpati (014-771 1169)**: auto-reply SKRIP 1/3–3/3 ON (Sir), Link PREVIEW10. 7 template (/harga /kupon /link /detail /kenapa /terima + Receive Payment). 24 gambar dalam Media Gallery.

## Tindakan tertangguh (tunggu Sir)
1. Bajet: BOTTOM RM15 → RM10, MIDDLE RM15 → RM20; pause M2. (Sir belum kata OK.)
2. Kreatif baru ikut 3 video + 2 poster: TOP perlu 2 poster; MIDDLE 1 video + 2 poster; BOTTOM 3 video.
3. Tukar mesej isi automatik iklan WhatsApp kepada "SKRIP".
4. Audience senarai pembeli: Sir perlu masukkan akaun iklan ke Business portfolio, kemudian upload CSV (fail di luar repo).
5. Cover framework belum ada: Takaful, Produk Kesihatan, Gadget.
6. Buang nama prospek lama dari `case-study/03`, `04`, `14` (repo awam).
7. Fast Action Bonus (ebook m/s 67–70): cadangan free 1 framework jika bayar dalam 24 jam, perlu kelulusan Sir.

## Report harian (cara jimat token)
1. Meta: `ads_get_ad_entities` level ad, `date_preset` yesterday, filter campaign.id 3 kempen di atas, fields: amount_spent, impressions, link_click, landing_page_view, omni_initiated_checkout, omni_purchase, results, cost_per_result.
2. BCL: `list_transactions` (status all, tarikh semalam–hari ini).
3. Murpati: `list_conversations` number 60147711169, limit 15.
4. Tulis 1 baris dalam `03-result-harian.md` (tanpa nama), lapor ringkas kepada Sir.
