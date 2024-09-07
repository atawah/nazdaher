from odoo import models, fields, api
import qrcode
import logging
import base64  # Add this line to import the base64 module
import io  # Add this line to import the io module
_logger = logging.getLogger(__name__)

class AssetQrCode(models.Model):
    _inherit = 'account.asset.asset'

    url = fields.Char("Link", compute="generate_qr_code")
    qr_image = fields.Binary("QR Image", compute="generate_qr_code")

    @api.depends('url')
    def generate_qr_code(self):
        for record in self:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(record.url)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")
            qr_image_byte_array = io.BytesIO()
            qr_image.save(qr_image_byte_array, format='PNG')
            qr_image_binary = base64.b64encode(qr_image_byte_array.getvalue())
            record.qr_image = qr_image_binary

            record.url = "http://localhost:8069/web#id=" + str(record.id) + "&view_type=form&model=account.asset.asset&action=286"