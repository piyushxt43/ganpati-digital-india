"""QR generator using python-qrcode (open source, github.com/lincolnloop/python-qrcode)."""
import sys, qrcode
from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import VerticalGradiantColorMask
import qrcode.image.svg

URL = sys.argv[1]

def base():
    q = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=40, border=4)
    q.add_data(URL); q.make(fit=True); return q

# 1. Plain high-contrast — most reliable for print
base().make_image(fill_color=(21, 33, 63), back_color="white").save("qr/qr-plain.png")

# 2. Saffron -> green tricolour gradient, rounded modules
base().make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=VerticalGradiantColorMask(
        back_color=(255, 255, 255), top_color=(224, 90, 21), bottom_color=(21, 105, 74)),
).save("qr/qr-tricolour.png")

# 3. Vector for large-format printing
f = qrcode.image.svg.SvgPathImage
q = qrcode.QRCode(error_correction=ERROR_CORRECT_H, border=4, image_factory=f)
q.add_data(URL); q.make(fit=True); q.make_image().save("qr/qr-plain.svg")

print("version:", base().version, "| url:", URL)
