# -*- coding: utf-8 -*-
{
    'name': 'Asset QR Code',
    'version': '1.0',
    'summary': 'Adds QR code to each asset with a link to its page',
    'author': 'ATAWAH SPC',
    'category': 'Accounting',
    'depends': ['om_account_asset', 'web', 'base'],
    'data': [
        'views/asset_qr_code_view.xml',
        'security/ir.model.access.csv',
            ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
