

from odoo import models, fields, api
import qrcode
import base64
from io import BytesIO

class AssetQrCode(models.Model):
    _inherit = 'account.asset.asset'

    qr_code_image = fields.Binary("QR Code", attachment=True)
    qr_code_url = fields.Char("QR Code URL", compute="_compute_qr_code_url")

    @api.depends('name')
    def _compute_qr_code_url(self):
        for record in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            record.qr_code_url = f"{base_url}/web#id={record.id}&model=account.asset&view_type=form"

    @api.model
    def create(self, vals):
        res = super(AssetQrCode, self).create(vals)
        res._generate_qr_code()
        return res

    def write(self, vals):
        res = super(AssetQrCode, self).write(vals)
        self._generate_qr_code()
        return res

    def _generate_qr_code(self):
        for record in self:
            if record.qr_code_url:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(record.qr_code_url)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                record.qr_code_image = qr_image
