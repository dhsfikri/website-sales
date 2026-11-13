# Sir Dharma Sales System — Landing Page

Landing page statik untuk jual ebook closing WhatsApp (Fasa 1).

- `index.html` — satu fail, tiada build step. Sesuai untuk Cloudflare Pages / GitHub Pages.
- Semua butang beli → form BCL `https://sweetcactusenterprise.bcl.my/form/ebook-sirdharma`
- Meta Pixel: SirDharma 2026 (`255927347311677`) — PageView, ViewContent, InitiateCheckout, Contact
- Butang WhatsApp → 016-767 7759

## Versi BCL (hos utama)
- `bcl/sales-page-bcl.html` — versi yang dimasukkan ke form BCL `ebook-sirdharma` (jenis Custom HTML).
- Gambar diambil dari media library BCL (platform-bcl.bsb-cdn.com), bukan dari folder `assets/`.
- Tiada JavaScript; semua butang beli ke `#bayar` (borang bayaran BCL pada halaman yang sama).
- Bila ubah `index.html`, kemas kini fail ini juga dan hantar semula ke BCL.
