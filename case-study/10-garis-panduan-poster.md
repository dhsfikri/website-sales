# 10 · Garis panduan poster (arahan Sir, 19 Nov)

Setiap poster iklan mesti ada 4 ciri ini:

| Ciri | Maksud dalam reka bentuk |
|---|---|
| **Premium** | Warna brand (hijau gelap #0b3b2c, kuning #ffd21f), ruang lapang, font Poppins tebal, tiada elemen murah/berselerak |
| **Realistic** | Foto sebenar Sir / sesi sebenar. UI sebenar (notifikasi WhatsApp gaya iPhone, chat sebenar). **Tiada kartun, emoji besar, bentuk lukisan atau ilustrasi** |
| **4K clarity** | Render 2x (2160×2700 untuk 4:5). Guna foto resolusi tinggi; elak besarkan foto kecil |
| **Cinematic** | Foto penuh dengan gradient gelap (vignette), cahaya dramatik, kedalaman (latar kabur, subjek tajam) |

Rujukan yang Sir suka: `ads/creative/deepdive-d5.png`, `deepdive-d6.png` (v3). Sumber: `ads/creative/deepdive-v3.html`.

Yang Sir tolak: gaya animasi/kartun (`deepdive-d3/d4`, baldi, emoji).

Nota: foto paling tajam yang ada: `konsultasi.jpg` (1400px), `pentas-influence.jpg` (1400px), `hero-whiteboard.jpg` (1200px). Foto lain ≤1000px; untuk 4K sebenar, perlukan foto asal resolusi penuh dari Sir.

## Wajib: semak gambar sebelum publish (pelajaran 20 Nov)
Kes: iklan H1 Hartanah dan RP1 keluar dengan gambar preview link BCL (banner bcl.my), bukan poster kita. Punca: `image_url` diletak di luar `link_data`, jadi Meta abaikan dan ambil gambar OG dari link.

Langkah wajib untuk setiap iklan baru atau tukar gambar:
1. Upload poster dahulu (ads_create_creative dengan image_url) dan ambil `image_hash`.
2. Bina creative inline dengan `link_data.image_hash` (atau `child_attachments[].image_hash` untuk carousel). Jangan guna `image_url` di luar link_data.
3. Sebelum minta Sir publish: baca semula draf dan pastikan `image_hash` dalam draf **sama** dengan hash poster yang diupload. Jika tiada hash atau hash lain, jangan publish.
4. Lepas publish: baca semula creative live dan sahkan hash sekali lagi.
