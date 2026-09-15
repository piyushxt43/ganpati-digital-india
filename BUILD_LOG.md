# Build log — 2026-09-15

**Task:** QR-scannable landing page for a Ganesh Chaturthi "Digital India" rangoli.

1. Sourced rangoli image from `~/Downloads/WhatsApp Image 2026-09-15 at 09.56.55.jpeg`,
   copied to `assets/` and downscaled to 1200px.
2. Built `index.html` — Yatra One + Mukta type, kolam-dot rails, sand/marigold/kumkum/peacock
   palette, light + dark themes. Content: shlok, rangoli image, 8 pillar cards linking to
   official sites (NPCI, UIDAI, DigiLocker, ONDC, IndiaAI, BHASHINI, BharatNet, services.india.gov.in),
   everyday-life grid, tradition→tech bridge, closing blessing.
3. Published as Artifact → https://claude.ai/artifact/Ua3rPhfWRJZtNNJ5U6ANop
4. Installed `qrcode[pil]` (github.com/lincolnloop/python-qrcode) into `.venv`.
5. Generated QR v6, ECC level H, in 3 formats via `qr/make_qr.py`.

6. Artifact URL required a Claude login — scanners landed on the Claude homepage. Replaced with
   public static hosting: wrapped index.html as a standalone document (doctype/head/body, viewport,
   OG tags), pushed to github.com/piyushxt43/ganpati-digital-india, enabled GitHub Pages.
7. Regenerated all three QR files against https://piyushxt43.github.io/ganpati-digital-india/ — verified live (page 200, image 200).

**Status:** done. QR scans to a public page, no login.
