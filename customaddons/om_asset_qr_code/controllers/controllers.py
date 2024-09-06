# -*- coding: utf-8 -*-
# from odoo import http


# class AssetQrCode(http.Controller):
#     @http.route('/asset_qr_code/asset_qr_code', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asset_qr_code/asset_qr_code/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asset_qr_code.listing', {
#             'root': '/asset_qr_code/asset_qr_code',
#             'objects': http.request.env['asset_qr_code.asset_qr_code'].search([]),
#         })

#     @http.route('/asset_qr_code/asset_qr_code/objects/<model("asset_qr_code.asset_qr_code"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asset_qr_code.object', {
#             'object': obj
#         })

