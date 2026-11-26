# CLAUDE.md · Projek Sir Dharma (baca dulu, jangan baca semua fail)

**Bahasa: SENTIASA balas dalam Bahasa Melayu Malaysia santai. Panggil "Sir". Tak faham, tanya.**

## Matlamat
Jual Ebook 2026 "Wassap Masih Relevan?" (RM37, asal RM67) + framework/bundle. Sasaran RM10,000.

## Peraturan Sir (wajib)
- Iklan: draf dulu, publish hanya bila Sir kata "publish"/"OK". Jangan ubah bajet tanpa izin. Jumlah bajet < RM50/hari.
- Repo AWAM: jangan simpan nama/nombor prospek, URL webhook, token, atau isi ebook.
- Log setiap perubahan: `case-study/04-changelog.md` (1 baris). Result harian: `case-study/03-result-harian.md`.
- Poster premium, realistik, 4K; semak image_hash sebelum publish. Setiap ad set: 3 video + 2 poster.

## Keadaan semasa (kemas kini setiap kali struktur berubah)
- Meta akaun 1235454997962640 · Page 111701606844448 · IG 17841410538491353 · Pixel 255927347311677
- Struktur live 25 Nov (RM45/hari): TOP 120252834701930048 (RM10) · MIDDLE 120252892405900048 (RM25) · BOTTOM WhatsApp 120252834702000048 (RM10)
- MIDDLE juga ada ad set retarget kenalan (Kenalan HP + Group Kelas SD, exclude pembeli) dengan video K1 kenalkan diri + PREVIEW10.
- Senarai iklan, ayat & link video: `case-study/17-iklan-live.md`
- Pantau CTR: sasaran ≥1% TOP/MIDDLE, ≥1.5% BOTTOM.
- BCL forms: 21578 ebook-sirdharma · 21730 preview-ebook-2026 · 22024 sd-wa · 22025 sd-th · Kupon PREVIEW10 (10%), SD01 (25%)
- Murpati 014-771 1169: auto-reply SKRIP 1/3–3/3 ON, template /harga /kupon /link /detail /kenapa /terima

## Fail mana untuk tugas apa (baca yang perlu sahaja)
| Tugas | Baca |
|---|---|
| Iklan Meta (cipta, edit, report) | `.claude/skills/iklan-meta-sirdharma/SKILL.md` |
| Ayat WhatsApp, auto-reply, closing | `.claude/skills/whatsapp-closing-sirdharma/SKILL.md` |
| Video motion | `ads/video-tips/tips.html` + `ads/video-tips/tools/` |
| Poster | `case-study/10-garis-panduan-poster.md` |
| Sales page BCL | `bcl/` |
| Tindakan tertangguh | `HANDOFF-COWORK.md` bahagian "Tindakan tertangguh" |

## Jimat token
- Report: minta field yang perlu sahaja (amount_spent, ctr, link_click, landing_page_view, IC, purchase). Guna `hide_ui: true` untuk banyak create.
- Jangan baca `03-result-harian.md` / `04-changelog.md` penuh; guna `tail`.
- Jangan baca semula fail yang dah ada dalam konteks.
