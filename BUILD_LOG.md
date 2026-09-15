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

**Open item:** artifact must be shared publicly by the user before the QR is usable by others.
