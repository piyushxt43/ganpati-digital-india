# Ganpati Bappa — Digital India QR

**Live page:** https://piyushxt43.github.io/ganpati-digital-india/
**Repo:** https://github.com/piyushxt43/ganpati-digital-india

Public static page on GitHub Pages — opens for anyone, no login.

## Files
- `index.html` — the landing page source
- `assets/ganpati-digital-india.jpg` — rangoli image (1200px)
- `qr/qr-plain.png` — 1960px indigo-on-white QR (best for print)
- `qr/qr-tricolour.png` — saffron→green gradient, rounded modules
- `qr/qr-plain.svg` — vector, for large-format printing
- `qr/make_qr.py` — generator script

## Regenerate
```
.venv/bin/python qr/make_qr.py "<url>"
```

## QR generator
[python-qrcode](https://github.com/lincolnloop/python-qrcode) (BSD) — error correction level H
(~30% recoverable), so the code still scans with sand dust, glare or a partial smudge on it.

## Printing tips
- Minimum printed size **10×10 cm**; bigger is better for a floor rangoli.
- Keep the white border (quiet zone) — do not crop it or fill it with rangoli colour.
- Print on paper/board and place it on the rangoli; don't draw the QR in loose powder.
